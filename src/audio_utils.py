"""Audio processing utilities for the Hassaniya TTS pipeline."""

import io
import numpy as np

try:
    import librosa
    import librosa.display
    LIBROSA_AVAILABLE = True
except ImportError:
    LIBROSA_AVAILABLE = False

try:
    import soundfile as sf
    SOUNDFILE_AVAILABLE = True
except ImportError:
    SOUNDFILE_AVAILABLE = False

from .config import SAMPLE_RATE, N_FFT, HOP_LENGTH, N_MELS


def bytes_to_waveform(audio_bytes: bytes, sr: int = SAMPLE_RATE):
    if SOUNDFILE_AVAILABLE:
        audio, orig_sr = sf.read(io.BytesIO(audio_bytes))
        if orig_sr != sr and LIBROSA_AVAILABLE:
            audio = librosa.resample(audio.astype(np.float32), orig_sr=orig_sr, target_sr=sr)
        return audio.astype(np.float32), sr
    raise ImportError("soundfile is required to decode audio bytes")


def compute_mel_spectrogram(waveform: np.ndarray, sr: int = SAMPLE_RATE):
    if not LIBROSA_AVAILABLE:
        raise ImportError("librosa is required for mel spectrogram computation")
    mel = librosa.feature.melspectrogram(
        y=waveform, sr=sr, n_fft=N_FFT,
        hop_length=HOP_LENGTH, n_mels=N_MELS
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)
    return mel_db


def compute_mfcc(waveform: np.ndarray, sr: int = SAMPLE_RATE, n_mfcc: int = 13):
    if not LIBROSA_AVAILABLE:
        raise ImportError("librosa is required for MFCC computation")
    return librosa.feature.mfcc(
        y=waveform, sr=sr, n_mfcc=n_mfcc,
        n_fft=N_FFT, hop_length=HOP_LENGTH
    )


def get_audio_duration(waveform: np.ndarray, sr: int = SAMPLE_RATE) -> float:
    return len(waveform) / sr


def trim_silence(waveform: np.ndarray, top_db: int = 20):
    if not LIBROSA_AVAILABLE:
        raise ImportError("librosa is required for silence trimming")
    trimmed, _ = librosa.effects.trim(waveform, top_db=top_db)
    return trimmed
