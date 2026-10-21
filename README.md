<!-- living-code-readme:1 -->
# ✳️ Living Code for Claude Code

**Calm slate. Living color.** Living Code for Claude Code: prompt accents, permissions, messages, diffs and subagent colors in four native custom themes.

[Installation](#installation) · [Flavors](#flavors) · [Configuration](#configuration) · [All ports](https://github.com/living-code-theme)

## Previews

Real application screenshots have not been captured yet.

## Installation

```sh
git clone https://github.com/living-code-theme/claude-code.git
cd claude-code
```

Install in a version of Claude Code whose `/theme` menu includes **New custom theme…**. Copy the JSON files into the personal theme directory:

```sh
mkdir -p "$HOME/.claude/themes"
cp themes/*.json "$HOME/.claude/themes/"
```

Restart Claude Code once if that directory did not exist when it started. Run `/theme` and select **Living Code Night**. Later changes hot-reload.

## Flavors

Expand a flavor for its full-size preview and activation instructions.

<details data-lc-flavor="night">
<summary><strong>Night</strong> · Dark · full palette</summary>

A real application capture is not available yet.

Run `/theme` and select **Living Code Night**. Its stored preference is `custom:living-code-night`.

</details>

<details data-lc-flavor="frost">
<summary><strong>Frost</strong> · Dark · softer chroma</summary>

A real application capture is not available yet.

Run `/theme` and select **Living Code Frost**. Its stored preference is `custom:living-code-frost`.

</details>

<details data-lc-flavor="paper">
<summary><strong>Paper</strong> · Light · near-white slate</summary>

A real application capture is not available yet.

Run `/theme` and select **Living Code Paper**. Its stored preference is `custom:living-code-paper`.

</details>

<details data-lc-flavor="signal">
<summary><strong>Signal</strong> · Dark · teal accent</summary>

A real application capture is not available yet.

Run `/theme` and select **Living Code Signal**. Its stored preference is `custom:living-code-signal`.

</details>

## Configuration

The files contain a display `name`, a `base` preset and documented `overrides`. Paper inherits `light`; the other flavors inherit `dark`. Diff backgrounds are tinted separately from the brighter word-level highlights. Shimmer colors and all eight subagent colors are included. Your terminal still owns the main screen background; use a matching Living Code terminal theme.

## Compatibility

Targets the custom-theme JSON API documented in the [Claude Code terminal configuration reference](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme). This is not a status-line workaround or a patched Claude binary. Old versions with only built-in presets need an update. The `effortUltra` override requires Claude Code 2.1.239 or later; older versions ignore unknown tokens. Fullscreen-only surfaces apply only in fullscreen mode. Tests validate the documented token contract; a full interactive visual capture is not included.

## Contributing

Found a problem? [Open an issue](https://github.com/living-code-theme/claude-code/issues/new/choose) with the app version, the flavor and a screenshot. Want Living Code somewhere else? [Request a port](https://github.com/living-code-theme/core/issues/new?template=port-request.yml).

Pull requests are welcome. Keep this README, `port.json` and `images/` in sync, and use real screenshots of the app, never mockups.

🦎 **One chameleon, many habitats.** Part of [Living Code](https://github.com/living-code-theme).

## License

[MIT](LICENSE) © Elliot Luque
