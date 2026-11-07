# Contributing

Contributions grounded in real website work are especially useful: reproducible interaction failures, clearer decision rules, browser-specific findings, and improvements to installation or documentation.

## Propose a change

1. Open an issue for broad workflow changes, or send a pull request for a focused fix.
2. Describe the concrete problem and the behavior the change should produce.
3. Keep the skill entry point concise; place conditional details in the relevant reference.
4. Link new references from the entry point or another relevant reference.
5. Preserve the existing scope, accessibility requirements, and user authorization boundaries.

Avoid adding effects merely to expand the catalog, mandatory dependencies for simple work, universal rules derived from a single preference, or performance claims without measurement.

## Local validation

Python 3.10+ and PyYAML are contributor tools only:

```bash
python3 -m venv .venv
```

Activate the environment (`source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` on Windows), then run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

The checks validate skill metadata, packaged references, and local Markdown file links. They do not prove animation quality or browser compatibility.

## Behavioral verification

For changes affecting implementation decisions, exercise the skill on a small, isolated website fixture. Record the agent/client, stack, browser/device or emulation, task, and relevant result. Test interruptions and reduced motion when affected. Do not commit private project files, account information, or unlicensed assets.

For contributed demos, identify their author, source, license, and what was actually verified. Label illustrations and mockups as such. Keep generated website output separate from the installable skill.

## Pull requests

Explain the problem, resulting behavior, and validation. Add a changelog entry for user-visible changes. Contributions are accepted under the repository's MIT license; retain third-party attribution when applicable.
