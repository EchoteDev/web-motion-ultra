# Implementation and QA

## Progressive enhancement and initialization

Base HTML already contains readable content, final values, and functioning actions. Do not apply `opacity: 0` globally through a `.js` class: a failed bundle or CDN could leave content hidden. A `noscript` block helps only when JavaScript is disabled, not when it fails.

Choose one of these strategies according to the stack:

- Start Web Animations API animations on visible elements without persistent hidden initial styles; return to base styling on completion or cancellation.
- With a library, apply initial states only to elements already controlled by their initializer. Register cleanup and restoration first; if initialization fails, remove temporary states and show the content.
- With local CSS classes, activate a prepared state only after registering the trigger, and restore visibility on errors and focus. Avoid hiding the whole page in the head.

Do not leave a CTA invisible but keyboard-focusable. If focus enters an element being revealed, make it visible immediately without waiting for scroll triggers or delays. Also check mid-page loading, anchors, and backward navigation.

Wait for `document.fonts.ready` before font-dependent measurement and splitting, without blocking page readability. If the project loads fonts dynamically, handle their actual lifecycle. Recompute splits and measurements when width changes, avoiding observers triggered by their own modifications.

Declare dimensions or aspect ratios for images and video. Update trigger and pin measurements after actual layout changes and media/font loading; do not refresh every frame.

## Performance and properties

- Prefer `transform` and `opacity` without assuming they always guarantee cheap compositing. Avoid large filtered surfaces and excessive layers.
- Batch layout reads and writes. Use IntersectionObserver for simple entrances, requestAnimationFrame for necessary loops, and passive listeners when event cancellation is unnecessary.
- Do not keep requestAnimationFrame running for completed effects; suspend offscreen work and work in hidden documents.
- Apply `will-change` only to elements and periods that benefit from it, removing it after the effect.
- If entrance, parallax, and hover affect the same object, separate layers or compose transforms so one effect does not erase another.
- Size changes may be necessary for panels and accordions. Prefer native mechanisms or a contained transition, measure costs, and avoid arbitrary `max-height` values that clip content or distort timing.
- With CSS scroll-driven animations, use feature detection and a readable static fallback. Do not also run the JavaScript fallback simultaneously.

## Lifecycle and libraries

- Idempotent initialization: a second mount does not duplicate events, observers, or animations.
- Cleanup: cancel animations, requestAnimationFrame, timeouts, observers, and listeners; restore temporary styles and text splits, and remove pinning and spacers.
- With GSAP, use scope/context and matchMedia when supported by the project version. Create and remove triggers within their desktop, mobile, and reduced-motion conditions. Avoid global cleanup that destroys effects elsewhere on the site.
- If Lenis is genuinely needed, use one update cycle, integrate ScrollTrigger according to the adopted version's documentation, and dispose of both correctly. Do not add a second ticker by habit.
- In React, keep content in declarative rendering and use scoped references. Verify setup/cleanup through remounts and Strict Mode; do not directly split React-managed DOM.
- In SPAs, verify route entry/exit, scroll restoration, and focus. A visual transition does not justify breaking links, history, or direct page loading.

## Text and motion accessibility

- For reduced motion, show the final result immediately and preserve all content. Remove pins/spacers and turn horizontal narratives into normal reading order. Retain only useful brief feedback without problematic displacement.
- Observe `matchMedia('(prefers-reduced-motion: reduce)')` for runtime changes too; CSS and JavaScript must agree on state. Do not leave inline transforms or opacity overriding the CSS fallback.
- For a simple split heading, keep one accessible text copy and make the split visual copy decorative. If using `aria-label`, verify that the role supports it and that it conveys the complete text without duplication. Do not indiscriminately replace paragraph, emphasis, and link semantics with labels.
- Do not apply `aria-hidden` to focusable elements or their ancestors. Decorative copies must contain no interactive controls.
- A pause control must be keyboard-accessible, have an understandable name and state, and actually stop all loops within its scope. Hover-only pausing is insufficient.
- Maintain contrast during reveals, background transitions, and progressive text highlighting. Do not communicate information solely through color or motion.
- Check zoom and reflow, focus-visible, Escape dismissal for overlays, and focus restoration after closing.

Sources to consult for deeper guidance or current behavior:

- [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
- [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- [MDN: aria-hidden](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden)

## Practical checks

Select checks relevant to implemented effects and record tooling limitations.

| Scenario | What to verify |
| --- | --- |
| Desktop, initial load | Coherent sequence, immediately available CTA, no lost content |
| Full scroll and return | Stable triggers, readable final state, no orphaned pins or blank spaces |
| Narrow mobile and orientation | No accidental overflow, clipped text, or hover-only functions |
| Keyboard and touch | Visible focus, correct order, reachable links and controls |
| Initial and runtime reduced motion | Loops/displacement stop, complete content, pin cleanup |
| Disabled JavaScript | Essential content readable and base actions available |
| Blocked motion dependency | Content still visible, working navigation, no permanent overlay |
| Resize and late fonts/media | Correct splitting, updated measurements, no obvious jumps |
| Anchors, back/forward, route remount | Sensible position and focus, no duplicate triggers |
| Loops and autoplay | Usable pause, offscreen suspension, no unexpected audio |
| Performance profile when needed | Expensive layout/paint, dropped frames, and shifts observed and corrected |

Screen dimensions alone do not simulate touch input; reading a media query does not verify reduced motion. Exercise these states when the browser permits, distinguishing actual tests from expectations.

Conclude with completed checks, remaining limitations, and actual tuning parameters. Do not claim full compliance, absence of layout shifts, or 60 fps without the corresponding verification.
