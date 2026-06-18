"""Quick end-to-end smoke test for the Hassaniya TTS MVP pipeline."""

from __future__ import annotations

import io
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def main() -> int:
    errors: list[str] = []
    print(f"Python: {sys.version.split()[0]}")
    print(f"Project: {PROJECT_ROOT}\n")

    try:
        import pandas as pd
        import numpy as np
        import librosa
        import soundfile as sf
        print("[OK] pandas, numpy, librosa, soundfile")
    except Exception as exc:
        errors.append(f"imports: {exc}")
        pd = None

    df = None
    if pd is not None:
        try:
            parquet_path = os.path.join(PROJECT_ROOT, "audios_dataset.parquet")
            df = pd.read_parquet(parquet_path)
            print(f"[OK] parquet: {len(df)} rows, columns={list(df.columns)}")
        except Exception as exc:
            errors.append(f"parquet: {exc}")

    if df is not None:
        try:
            from src.preprocessing import HassaniyaTextProcessor

            processor = HassaniyaTextProcessor()
            text = df["transcription"].iloc[0]
            norm = processor.normalize(text)
            ids = processor.text_to_sequence(text, processor.get_vocab([text]))
            print(f"[OK] preprocessing: len={len(norm)}, token_ids={len(ids)}")
        except Exception as exc:
            errors.append(f"preprocessing: {exc}")

        try:
            from src.audio_utils import bytes_to_waveform, compute_mel_spectrogram

            sample = df["audio"].iloc[0]
            audio_bytes = sample.get("bytes", b"") if isinstance(sample, dict) else b""
            if not audio_bytes:
                raise ValueError("empty audio bytes in first row")
            wav, sr = bytes_to_waveform(audio_bytes)
            mel = compute_mel_spectrogram(wav, sr)
            print(f"[OK] audio: {len(wav)/sr:.2f}s @ {sr}Hz, mel={mel.shape}")
        except Exception as exc:
            errors.append(f"audio: {exc}")

    try:
        import torch
        print(f"[OK] torch {torch.__version__}, cuda={torch.cuda.is_available()}")
    except Exception as exc:
        errors.append(f"torch: {exc}")

    try:
        from gtts import gTTS

        out_dir = os.path.join(PROJECT_ROOT, "results", "generated_audio")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "smoke_test.mp3")
        gTTS(text="السلام عليكم", lang="ar").save(out_path)
        print(f"[OK] gTTS: {out_path} ({os.path.getsize(out_path)} bytes)")
    except Exception as exc:
        errors.append(f"gtts (needs internet): {exc}")

    if errors:
        print("\n[FAILURES]")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("\nAll smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
