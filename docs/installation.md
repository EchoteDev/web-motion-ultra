# Installation, updates, and removal

## Requirements

- A coding agent that can read skill instructions and edit your website project.
- Git for the clone-based methods, or a ZIP extractor for the download method.
- Browser tooling if you want actual interaction and performance verification.

End users do not need Python, Node.js, or a package install to read and install this instruction-only skill. Your website may have its own development dependencies. Python and PyYAML are used only by this repository's contributor validation command.

## Codex: built-in installer

In Codex, enter:

```text
$skill-installer install the skill from https://github.com/EchoteDev/web-motion-ultra/tree/main/skills/web-motion-ultra
```

Then invoke `$web-motion-ultra` with your task. If the skill is missing from discovery, restart Codex. The installer manages its own destination; do not also install a second manual copy with the same name.

## Codex: manual personal installation

Current official documentation lists `~/.agents/skills` for personal skills and `.agents/skills` in a repository for project skills. See [Build skills](https://learn.chatgpt.com/docs/build-skills) for current discovery rules.

### macOS / Linux

Run from the parent folder where you want to keep the downloaded repository:

```bash
git clone https://github.com/EchoteDev/web-motion-ultra.git
mkdir -p "$HOME/.agents/skills"
cp -R web-motion-ultra/skills/web-motion-ultra "$HOME/.agents/skills/"
```

Before copying, check that `~/.agents/skills/web-motion-ultra` does not already exist. For an existing installation, use the update procedure below.

### Windows PowerShell

```powershell
git clone https://github.com/EchoteDev/web-motion-ultra.git
$skillParent = Join-Path $HOME '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
if (Test-Path (Join-Path $skillParent 'web-motion-ultra')) {
    throw 'Skill already exists. Follow the update instructions instead.'
}
Copy-Item -Recurse './web-motion-ultra/skills/web-motion-ultra' $skillParent
```

## Project-only installation

Download or clone this repository outside your website project first. From the website project root:

```bash
mkdir -p .agents/skills
cp -R /path/to/web-motion-ultra/skills/web-motion-ultra .agents/skills/
```

Replace `/path/to/web-motion-ultra` with the clone's actual location. Ensure the destination does not already exist. The resulting entry point must be `.agents/skills/web-motion-ultra/SKILL.md`, not an extra nested copy.

You can commit this project-scoped skill folder to share it with your team.

## Download without Git

1. Open [Releases](https://github.com/EchoteDev/web-motion-ultra/releases).
2. Download the `web-motion-ultra-v1.0.0.zip` skill asset for the initial release, or the corresponding asset for a newer release.
3. Extract it. The archive contains a `web-motion-ultra` folder with `SKILL.md`, `agents`, and `references` inside.
4. Move that whole folder into your chosen skills directory.

GitHub's **Code → Download ZIP** downloads the entire repository instead. In that archive, install only `skills/web-motion-ultra`.

## Other coding agents

The Markdown instructions can be adapted to other coding agents that support skills. Consult that agent's current documentation for its discovery directory and invocation syntax. Copy the complete skill folder, including references. Do not assume Codex's `$` invocation syntax or `agents/openai.yaml` metadata is interpreted by every client.

If your client has no skill loader, ask it to read `skills/web-motion-ultra/SKILL.md` and the linked references before working on the website. This is a manual workflow, not a claim of native integration.

## Update

1. Back up any local customizations to your installed skill.
2. In your downloaded repository, run `git pull --ff-only` and review [CHANGELOG.md](../CHANGELOG.md).
3. Move the old installed folder to a backup location **outside skill-discovery directories**.
4. Copy the new `skills/web-motion-ultra` folder into the same installation location.
5. Invoke `$web-motion-ultra` again; restart Codex if discovery has not refreshed.

For reproducible installs, use a release tag rather than `main`: clone with `git clone --branch v1.0.0 --depth 1 https://github.com/EchoteDev/web-motion-ultra.git`. Check out newer release tags explicitly when updating a tag-based clone.

## Remove

Move or delete only the installed `web-motion-ultra` folder from your skills directory. This removes the instructions from discovery; it does not undo website changes made while using the skill.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Skill not visible | Confirm the discovery path and folder name; ensure `SKILL.md` is directly inside; restart the agent if needed |
| Duplicate entries | Keep one active installation per intended scope; move backups outside discovery directories |
| Agent gives generic advice | Invoke the skill explicitly, provide the website project, and ask for implementation |
| No browser testing performed | Confirm browser tools are available; ask the agent to report actual checks and limitations |
| Unexpected framework changes | Specify the existing stack and enhancement scope; the skill defaults to preserving both |
