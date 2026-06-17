"""Text preprocessing utilities for Hassaniya Arabic."""

import re
import unicodedata


class HassaniyaTextProcessor:
    """Preprocessor for Hassaniya Arabic text, handling normalization,
    cleaning, and tokenization specific to the dialect."""

    ARABIC_DIACRITICS = re.compile(r'[ً-ٰٟ]')

    CHAR_NORMALIZATIONS = {
        'آ': 'ا', 'أ': 'ا', 'إ': 'ا', 'ٱ': 'ا',
        'ؤ': 'و',
        'ئ': 'ي',
        'ة': 'ه',
        'ى': 'ي',
        'ٹ': 'ت',
        'ڤ': 'ف',
        'گ': 'ك',
    }

    def normalize(self, text: str) -> str:
        text = unicodedata.normalize('NFKC', text)
        text = self.ARABIC_DIACRITICS.sub('', text)
        for src, dst in self.CHAR_NORMALIZATIONS.items():
            text = text.replace(src, dst)
        text = re.sub(r'[^؀-ۿ\s.,،؛:؟!؟\-]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def tokenize(self, text: str) -> list[str]:
        return list(text.replace(' ', ' _ ').replace('_', ' _ ').split())

    def char_tokenize(self, text: str) -> list[str]:
        tokens = []
        for ch in text:
            if ch == ' ':
                tokens.append('<space>')
            else:
                tokens.append(ch)
        return tokens

    def get_vocab(self, texts: list[str]) -> dict[str, int]:
        chars = set()
        for text in texts:
            normalized = self.normalize(text)
            chars.update(normalized)
        vocab = {'<pad>': 0, '<sos>': 1, '<eos>': 2, '<space>': 3}
        for i, ch in enumerate(sorted(chars - {' '}), start=4):
            vocab[ch] = i
        return vocab

    def text_to_sequence(self, text: str, vocab: dict[str, int]) -> list[int]:
        normalized = self.normalize(text)
        tokens = self.char_tokenize(normalized)
        return [vocab.get(t, 0) for t in tokens]
