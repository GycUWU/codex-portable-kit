---
name: application-ui-designer
description: Design, review, or refactor attractive modern UI for consumer applications, productivity tools, utilities, SaaS products, creative software, desktop/mobile/web applications, onboarding, settings, dashboards, content tools, and other non-industrial software where usability, visual hierarchy, brand character, delight, and polished interaction matter.
---

# Application UI Designer

Design application software that feels intentional, useful, and visually distinctive.

Priority:
1. User task and information hierarchy.
2. Ease of learning and navigation.
3. Strong visual concept.
4. Consistent design system.
5. Responsive/adaptive behavior.
6. Microinteraction and polish.
7. Brand expression.

Do not default to generic AI/SaaS aesthetics.

## Before design
Determine target user, core job, platform/viewport, usage frequency, content density, navigation model, emotional tone, and one visual idea that differentiates the product.
Choose a direction before coding: minimal utility, editorial, warm consumer, premium, technical productivity, creative studio, playful, or another coherent direction. Do not mix incompatible directions.

## Route by product type
- Productivity/utility: speed, shortcuts, command hierarchy, useful density, strong empty states.
- Consumer/lifestyle: approachable tone, onboarding, confidence, imagery/illustration when useful.
- SaaS/business: object hierarchy, navigation, forms/tables, progressive disclosure, clear actions.
- Creative software: workspace/canvas first, tool discoverability, inspectors, keyboard efficiency.
- Mobile: thumb reach, platform patterns, clear back behavior, adaptive keyboard handling.

## Composition before components
Start from major zones, reading order, visual anchor, dominant action, and secondary context. Do not start with a grid of cards.

## Visual hierarchy
Use scale, spacing, contrast, alignment, grouping, typography, and color. Do not depend on shadows/borders for every layer.

## Cards
Use cards only when content behaves like an independent object. Prefer open layouts, sections, dividers, list rows, split panes, and typographic grouping when appropriate.

## Color
Choose a neutral foundation, primary accent, semantic states, and optional supporting accent. Avoid default purple-blue gradients unless they fit the actual brand.

## Typography
Use at most two font families unless the concept strongly requires more. Avoid defaulting to Inter on every project. Build a deliberate scale for title, section, body, labels, and metadata.

## Motion
Use motion to preserve context, confirm actions, explain hierarchy/spatial change, and support direct manipulation. Avoid animation that slows frequent workflows.

## States
Design default, hover/focus, selected, loading, empty, error, disabled, success, and offline states when relevant.

## Responsive behavior
Specify what changes, not only what shrinks: columns collapse, panels become drawers, navigation changes form, actions move, and scroll behavior adapts.

## Avoid generic AI UI
- hero headline + three cards as universal template
- gradient blobs
- excessive glassmorphism
- meaningless sparkle icons
- identical rounded cards everywhere
- fake analytics charts
- default purple/blue accent
- oversized whitespace with little content
- random shadows
- one animation style per component

## Review
Load `references/app-review.md` before finalizing. If code can be rendered, inspect screenshots at target sizes. Review composition first, then typography/color, then micro-details.
