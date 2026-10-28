# CapCut Audio

**Standalone local dialogue leveling: choose a project → process → A/B → Apply/Undo.**

[Vietnamese](README.md) · [Releases](https://github.com/Ductoii/capcut-audio/releases)

No Codex, chatbot, plugin, MCP, API key or chat request is needed at runtime. Cards and screenplay work use the separate [CapCut Cinematic Cards skill](https://github.com/Ductoii/capcut-cinematic-cards).

Requires Python 3.10–3.13 and FFmpeg/ffprobe:

```bash
curl -fsSL https://raw.githubusercontent.com/Ductoii/capcut-audio/v0.1.0/install-audio.py | python3
```

Launch `~/.local/bin/capcut-audio`. The installer creates a private runtime. Migration removes only the retired managed CapCut Harness plugin/skill/launcher/runtime and preserves audio jobs/Undo backups. No new skill is installed; unrelated plugins remain untouched.

- Discover projects from CapCut stores/indexes, custom save paths and OS search. Unsupported drafts remain visible with an editing reason. External discovery depends on OS indexing/access.
- **Level dialogue** runs algorithms directly on the computer, preparing listening files without editing the project.
- Compare original/processed audio, change settings or exclude false detections. Scoped media links do not depend on cookies; **Reload audio** refreshes playback.
- Save and close CapCut before Apply. An external root master is added and original audible participants are muted, preserving picture, compound structures and text.
- A changed timeline/source marks the old job **outdated**, with **Process current timeline again**. Undo refuses later foreign edits.

The source-local pipeline uses VAD, duration-weighted speech anchoring, bounded phrase trims, gentle 2:1 RMS compression and source/master peak protection. Defaults: −16 LUFS speech, −1.5 dBTP, stereo 48 kHz PCM24, maximum boost 48 dB. This is an online-film starting preset, not a universal film/MV standard. Separate music sources keep their level; embedded background/noise follows its source. No stem separation, reliable singing classification or restoration of already distorted audio.

Readable unencrypted local schema `360000`; unsupported routing/effects/variable speed are refused. No Computer Use. Source reconstruction is not native editor/export verification. Keep `~/.local/share/capcut-harness`: its legacy path preserves saved jobs and exact Undo references. New runtime: `~/.local/share/capcut-audio-tool`.

Syntax, scoped HTTP playback and packaging receive checks; no extra real-film/300-source validation cycle. macOS is the development environment; other operating systems remain unverified. [MIT](LICENSE).
