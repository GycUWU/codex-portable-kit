"""最小迁移回归：拒绝越界/损坏/新增负载，验证路径迁移和覆盖备份。"""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import sys
import shutil
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import install
from verify import safe, check


@contextlib.contextmanager
def workspace_temp(parent):
    # fixed by gyc 2026-09-28：权限：Windows 沙箱中继承工作区 ACL，避免 tempfile 的 0700 目录拒绝访问。
    path = parent / uuid.uuid4().hex
    path.mkdir()
    try:
        yield path
    finally:
        assert path.resolve().parent == parent.resolve()
        shutil.rmtree(path)


def main():
    test_dir = ROOT / ".test-output"
    test_dir.mkdir(exist_ok=True)
    with workspace_temp(test_dir) as work:
        work = Path(work)
        source = work / "bundle"
        source.mkdir()
        skill = source / "skills/demo/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("---\nname: demo\n---\n{{HOME_POSIX}}/.codex\n", encoding="utf-8")
        (source / "manifest.json").write_text(json.dumps({"skills": [{"directory": "demo"}]}), encoding="utf-8")
        sums = {p.relative_to(source).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in source.rglob("*") if p.is_file()}
        (source / "checksums.json").write_text(json.dumps(sums), encoding="utf-8")
        for invalid in ["../escape", "/outside", "skills/../../escape"]:
            try:
                safe(source, invalid)
            except ValueError:
                pass
            else:
                raise AssertionError("未拒绝越界路径")
        original = skill.read_bytes()
        skill.write_bytes(b"changed")
        try:
            check(source)
        except ValueError:
            pass
        else:
            raise AssertionError("未拒绝损坏负载")
        skill.write_bytes(original)
        unsigned = source / "unexpected.py"
        unsigned.write_text("print('extra')", encoding="utf-8")
        try:
            check(source)
        except ValueError:
            pass
        else:
            raise AssertionError("未拒绝未登记负载")
        unsigned.unlink()
        target = work / "target user"
        installed = target / ".agents/skills/demo/SKILL.md"
        installed.parent.mkdir(parents=True)
        installed.write_text("existing", encoding="utf-8")
        extra = installed.parent / "personal.txt"
        extra.write_text("keep", encoding="utf-8")
        saved_root, saved_argv = install.ROOT, sys.argv
        try:
            install.ROOT = source
            sys.argv = ["install.py", "--home", str(target)]
            with contextlib.redirect_stdout(io.StringIO()):
                install.main()
                install.main()
        finally:
            install.ROOT, sys.argv = saved_root, saved_argv
        assert target.as_posix() in installed.read_text(encoding="utf-8")
        assert extra.read_text(encoding="utf-8") == "keep"
        backups = list((target / ".codex/migration-backups").rglob("SKILL.md"))
        assert len(backups) == 1 and backups[0].read_text(encoding="utf-8") == "existing"
    print("迁移回归通过：越界、损坏、未登记负载、路径替换、备份、重复安装。")


if __name__ == "__main__":
    main()
