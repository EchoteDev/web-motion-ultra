# Prompt cookbook

Use these starting points with your own project context. They are example requests, not claims about completed demos.

## A useful brief

```text
Use $web-motion-ultra.
Mode: enhance an existing site / create a new page.
Project: [product, audience, and primary action].
Scope: [routes or sections].
Motion character: [editorial, playful, precise, calm, cinematic].
Motion intensity: [LOW, MEDIUM, HIGH].
Stack: [existing framework and animation dependencies].
Constraints: [content to preserve, device priorities, performance limits].
Deliver: implementation, concise motion map, actual verification, and tuning parameters.
```

You do not need to fill every field. The agent should infer context already available in the repository and state useful assumptions.

## Choose your motion intensity

Invoke the skill and select **one** built-in profile. The skill already contains the effect direction, mobile adaptation, accessibility behavior, and implementation/verification instructions. No long brief is needed when your project or target page is already available.

### 1. Low intensity — subtle and refined

Small reveals, gentle feedback, and mostly stable composition.

```text
$web-motion-ultra
Motion intensity: LOW
```

### 2. Medium intensity — balanced and engaging

An orchestrated hero, varied reveals, and one recognizable signature moment.

```text
$web-motion-ultra
Motion intensity: MEDIUM
```

### 3. High intensity — rich and expressive

Rich, layered choreography, expressive transitions, and a strong signature moment on desktop and mobile.

```text
$web-motion-ultra
Motion intensity: HIGH
```

In Claude Code, replace `$web-motion-ultra` with `/web-motion-ultra`. In other agents, select or invoke the skill as described in the [installation guide](installation.md), then send only the `Motion intensity:` line.

Choose one level per request. The skill infers the target from your active project and conversation; specify a page or route only when needed. You can add optional constraints such as “home page only” or “keep the hero unchanged.” For a new page, provide the creation brief too. LOW is not forced reduced motion; all three profiles respect the user's actual accessibility preference.

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
