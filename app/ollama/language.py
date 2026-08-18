"""Detección de idioma local (heurística, sin servicios externos).

Estrategia:
1. Scripts no latinos (CJK, kana, hangul, cirílico, etc.) -> idioma directo.
2. Texto latino -> conteo de stopwords por idioma.
"""
from __future__ import annotations

import re

KANA_RE = re.compile(r"[\u3040-\u30ff]")
HANZI_RE = re.compile(r"[\u4e00-\u9fff]")
HANGUL_RE = re.compile(r"[\uac00-\ud7af]")
CYRILLIC_RE = re.compile(r"[\u0400-\u04ff]")
GREEK_RE = re.compile(r"[\u0370-\u03ff]")
HEBREW_RE = re.compile(r"[\u0590-\u05ff]")
ARABIC_RE = re.compile(r"[\u0600-\u06ff]")
THAI_RE = re.compile(r"[\u0e00-\u0e7f]")
DEVANAGARI_RE = re.compile(r"[\u0900-\u097f]")

STOPWORDS = {
    "es": {"el", "la", "los", "las", "de", "del", "que", "y", "en", "un", "una", "es", "por", "para", "con", "se", "su", "lo", "al", "como", "más", "pero", "este", "esta"},
    "en": {"the", "and", "of", "to", "in", "is", "a", "for", "with", "on", "that", "it", "this", "are", "was", "be", "as", "at", "by", "or", "an"},
    "pt": {"o", "a", "os", "as", "de", "do", "da", "que", "e", "em", "um", "uma", "é", "por", "para", "com", "se", "sua", "seu", "como", "mais", "mas", "este", "esta"},
    "fr": {"le", "la", "les", "de", "du", "des", "et", "en", "un", "une", "est", "pour", "avec", "sur", "que", "qui", "dans", "par", "au", "aux", "ce", "cette"},
    "de": {"der", "die", "das", "den", "dem", "und", "ist", "ein", "eine", "für", "mit", "auf", "von", "zu", "im", "in", "als", "auch", "dass", "bei", "nach"},
    "it": {"il", "lo", "la", "i", "gli", "le", "di", "del", "e", "è", "un", "una", "per", "con", "che", "in", "su", "come", "più", "ma", "questo", "questa"},
    "nl": {"de", "het", "een", "van", "en", "is", "voor", "met", "op", "in", "dat", "zijn", "niet", "als", "aan", "ook", "maar", "bij", "naar", "die"},
    "ja": {"の", "です", "を", "に", "は", "が", "た", "て", "で", "と", "ます", "こと", "する", "な", "も", "か"},
    "zh": {"的", "是", "了", "在", "和", "有", "不", "这", "为", "与", "也", "很", "会", "对", "中", "我们", "可以"},
    "ko": {"은", "는", "이", "가", "을", "를", "에", "의", "도", "으로", "에서", "하다", "있다", "합니다"},
    "ru": {"и", "в", "не", "на", "я", "что", "он", "с", "как", "это", "по", "но", "они", "она", "так", "же", "из", "от", "для"},
    "uk": {"і", "в", "не", "на", "що", "з", "як", "це", "по", "але", "вони", "для", "та"},
    "pl": {"i", "w", "nie", "na", "to", "się", "z", "jest", "że", "do", "od", "dla", "ale", "jak"},
    "tr": {"ve", "bir", "bu", "için", "ile", "de", "da", "olan", "olarak", "daha", "gibi", "ama"},
    "id": {"dan", "yang", "di", "dengan", "untuk", "dari", "ini", "itu", "adalah", "pada", "ke", "juga", "tidak"},
    "sv": {"och", "i", "att", "det", "som", "en", "ett", "för", "med", "på", "av", "är", "den", "till"},
    "da": {"og", "i", "at", "det", "som", "en", "et", "for", "med", "på", "af", "er", "den", "til"},
    "no": {"og", "i", "at", "det", "som", "en", "et", "for", "med", "på", "av", "er", "den", "til"},
    "fi": {"ja", "on", "ei", "että", "se", "sen", "hän", "kuin", "myös", "tai", "joka", "ovat"},
}

SCRIPT_MAP = [
    (KANA_RE, "ja"),
    (HANZI_RE, "zh"),
    (HANGUL_RE, "ko"),
    (CYRILLIC_RE, "ru"),
    (GREEK_RE, "el"),
    (HEBREW_RE, "he"),
    (ARABIC_RE, "ar"),
    (THAI_RE, "th"),
    (DEVANAGARI_RE, "hi"),
]


class LanguageDetector:
    """Detector heurístico de idioma."""

    @staticmethod
    def detect(text: str | None) -> str:
        if not text:
            return "unknown"
        text = text.strip()
        if len(text) < 10:
            return "unknown"

        # 1. Scripts no latinos
        for regex, lang in SCRIPT_MAP:
            matches = regex.findall(text)
            if matches and len(matches) >= 2:
                return lang
        # Japonés usa kana + hanzi
        if KANA_RE.search(text):
            return "ja"

        # 2. Latín: stopwords
        words = re.findall(r"[a-zA-Zà-ÿÀ-Ý]{1,}", text.lower())
        if not words:
            return "unknown"
        scores = {}
        for lang, stops in STOPWORDS.items():
            if lang in ("ja", "zh", "ko", "ru", "uk"):
                continue
            scores[lang] = sum(1 for w in words if w in stops)
        best = max(scores, key=scores.get) if scores else "unknown"
        if scores.get(best, 0) < 2:
            return "unknown"
        return best


detect_language = LanguageDetector.detect


def needs_translation(lang: str | None) -> bool:
    """¿El contenido debe traducirse al español?"""
    return lang not in (None, "", "es", "unknown")