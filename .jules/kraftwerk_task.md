# Task Assignment: 'kraftwerk'

## Feature: Speaker Diarization
Implement speaker diarization in `vault-video-enhancer` to distinguish between multiple speakers in generated SRT files.

### Requirements:
1.  **Dependency**: Add `pyannote.audio` to `requirements.txt`.
2.  **Core Logic**: Create a new module `vault_enhancer/diarization.py` that utilizes `pyannote.audio`'s pre-trained speaker diarization pipeline to generate speaker segments.
3.  **Integration**: Modify `vault_enhancer/core.py` to:
    -   Accept a `diarization` boolean parameter.
    -   Run the diarization pipeline if requested.
    -   Align the ASR transcript segments with the diarization segments to attribute text to speakers.
4.  **CLI/GUI**:
    -   Update `enhancer.py` to include a `--diarization` argument.
    -   Update `vault_gui.py` to include a "Enable Diarization" checkbox in the UI.

### Constraints:
-   Maintain 100% local processing (weights on-device).
-   Adhere to VaultWares security coding standards (no hardcoded secrets/tokens). The `pyannote.audio` pipeline requires an HF token, which MUST be loaded securely (e.g., from an environment variable `HF_AUTH_TOKEN`, NEVER hardcoded).

### Status: Delegated by Ziegler (2024-05-09)
