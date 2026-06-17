# Hassaniya Arabic Text-To-Speech System Using Transfer Learning

## Project Overview
Academic MVP/proof-of-concept for a Hassaniya dialect TTS system using transfer learning.
Master M1 AI — NLP Dialects Module.

## Student
- **Name:** Mohamed Salem Ebnou Echvagha Oubeid
- **ID:** C34613
- **Module:** NLP Dialects
- **Date:** 18/06/2026

## Key Constraints
- Small Hassaniya dataset (limited recordings)
- Limited time (single night implementation)
- Beginner/intermediate Speech AI knowledge
- Framed as **proof of concept**, NOT production system

## Technical Strategy
- **Primary:** Transfer learning with pretrained TTS models (Coqui TTS / gTTS fallback)
- **Fallback:** Dataset preprocessing + annotation + architecture explanation + synthetic demo
- No training from scratch — explain why in report (data/compute requirements)

## Tech Stack
Python, Google Colab, Pandas, NumPy, Librosa, Matplotlib, PyTorch, Coqui TTS (or gTTS fallback)

## Repository Structure
```
hassaniya-tts/
├── data/raw/              # Raw audio files
├── data/processed/        # Processed audio
├── data/metadata.csv      # Text-audio mappings
├── notebooks/             # Jupyter notebooks (01-04)
├── src/                   # Python source modules
├── reports/               # LaTeX report
├── presentation/          # HTML/CSS/JS slides
├── results/               # Spectrograms, generated audio, figures
├── requirements.txt
├── README.md
└── LICENSE
```

## Commands
- Install deps: `pip install -r requirements.txt`
- Run notebooks in order: 01 → 02 → 03 → 04
- Build report: `pdflatex reports/report.tex`
- Open presentation: `presentation/index.html`

## Style
- All notebooks: markdown explanations + educational comments
- Report: academic LaTeX, 10-15 pages
- Presentation: 15 slides HTML/CSS/JS
- Code comments: beginner-friendly, bilingual (EN/FR where helpful)
