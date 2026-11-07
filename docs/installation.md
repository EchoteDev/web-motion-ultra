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
2. Download the `web-motion-ultra-v1.1.0.zip` skill asset, or the corresponding asset for a newer release.
3. Extract it. The archive contains a `web-motion-ultra` folder with `SKILL.md`, `agents`, and `references` inside.
4. Move that whole folder into your chosen skills directory.

GitHub's **Code → Download ZIP** downloads the entire repository instead. In that archive, install only `skills/web-motion-ultra`.

## Claude Code

Clone this repository once and enter the clone before running the commands below:

```bash
git clone https://github.com/EchoteDev/web-motion-ultra.git
cd web-motion-ultra
```

For a personal skill available across local projects (macOS/Linux):

```bash
mkdir -p "$HOME/.claude/skills"
cp -R skills/web-motion-ultra "$HOME/.claude/skills/"
```

For a project-only skill, copy the folder into `<your-website-project>/.claude/skills/web-motion-ultra/` instead. Invoke it in Claude Code:

```text
/web-motion-ultra Improve this website with smooth desktop and mobile animations.
```

See [Claude Code skill documentation](https://code.claude.com/docs/en/skills). These personal paths describe local Claude Code sessions; account-synced/cloud sessions have separate loading rules.

## Google Antigravity

From the repository clone, install a global skill (macOS/Linux):

```bash
mkdir -p "$HOME/.gemini/config/skills"
cp -R skills/web-motion-ultra "$HOME/.gemini/config/skills/"
```

For a workspace skill, copy it into `<your-website-project>/.agents/skills/web-motion-ultra/`. Current Antigravity documentation uses `.agents/skills`; `.agent/skills` is a legacy compatibility path. App, CLI, and standalone IDE share the global location above.

Ask the agent:

```text
Use the web-motion-ultra skill to improve this website's desktop and mobile motion.
```

The App and interactive CLI also support `/web-motion-ultra`. If adding a skill to a running CLI, use `/skills reload` or start a new conversation. In the standalone IDE, inspect discovered skills in the Customizations menu. See [Antigravity skill documentation](https://antigravity.google/docs/skills).

## Cursor

From the repository clone, install a personal skill (macOS/Linux):

```bash
mkdir -p "$HOME/.cursor/skills"
cp -R skills/web-motion-ultra "$HOME/.cursor/skills/"
```

For a project skill, copy it into `<your-website-project>/.cursor/skills/web-motion-ultra/`. Cursor also supports `.agents/skills` project directories and `~/.agents/skills` personal directories; choose one active location rather than duplicating the skill.

In Agent chat, type `/` and select `web-motion-ultra`, then describe the task. Local personal skills are not automatically available to every remote/cloud execution environment; use a project skill or follow Cursor's documented sync setup. See [Cursor skill documentation](https://cursor.com/docs/skills).

## GitHub Copilot

For a repository-scoped skill, copy the folder into:

```text
<your-website-project>/.github/skills/web-motion-ultra/
```

For example, from your website project root (macOS/Linux):

```bash
mkdir -p .github/skills
cp -R /path/to/web-motion-ultra/skills/web-motion-ultra .github/skills/
```

Replace `/path/to/web-motion-ultra` with the actual clone location. Commit the project skill if it should be available to repository-based Copilot workflows.

For a personal local skill, from the downloaded repository clone:

```bash
mkdir -p "$HOME/.copilot/skills"
cp -R skills/web-motion-ultra "$HOME/.copilot/skills/"
```

In a supported Copilot agent experience, ask:

```text
Use the web-motion-ultra skill to add purposeful, smooth animations to this website.
```

Copilot loads relevant skills based on their descriptions. Skill support is documented for Copilot cloud agent, code review, CLI, app, and agent mode in VS Code; the ability to implement and browser-test a site depends on the selected experience. See [GitHub Copilot skill documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Windows PowerShell: additional agents

From the downloaded repository clone, choose **one** destination for your agent:

| Agent | Personal destination | Project destination |
| --- | --- | --- |
| Claude Code | `$HOME/.claude/skills` | `<project>/.claude/skills` |
| Antigravity | `$HOME/.gemini/config/skills` | `<project>/.agents/skills` |
| Cursor | `$HOME/.cursor/skills` | `<project>/.cursor/skills` |
| Copilot | `$HOME/.copilot/skills` | `<project>/.github/skills` |

Set `$skillParent` to that location. This example installs for Claude Code:

```powershell
$skillParent = Join-Path $HOME '.claude/skills'
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
if (Test-Path (Join-Path $skillParent 'web-motion-ultra')) {
    throw 'Skill already exists. Follow the update instructions instead.'
}
Copy-Item -Recurse './skills/web-motion-ultra' $skillParent
```

Before any macOS/Linux copy above, confirm the destination's `web-motion-ultra` folder does not exist. If it does, follow the update procedure instead. Copy the complete folder so linked references remain available. `SKILL.md` must sit directly inside `web-motion-ultra`, without an extra nested copy.

## Other coding agents

The Markdown instructions can be adapted to other coding agents that support skills. Consult that agent's current documentation for its discovery directory and invocation syntax. Copy the complete skill folder, including references. Do not assume Codex's `$` invocation syntax or `agents/openai.yaml` metadata is interpreted by every client.

If your client has no skill loader, ask it to read `skills/web-motion-ultra/SKILL.md` and the linked references before working on the website. This is a manual workflow, not a claim of native integration.

## Update

1. Back up any local customizations to your installed skill.
2. In your downloaded repository, run `git pull --ff-only` and review [CHANGELOG.md](../CHANGELOG.md).
3. Move the old installed folder to a backup location **outside skill-discovery directories**.
4. Copy the new `skills/web-motion-ultra` folder into the same installation location.
5. Invoke or select the skill using your agent's syntax above; refresh discovery or restart the agent if needed.

For reproducible installs, use a release tag rather than `main`: clone with `git clone --branch v1.1.0 --depth 1 https://github.com/EchoteDev/web-motion-ultra.git`. Check out newer release tags explicitly when updating a tag-based clone.

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
