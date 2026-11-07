# Effect selection

Choose according to content, objective, and device capabilities. The signature moment can be subtle; not every site needs pinning, parallax, or a cinematic hero.

## Motion character

| Character | Useful language | Keep in check |
| --- | --- | --- |
| Editorial, elegant | Masked headings, spacious imagery, pauses | Word-by-word stagger on long text |
| Playful, energetic | Local spring feedback, responsive cards, rhythmic accents | Repeated bounce and many simultaneous animations |
| Technical, precise | Alignment, progress, short state transitions | Effects that hide data or delay operations |
| Calm, organic | Fades, minimal translation, soft changes | Continuous loops in the reading area |
| Cinematic | One narrative sequence of media and masks | Forced scrolling, artificial waits, heavy media |

## Hero and text

- **Orchestrated entrance:** heading, subtitle, and image with small overlaps. The CTA remains immediately visible and reachable. On mobile, reduce distance and total duration; with reduced motion, show the final composition.
- **Line-mask reveal:** useful for short headings; account for fonts, accents, descenders, and wrapping. Do not split paragraphs or links by habit.
- **Scrubbed text color:** useful for pacing a narrative sentence. Even the least emphasized state must retain readable contrast; use the final color for reduced motion.
- **Counters:** use real, meaningful data with the final value already in HTML. Do not continuously announce decorative updates; no `aria-live` on the count.
- **Marquee:** for secondary sequences, never the only access to information. Exclude decorative duplicates from the accessibility tree, prevent focusable duplicates, and provide a pause control and static version.

## Media and backgrounds

- **Clip-path or gentle zoom:** reveal images without changing layout; check rendering cost and clipping. Show complete media for reduced motion.
- **Parallax:** only on media or decoration, with limited amplitude and sufficient container space; never on text. Disable it when it impairs reading or on unsuitable devices.
- **In-viewport video:** reserve dimensions, use a poster, handle rejected `play()` calls, and stop offscreen playback. Autoplay must not introduce unexpected audio. For reduced motion, use a poster or user-initiated playback. Provide controls for persistent moving content.
- **Gradients, SVG blobs, and grain:** local visual accents. A static image can add depth without looping; animated gradients and filters may require expensive repaints.
- **Canvas/WebGL:** only with a clear visual role, compatible budget, and static fallback. Stop rendering when the content is not visible.

## Scrolling and navigation

- **Progress bar:** useful for long reading or a narrative journey; do not simulate loading. Use a static state or update without spatial animation where necessary.
- **Pinned section:** only for a story that benefits from guided progress; limit its length. On mobile and with reduced motion, stack content in its original order without empty pin spacing.
- **Horizontal gallery:** can illustrate a journey; preserve touch and keyboard alternatives and access to every item without trapping the wheel.
- **Background changes between sections:** useful for chapters; verify text, link, and header contrast throughout the transition.
- **Compact or hidden header:** must not disappear while it contains focus. Handle reappearance, anchors, and space for sticky headings.
- **Smooth scrolling:** add only when requested or useful to the concept. Preserve shortcuts, anchors, back/forward, and scroll restoration. Do not use it with reduced motion.
- **Page transitions:** use View Transitions after feature detection, preserving normal navigation when unavailable. An overlay is optional; failures must not block navigation or trap focus.

## Controls and feedback

- **Card lift, spotlight, or tilt:** highlight actual interactivity rather than making static cards look clickable. Tilt and spotlight track only fine pointers; provide equivalent focus and pressed-state feedback.
- **Magnetic button:** move a visual layer without unpredictably moving the hit area or focus position. Disable on touch and with reduced motion.
- **Custom cursor:** a rare choice for expressive projects, fine pointers only. Retain a working pointer if the script fails and do not obscure text or controls.
- **Underlines and icons:** brief hover, focus-visible, and active feedback without layout changes.
- **Fullscreen menu:** brief choreography, semantically correct open/closed states, Escape dismissal, and restored focus. If modal, manage focus and background content as for a dialog.
- **Accordions and tabs:** prioritize semantics, focus, and state. Moving indicators and panel transitions follow the control; never wait for animation to update `aria-expanded` or selection.
- **Forms:** timely validation, submission, and success feedback. Communicate states through accessible text too; animation does not replace the message.

## Concept examples

These illustrate reasoning, not templates to apply to every page.

- **Photography portfolio:** “Images arrive like uncovered prints, while text remains stable to give the work room.” Signature: main-project reveal. Support: gentle image transitions and link underlines.
- **Technical product landing page:** “Motion demonstrates how the product simplifies a task.” Signature: a guided demo in one section. Support: control feedback and feature progression, without animating every text block.
- **Wellness studio:** “Sections unfold at a calm pace, with information and booking immediately available.” Signature: a restrained image reveal. Support: service accordions and local transitions without loops.
