---
name: web-motion-ultra
description: Design, implement, and refine smooth desktop and mobile animations and tailored motion for new or existing web pages and websites. Use when asked to make a page feel less static, animate a landing page, or add brand-consistent microinteractions, reveals, parallax, and scroll choreography. Does not cover video production or merely adding backend-driven dynamic content.
---

# Web Motion Ultra

Transform a static page into a living experience through the craft of a creative developer and motion designer. Every movement should guide attention, communicate state, establish hierarchy, or express the brand. Choreograph motion around the content rather than applying identical effects everywhere.

## Context and scope

Infer the mode, objective, audience, affected pages, motion character, intensity, and stack from the project and request. Do not ask a questionnaire when this information is already available. Briefly state useful assumptions; ask only for information that prevents progress.

- **Enhance, the default for an existing site:** preserve copy, section order, visual identity, functionality, and information architecture. Add only wrappers, attributes, and local changes needed for motion. Do not turn the request into a redesign.
- **Create:** when a new page is requested, design layout and movement together, using layers, scale contrast, and hierarchy that remains legible at rest.
- If no page, URL, or code is available, define a preliminary concept and request the material needed to apply it. Do not invent the user's site or claim changes that were never made.
- For a URL, use available reading or browser tools. A screenshot alone cannot verify interactions and scrolling.

Respect the existing stack and dependencies. For a new page without constraints, start with HTML, CSS, and vanilla JavaScript. Use CSS and IntersectionObserver for simple effects; GSAP with ScrollTrigger for complex sequences, pinning, and scrubbing; Motion/Framer Motion when already used in React or requested. Lenis is optional and must serve the project, not be a prerequisite. Before adding libraries, verify APIs and versions in official documentation. Use the existing package manager or pinned CDN versions, never `latest`.

## Built-in motion intensity profiles

A skill invocation plus one line is a complete motion-enhancement request when a target project or page is available:

```text
Motion intensity: LOW
Motion intensity: MEDIUM
Motion intensity: HIGH
```

Select one value, case-insensitively. Apply the corresponding profile below without asking the user to repeat its effect choices, mobile requirements, preservation rules, or QA instructions. Infer the target from the active project and established conversation scope; ask for the target only when missing or ambiguous. For an existing page, implement the selected profile through the full workflow unless the user requested only planning or review. Do not merely describe the preset.

An explicit intensity overrides contextual intensity defaults. Treat restrained/subtle as LOW, balanced as MEDIUM, and bold/expressive as HIGH when used as intensity labels. If no intensity is specified, infer it using the concept guidance below. Additional user constraints refine the profile and take precedence over its creative defaults. When changing intensity on an already animated page, retune the existing system instead of stacking another animation layer.

### LOW — subtle and refined

Target: calm, elegant polish with stable composition and unobtrusive motion.

- Keep most of the page still. Apply short, small reveals to selected headings or images, gentle button/link feedback, and smooth local transitions on existing menus, tabs, and accordions.
- Make the signature moment a discreet detail. Avoid decorative loops, narrative pinning, large displacements, and parallax by default.
- Use compact timing, minimal stagger, and small travel (roughly 4–12 px where translation is appropriate); do not animate every reading block.
- Keep body text stable and primary actions immediately visible and usable.
- On mobile, retain polished tap and disclosure feedback with stable hit areas. LOW is a creative intensity, not forced reduced-motion mode.
- Prefer native CSS/browser effects and existing dependencies; do not add a library for simple polish.

### MEDIUM — balanced and engaging

Target: visibly animated, cohesive motion with a clear rhythm and one recognizable signature moment.

- Orchestrate the hero with purposeful overlap between heading, supporting content, and main imagery; keep the CTA available immediately.
- Give headings, images, cards, and lists related but distinct reveals. Avoid identical fade-ups across every section.
- Refine feedback for existing navigation, buttons, cards, and disclosures. Use measured travel, shared easing, and bounded stagger.
- Add restrained media parallax or scroll-linked progress only where it helps explain the story. Leave pauses and stable reading areas between beats.
- On touch/mobile, preserve the concept with shorter travel where useful, native scrolling, and immediate tap feedback; replace pointer-only treatments.
- Reuse the stack and introduce a choreography library only when the selected effects justify it.

### HIGH — rich and expressive

Target: an ambitious, art-directed experience with rich animation, layered sequences, and fluid continuity on desktop and mobile. HIGH must produce a visibly more expressive treatment than MEDIUM, not merely longer durations.

- Create a strong brand-specific signature moment and layered hero choreography. Consider masked typography, expressive image reveals, depth, and overlapping sequences according to the content.
- Connect sections through varied transitions and a recognizable motion motif. Select a coherent combination of media parallax, scroll-driven storytelling, shared-element transitions, or a bounded pinned sequence when useful; do not use every effect by default.
- Use greater visual amplitude and compositional depth where appropriate, with controlled timing and deliberate pauses. Maintain one visual lead at a time, readable body text, and immediately available CTAs.
- Give existing interactive elements distinctive, interruptible feedback. Preserve native control of scrolling and semantic navigation.
- Create a rich mobile interpretation too: retain the signature idea through lighter masks, layered reveals, purposeful transitions, and tactile feedback. Replace pointer-only effects; do not silently reduce HIGH to LOW simply because the viewport is narrow.
- If performance suffers, remove expensive rendering and competing effects first, then simplify while preserving the concept. Explain material compromises rather than promising unmeasured frame rates.

### Shared behavior for every profile

Preserve existing content, information architecture, functionality, and visual identity in enhancement mode. In creation mode, design layout and motion together within the requested brief. Always adapt to desktop and touch, handle interruptions and cleanup, and run relevant verification where tools are available.

Apply the full selected profile when the user has no reduced-motion preference. Respect `prefers-reduced-motion: reduce` or an explicit user request for reduced motion with a complete, readable alternative; do not force that preference merely because LOW is selected or the device is mobile. HIGH does not override an actual accessibility preference.

Use the profile to choose amplitude, effect density, and complexity; the token values below are starting points, not a cap that flattens the differences between profiles. Report the selected level and the actual implementation and checks concisely, without asking the user to restate this specification.

## Ultra quality standard

Interpret “Ultra” as precise choreography, continuous interactions, and verified desktop and mobile quality. It does not automatically increase intensity, effect count, or dependencies.

Before making changes, observe the page and identify concrete problems: static hierarchy, missing feedback, inconsistent timing, jumps, heavy scrolling, or effects incompatible with touch. If motion already exists, record a baseline and improve the existing system. Keep analysis and documentation proportional to local changes.

For every implementation, read [references/smooth-responsive-motion.md](references/smooth-responsive-motion.md): it defines choreography, interruptions, input profiles, performance, and acceptance criteria. Consult the effect catalog to choose the visual language; quality also depends on what happens between states.

## 1. Concept

Examine structure, content, the primary action, and existing interactions. Define:

- A **motion concept** in one sentence describing behavior, not just aesthetic adjectives.
- A **signature moment** for the page or journey: its most memorable effect, with a narrative or practical purpose. In operational interfaces, this may be a subtle microinteraction.
- Supporting effects for each section, explaining what they help users understand or do.
- Character and intensity: restrained for operational interfaces and reading; medium as a starting assumption for promotional landing pages; bold only when consistent with the request. Intensity changes amplitude, density, and complexity, not just speed.

One visual lead at a time. Vary the treatment of headings, images, lists, and controls while sharing the same tokens. Use sequences, overlaps, and pauses; large elements may take longer than small ones. Do not delay CTA availability or impose a preloader to simulate quality.

To select effects, read [references/effect-selection.md](references/effect-selection.md). It is a selective repertoire, not a checklist to complete. A site can feel alive through responsive interactions without perpetual animations.

## 2. System and motion map

Centralize durations, easing, distances, and stagger in CSS tokens and JavaScript configuration. Adapt these starting values:

| Token | Starting value | Use |
| --- | --- | --- |
| micro | 150–250 ms | Control and link feedback |
| standard | 400–700 ms | Reveals and local transitions |
| hero | 800–1200 ms | Nonblocking main sequence |
| ease-out | cubic-bezier(0.16, 1, 0.3, 1) | Soft arrivals |
| ease-in-out | cubic-bezier(0.65, 0, 0.35, 1) | State transitions |
| stagger | 60–120 ms | Rhythm between related elements |
| distance | 16–48 px | Restrained displacement, reduced on mobile |

Use equivalent easing when a library expects a different format: do not pass a CSS string to an API that does not accept it. `linear` suits continuous loops, scroll-linked progress, and constant-speed movement. Avoid pervasive bounce and elastic easing. Limit the total duration of long staggered sequences as well as individual animations.

Prepare a motion map proportional to the work:

| Section/element | Purpose | Trigger | Effect/properties | Duration or scroll range | Easing | Delay/stagger | Mobile/touch | Reduced motion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

For interactive effects, also specify interruption, reversal, repeated-input behavior, and the final resting state. Define separate desktop and touch profiles with the same visual intent; screen width alone does not determine input or device performance.

For scrubbing, describe the scroll range and any smoothing instead of inventing a fixed temporal duration. Give each effect a reduced version or a complete static state.

## 3. Implementation

When code changes are requested, proceed from concept to implementation in the same task. Phases organize the work and do not require intermediate approvals. Stop between phases only when the user explicitly requests checkpoints; present the concrete phase result before asking to continue. If only a concept or motion map is requested, respect that scope.

Read [references/implementation-and-qa.md](references/implementation-and-qa.md) for initialization, accessibility, cleanup, and practical checks. Apply these constraints:

- Essential content and actions remain visible and usable without JavaScript, with missing dependencies, and after initialization errors. An early `.js` class alone does not guarantee this.
- Prefer `transform` and `opacity`; assess clip-path, filters, gradients, and large surfaces carefully. Do not promise 60 fps without measurements. Avoid alternating layout reads and writes.
- For accordions and other necessary size changes, choose a semantic, measured solution. Do not distort text with `scaleY` just to obey an absolute ban on `height`.
- Reserve media space and preserve existing transforms through wrappers or composition. Do not introduce layout shifts or accidental horizontal overflow.
- Preserve native scrolling, anchors, history, keyboard access, focus, and zoom. No scroll-jacking; smooth scrolling and pinning must retain user control.
- Adapt parallax and expensive graphics to touch/mobile capabilities while preserving the selected profile's visual intent. Replace pointer-only tilt and custom cursors with suitable touch feedback. Actions must not depend on hover.
- With `prefers-reduced-motion: reduce`, remove large displacement, parallax, spatial scrubbing, narrative pinning, and nonessential loops. Use immediate states or short fades where appropriate. Also respect preference changes during the session.
- No intentional flashing. For content moving automatically for more than five seconds alongside other content, provide pause/stop/hide or make it static. Reduced-motion support alone does not replace that control.
- Preserve semantics when splitting text into words or lines. Do not hide interactive elements or ancestors of focusable controls from screen readers.

For vanilla projects, use `motion.css` and `motion.js` when helpful. In frameworks, follow existing modules, components, and lifecycle conventions. Expose central configuration for intensity, timing, distances, stagger, and optional features; do not add toggles for unimplemented effects.

Use declarative attributes when they simplify reuse, such as `data-reveal="mask"`, `data-stagger="80"` (ms), and `data-parallax="0.15"` (factor). Define the units and meaning of supported attributes. Do not build a generic engine when a local CSS transition suffices.

Separate initializers such as `initHero`, `initReveals`, and `initParallax` only for effects actually present. Every initialization must be disposable; avoid duplicate observers, listeners, tickers, and triggers after navigation or remount. In React, use lifecycle and cleanup without directly modifying React-managed DOM to split text.

Deliver complete code integrated into project files when you have access. Do not merely paste snippets and leave implementation unfinished. Do not publish or deploy the site unless requested.

## 4. Verification and delivery

When a browser is available, verify initial and final animation states, mobile, touch/keyboard, resize, reduced motion, disabled JavaScript, and dependency failures. Run relevant project checks. Profile a representative interaction for expensive effects.

Before delivery, apply the acceptance criteria in the smooth-motion reference. If an effect struggles, first reduce rendering cost and concurrency, then amplitude or complexity; slowing it down does not fix dropped frames. Correct observed problems and run a targeted recheck.

Report what was actually verified and what remains unverified. Do not confuse code review with browser testing. Correct observed issues before concluding.

Scale the delivery to the request and include:

- Concept, signature moment, and concise motion map.
- Implemented changes and file links; complete code per file only if you cannot edit files directly.
- QA results, tradeoffs, and relevant remaining assumptions.
- Concrete parameters for making the result more restrained or more intense.

Do not repeat empty sections or approval questions for every phase.
