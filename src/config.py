"""Project configuration constants."""

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
METADATA_PATH = os.path.join(DATA_DIR, "metadata.csv")

RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
SPECTROGRAMS_DIR = os.path.join(RESULTS_DIR, "spectrograms")
GENERATED_AUDIO_DIR = os.path.join(RESULTS_DIR, "generated_audio")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")

SAMPLE_RATE = 22050
N_FFT = 1024
HOP_LENGTH = 256
N_MELS = 80
MAX_WAV_LENGTH = 10  # seconds

HASSANIYA_CHARS = (
    "ابتثجحخدذرزسشصضطظعغفقكلمنهويءآأإؤئةى"
    "َُِّْـًٌٍ"
    " .,،؛:؟!-"
)
