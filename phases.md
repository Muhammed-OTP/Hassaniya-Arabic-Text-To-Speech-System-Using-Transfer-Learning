# Execution Plan: 22:10 → 03:00 (4h 50min)

## Realistic Assessment

**What we have:**
- Empty GitHub repo
- Small Hassaniya dataset (to be added)
- Transfer learning strategy (no training from scratch)

**What we need to produce:**
1. Professional GitHub repository with README
2. 4 Jupyter notebooks (exploration, annotation, preprocessing, TTS demo)
3. Complete LaTeX report (10-15 pages)
4. HTML/CSS/JS presentation (15 slides)
5. Oral defense preparation (30 Q&A)

**Key simplification decisions:**
- Use gTTS/Coqui pretrained models — NO training from scratch
- Present as MVP/proof-of-concept — honest about limitations
- Synthetic demo if fine-tuning fails — explain why in report
- Focus on pipeline explanation over actual model performance

---

## Phase 1: Repository Foundation (22:10 → 22:40) — 30 min
- [x] Create CLAUDE.md
- [x] Create phases.md
- [ ] Create complete directory structure
- [ ] Generate README.md with Mermaid diagrams
- [ ] Create requirements.txt
- [ ] Create LICENSE
- [ ] Create sample metadata.csv with Hassaniya examples
- [ ] Create src/ modules (preprocessing, utils)

## Phase 2: Notebooks (22:40 → 23:30) — 50 min
- [ ] 01_data_exploration.ipynb — load data, stats, visualizations
- [ ] 02_annotation.ipynb — text normalization, phoneme mapping
- [ ] 03_preprocessing.ipynb — audio processing, spectrograms, feature extraction
- [ ] 04_tts_demo.ipynb — TTS pipeline demo with pretrained model

## Phase 3: LaTeX Report (23:30 → 01:00) — 1h 30min
- [ ] Cover page with student info
- [ ] Abstract + Introduction
- [ ] Problem Statement + Related Work
- [ ] Dataset Collection + Annotation
- [ ] Text Preprocessing + TTS Architecture
- [ ] Transfer Learning Strategy
- [ ] Experiments + Results (honest/preliminary)
- [ ] Limitations + Future Work + Conclusion
- [ ] References (real citations)

## Phase 4: HTML Presentation (01:00 → 02:00) — 1h
- [ ] 15-slide HTML/CSS/JS presentation
- [ ] Speaker notes for each slide
- [ ] Professional styling
- [ ] Mermaid/diagrams embedded

## Phase 5: Defense Preparation (02:00 → 02:30) — 30 min
- [ ] 30 likely teacher questions with answers
- [ ] Key concepts cheat sheet
- [ ] Architecture explanation practice points

## Phase 6: Final Push (02:30 → 03:00) — 30 min
- [ ] Review all deliverables
- [ ] Git commit everything
- [ ] Push to GitHub
- [ ] Final quality check

---

## Priority Order (if running out of time)
1. **README + repo structure** (first impression matters)
2. **LaTeX report** (main graded deliverable)
3. **Presentation** (soutenance tomorrow)
4. **Notebooks** (shows implementation work)
5. **Q&A prep** (can review on the way to class)

## Fallback Strategy
If Coqui TTS installation fails:
- Use gTTS (Google Text-to-Speech) for Arabic demo
- Show preprocessing pipeline with Librosa
- Explain architecture theoretically in report
- Generate spectrograms from existing audio
- Frame as "pipeline ready for fine-tuning when compute is available"
