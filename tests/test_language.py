from app.ollama.language import LanguageDetector, needs_translation


def test_detect_english():
    assert LanguageDetector.detect("The quick brown fox jumps over the lazy dog and runs.") == "en"


def test_detect_spanish():
    assert LanguageDetector.detect("El sistema recopila información tecnológica y la clasifica de forma automática.") == "es"


def test_detect_japanese():
    assert LanguageDetector.detect("これは技術情報を自動的に収集するシステムです。") == "ja"


def test_detect_chinese():
    assert LanguageDetector.detect("这是一个自动收集技术信息的系统。") == "zh"


def test_detect_portuguese():
    assert LanguageDetector.detect("O sistema coleta informações tecnológicas automaticamente e as classifica.") == "pt"


def test_detect_french():
    assert LanguageDetector.detect("Le système collecte automatiquement des informations technologiques.") == "fr"


def test_detect_german():
    assert LanguageDetector.detect("Das System sammelt automatisch technologische Informationen und klassifiziert sie.") == "de"


def test_detect_unknown_empty():
    assert LanguageDetector.detect("") == "unknown"
    assert LanguageDetector.detect(None) == "unknown"


def test_needs_translation():
    assert needs_translation("en") is True
    assert needs_translation("ja") is True
    assert needs_translation("es") is False
    assert needs_translation("unknown") is False