# Feature Proposal: Speaker Diarization

## Objective
Integrate speaker diarization into the Vault Video Enhancer to distinguish between multiple speakers in the generated SRT files (e.g., `[Speaker 1]: "Hello"`, `[Speaker 2]: "Hi"`).

## Value Proposition
Improves the accessibility and readability of transcribed media, especially for interviews, meetings, and multi-actor scenes.

## Implementation Plan (for 'kraftwerk' agent)
1.  **Dependencies**: Add `pyannote.audio` to `requirements.txt`.
2.  **Core Logic**: Create `vault_enhancer/diarization.py` to handle the `pyannote.audio` pipeline and token management.
3.  **Integration**: Update `vault_enhancer/core.py` to optionally run the diarization pipeline after ASR and align the diarized segments with the ASR text.
4.  **CLI/GUI Updates**: Add a `--diarization` flag to `enhancer.py` and a corresponding checkbox to `vault_gui.py`.
