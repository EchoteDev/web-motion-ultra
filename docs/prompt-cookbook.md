# Prompt cookbook

Use these starting points with your own project context. They are example requests, not claims about completed demos.

## A useful brief

```text
Use $web-motion-ultra.
Mode: enhance an existing site / create a new page.
Project: [product, audience, and primary action].
Scope: [routes or sections].
Motion character: [editorial, playful, precise, calm, cinematic].
Intensity: [restrained, medium, bold].
Stack: [existing framework and animation dependencies].
Constraints: [content to preserve, device priorities, performance limits].
Deliver: implementation, concise motion map, actual verification, and tuning parameters.
```

You do not need to fill every field. The agent should infer context already available in the repository and state useful assumptions.

## Choose your motion intensity

Use one of these three prompts to communicate the result you want. Replace `[page, route, or project]` with your target; provide the project files or URL when needed. The prompts use Codex syntax. In Claude Code use `/web-motion-ultra`; in other agents invoke or select the skill as described in the [installation guide](installation.md).

Intensity controls how prominent, varied, and spatially expressive the choreography is. It does not mean making every animation faster or slower. These are creative targets, not guarantees of an identical result on every site.

| Level | Intended result | Typical treatment |
| --- | --- | --- |
| Low / restrained | Quiet polish that supports reading and actions | Small reveals, subtle feedback, mostly stable composition |
| Medium / balanced | Clearly animated, cohesive, and engaging | Orchestrated hero, varied section reveals, one signature moment |
| High / bold | Rich, expressive motion with a distinctive visual identity | Layered choreography, dramatic media reveals, narrative transitions |

### 1. Low intensity — subtle and refined

**Expected result:** a polished, calm page. Motion is noticeable in the details, while text and layout feel stable. Suitable for content-heavy sites, professional services, and interfaces where completing a task is the priority.

```text
Use $web-motion-ultra to enhance [page, route, or project].
Motion intensity: LOW / RESTRAINED.
Target result: subtle, elegant polish with a calm rhythm.

Preserve the existing content, structure, functionality, and visual identity.
Keep most of the composition still. Use small, short reveals on selected
headings or images, gentle link and button feedback, and smooth local
transitions for menus, tabs, or accordions that are already present.
Make the signature moment a discreet detail rather than a dramatic sequence.
Avoid decorative loops, narrative pinning, large movements, and parallax.
Keep body text stable and CTAs visible and usable immediately.

Give desktop and touch/mobile equally polished feedback, with stable hit areas.
Apply the reduced-motion alternative when the user's preference requests it;
low intensity is the creative direction, not forced reduced-motion mode.
Reuse the existing stack and avoid adding a library for simple effects.
Implement the changes, verify relevant states where tools are available,
and report actual checks plus the parameters that control intensity.
```

### 2. Medium intensity — balanced and engaging

**Expected result:** a page that visibly comes to life through a coordinated hero, differentiated section entrances, and satisfying interactions. Suitable for product landing pages, portfolios, and brand websites that need character while remaining easy to scan.

```text
Use $web-motion-ultra to enhance [page, route, or project].
Motion intensity: MEDIUM / BALANCED.
Target result: clearly animated, smooth, and engaging, with a coherent rhythm.

Preserve the existing content, structure, functionality, and visual identity.
Create one recognizable signature moment that fits the page's content and brand.
Orchestrate the hero with purposeful overlap between the heading, supporting
content, and main image, keeping the CTA available immediately.
Vary reveals by content type: headings, imagery, cards, and lists should have
related but distinct treatments, rather than the same fade-up everywhere.
Add refined feedback to existing buttons, cards, navigation, and disclosures.
Use restrained media parallax or scroll-linked progress only where it helps
tell the story. Leave pauses and stable reading areas between animated beats.

Design a deliberate touch/mobile version with the same visual character,
shorter travel where useful, native scrolling, and immediate tap feedback.
Use the reduced-motion alternative when the user's preference requests it.
Reuse the project's stack, implement the motion, and verify interruptions,
mobile layout, and relevant browser behavior where tools are available.
Report the motion map, actual checks, and parameters for tuning intensity.
```

### 3. High intensity — rich and expressive

**Expected result:** a distinctive, art-directed experience with a strong signature moment, layered sequences, and expressive transitions. Suitable for creative portfolios, campaigns, and immersive product stories. The choreography remains readable and responsive to input.

```text
Use $web-motion-ultra to enhance [page, route, or project].
Motion intensity: HIGH / BOLD.
Target result: rich, expressive, memorable animation with fluid continuity
across desktop and mobile. Make the motion visibly ambitious.

Preserve the existing content, information architecture, and functionality.
Develop a clear motion concept and a strong signature moment tied to the brand.
Create layered hero choreography with masked typography, expressive image
reveals, purposeful depth, and overlapping sequences where appropriate.
Connect sections through varied transitions and a recognizable motion motif.
Use media parallax, scroll-driven storytelling, shared-element transitions,
or a bounded pinned sequence when the content genuinely benefits from them;
select a coherent combination rather than adding every effect.
Give existing interactive elements distinctive, interruptible feedback.
Keep one visual lead at a time, deliberate pauses, readable body text,
and CTAs available immediately. Preserve native user control of scrolling.

Create a rich touch/mobile choreography too: retain the signature idea through
lighter masks, layered reveals, purposeful transitions, and tactile feedback.
Replace pointer-only effects rather than stripping mobile of its character.
Use the full intended choreography when no reduced-motion preference is set;
provide the complete reduced-motion alternative when the user requests it.
If performance suffers, reduce rendering cost and competing effects while
preserving the concept. Do not claim frame-rate results without measurement.
Reuse the stack, implement the changes, and verify rapid input, desktop/mobile,
resize, reduced motion, and representative performance where tools allow.
Report the motion map, actual checks, tradeoffs, and intensity controls.
```

For a new page, replace “enhance” and the preservation sentence with your creation brief, including audience, content, and primary action. To adjust a result, state what should change: for example, “keep the hero expressive, reduce background motion, and make card feedback quieter.”

## Photography portfolio

```text
Use $web-motion-ultra on this photography portfolio.
Keep the images and typography as the focus.
Use restrained masked image reveals and a coherent project transition.
Keep body text stable and navigation immediately usable.
Adapt the effect for touch and reduced motion.
```

## Product demo as the signature moment

```text
Use $web-motion-ultra to animate the product walkthrough section.
Explain the sequence through motion rather than animating every paragraph.
Keep the rest of the landing page quiet.
Use the existing stack; justify any additional dependency.
On mobile, preserve the story in a readable vertical flow.
```

## Smooth mobile refinement

```text
Use $web-motion-ultra to refine the mobile experience.
Inspect scroll stutter, browser-toolbar resize behavior, and tap feedback.
Keep native touch scrolling and stable hit areas.
Replace pointer-only effects with purposeful mobile interactions.
Check interrupted transitions and runtime reduced-motion changes.
Measure a representative interaction if browser tools are available.
```

## Interaction repair

```text
Use $web-motion-ultra to fix this menu and accordion.
Rapid open/close actions currently produce jumps and stale final states.
Make transitions interruptible and preserve keyboard focus and semantics.
Avoid changing the overall visual design.
```

## Concept first, with checkpoints

```text
Use $web-motion-ultra in checkpoint mode.
First inspect the homepage and propose a motion concept,
one signature moment, and section-level choices.
Wait for my approval before the motion map and implementation.
```

Without an explicit checkpoint request, an implementation task proceeds through the workflow without phase-by-phase permission questions.

## Audit only

```text
Use $web-motion-ultra to review this site's existing motion.
Do not edit code yet. Identify the most consequential problems
in choreography, interruption handling, mobile input, accessibility,
and rendering cost. Distinguish browser observations from code-only findings.
```

## What to expect

For implementation tasks, expect a concise concept, effect mapping, integrated changes, actual verification results, and the parameters that control intensity. A performance claim should include the environment and measurement context. When tools are unavailable, the agent should explain what remains unverified.

Intensity changes amplitude, density, and complexity. Requesting “bold” should not delay CTAs, disable reduced motion, or give up control of scrolling.
