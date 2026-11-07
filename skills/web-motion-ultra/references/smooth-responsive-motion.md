# Smooth, responsive motion

## Choreography: relationships, continuity, and rest

Organize motion into three layers: navigation/state, content/narrative, and atmosphere. Control feedback takes priority over decoration; a narrative sequence must not block an interaction. Limit competing visual leads and leave intervals of rest.

- Choose a brand-consistent motif: a recognizable direction, origin, mask, or spatial relationship. Repeat it with purposeful variations rather than giving every block a different effect merely for variety.
- Connect origin and destination. A card opening a detail view can preserve perceived position and proportions; use shared-element transitions or FLIP only when they clarify the relationship and the stack supports them. Provide a direct fallback.
- Use overlap to connect related elements and pauses to separate chapters. Do not accumulate stagger across every card in a long list: animate the visible group or cap the total delay.
- Keep text, controls, and edges intact at rest. Check masks, overflow, character descenders, and final scales; remove transient styles when no longer needed.
- Reading reveals normally happen once. Scrolling back must not hide content already read. Replays and reversible scrubbing are explicit narrative choices.
- Keep primary content readable on first render; do not sacrifice its appearance or loading for a theatrical entrance. Essential assets must not wait for the motion engine.

## Interruptible interactions

For menus, tabs, accordions, hover, drag, and transitions, consider idle, start, movement, interruption, and final state. Use only the states the component needs; do not build a global state machine for a simple transition.

1. The user's new intention wins immediately. Rapid clicks, pointer exit, Escape, and navigation must not wait for an animation to finish.
2. Where possible, continue from the current visual value or reverse the active transition. Do not reset transforms and cause jumps or queue obsolete animations.
3. Maintain one owner for each animated property; CSS, libraries, and custom loops must not compete over the same transform. Separate visual layers where necessary.
4. Update functional state consistently with the action. Stale completion callbacks must not reopen panels, move focus, or apply outdated states. Use cancellation or transition identifiers when needed.
5. Handle pointercancel, focus loss, and route exit. After a canceled drag, the control returns to a valid state and retains an alternative usable without dragging.

Choose spring response and damping according to purpose. A spring for drag or feedback may follow variable input well, whereas an editorial reveal may need predictable timing. Do not impose an exact duration on a physical spring. Avoid oscillation on long text and critical controls.

In custom loops, use elapsed time rather than fixed increments per frame. For exponential following, use alpha = 1 - exp(-dt / tau), with dt and tau in the same units; cap delta after suspension and stop the loop when the value converges. Prefer the existing engine when it already handles these details. Do not smooth both input and timeline without assessing perceived lag.

## Desktop, touch, and hybrid devices

Combine layout breakpoints with input capabilities such as hover and pointer. Do not infer device quality from width or user agent alone. A tablet may have a mouse and keyboard; a laptop may support touch. Consider the actual input used for each interaction when necessary.

| Aspect | Fine-pointer desktop | Touch/mobile | Reduced motion |
| --- | --- | --- | --- |
| Reveals | Masks and restrained translations | Same hierarchy, shorter distances and stagger | Final state or appropriate short fade |
| Cards and buttons | Hover and focus, local accent | Immediate tap feedback, stable hit area | Immediate state feedback |
| Tilt/magnetism | Only where it improves the experience | Replace with pressed feedback; do not emulate a cursor | Disabled |
| Pinned storytelling | Only with narrative value | Usually a readable vertical sequence | Content in normal flow |
| Gallery | Controls, keyboard, optional drag | Native scrolling and snap if suitable, alternative controls | Navigation without large transitions |
| Atmosphere | Light, pausable accent | Static or justified low-cost effect | Static |

The mobile version needs a complete visual intention: an image reveal, hero rhythm, or control feedback can retain the desktop character without copying its costs. Do not indiscriminately disable every animation.

- Keep native touch scrolling and inertia as the foundation. Do not globally intercept touchmove or wheel to create a “smooth” feeling. Configure touch-action only on components requiring a gesture, preserving relevant scrolling and zoom.
- Account for mobile browser chrome, virtual keyboards, safe areas, and orientation. Choose stable or dynamic viewport units according to the intended effect; do not rebuild a timeline for every tiny viewport-height change.
- Do not attach essential states to hover: menus must also open through tap and keyboard. Hit areas must not follow magnetic animations, and effects must not cover neighboring controls.
- When the profile changes, dispose of previous effects before recreating them; preserve application state, reading position, and focus.

## Fluidity budget and diagnosis

Define a page-appropriate budget before introducing expensive effects: extra assets, JavaScript work, animated surfaces, and concurrent effects. Reuse existing libraries; load advanced effects when needed without delaying content or controls.

At 60 Hz, a frame lasts about 16.7 ms; at 120 Hz, about 8.3 ms. This includes the browser's entire pipeline, not just animation code. Do not equate “uses transform” with “is smooth.”

Compare baseline and result over the same journey and environment. Record device/browser, input, viewport, and any applied throttling. Observe dropped frames, long tasks, layout/paint, input latency, and layout shifts. A Lighthouse score or isolated FPS counter does not certify motion quality.

| Symptom | Check | First correction |
| --- | --- | --- |
| Stuttering scroll | Layout/paint and scripts on the scroll path | Remove repeated measurements; reduce filters and surfaces |
| Lagging pointer follower | Stacked smoothing and UI-state rendering | One engine; keep per-frame data outside application renders |
| Jump on resize | Timeline resets, splitting, and competing refreshes | Batch measurements and rebuild only when necessary |
| Jump on repeated taps | Queued animations or reset initial values | Cancel/reverse and continue from the current state |
| Hot phone or continuous power use | Invisible loops, background media, and canvas | Suspend invisible work and reduce continuous rendering |
| Jump on returning to the tab | Huge elapsed-time delta or stale measurement | Resume with updated timing and measurements |

If cost remains excessive, degrade in this reasoned order: remove expensive blur/distortion, reduce concurrency and surfaces, limit canvas resolution, replace pinning/parallax with simple sequences, and finally use a static state. Preserve content and feedback. Do not implement an automatic device classifier for a project that does not need one. If adapting quality at runtime, use sustained measurements and hysteresis to avoid continuous visible changes.

## Acceptance before delivery

Check scenarios relevant to the work without building disproportionate test infrastructure:

- Rapidly open/close menus and accordions; switch tabs before transitions finish. No jumps, stuck states, or late callbacks.
- Scroll slowly, quickly, and backward; open a deep anchor. All content remains reachable and readable.
- Try mouse, keyboard, touch, zoom, landscape, and virtual keyboards when available. Distinguish real devices from emulation.
- Change reduced motion while an effect is active. Content reaches a valid state without residual pinning or styles.
- Repeat navigation and remounts. Listener, observer, and loop counts must not grow each cycle; focus and scrolling remain correct.
- Inspect first render, an intermediate frame, and the final state, as well as observing movement. Screenshots alone do not demonstrate fluidity.
- For a motion-heavy page, profile at least one representative desktop sequence and one mobile or emulated sequence. If tools or devices are unavailable, state the limitation and do not invent measured results.

A defect in readability, control access, input, or cleanup prevents an effect from being considered finished. Missing measurement tools require a stated limitation, not an invented guarantee. Report corrections made and only the remaining observable risks.
