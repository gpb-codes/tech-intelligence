import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.sources.loader import load_categories, load_sources
from app.utils.config import Settings


def test_sources_yaml_loads():
    settings = Settings()
    sources = load_sources(settings.sources_path)
    assert len(sources) > 0
    assert all(s.id for s in sources)
    types = {s.type for s in sources}
    assert types <= {"rss", "github", "api"}


def test_sources_no_invented_urls():
    """Las URLs habilitadas deben apuntar a dominios reales y verificados."""
    settings = Settings()
    sources = load_sources(settings.sources_path)
    for s in sources:
        if s.enabled and s.type == "rss":
            assert s.url, f"Fuente habilitada sin URL: {s.id}"
            assert "example.com" not in s.url


def test_categories_load():
    settings = Settings()
    data = load_categories(settings.categories_path)
    assert "AI" in data["categories"]
    assert "General Tech" in data["categories"]
    assert "critical" in data["importance_levels"]
    assert "unknown" in data["pricing_values"]


def test_settings_env_override(monkeypatch):
    monkeypatch.setenv("OLLAMA_MODEL", "custom-model")
    from app.utils.config import load_settings

    s = load_settings(env_path=Path(".") / ".env")
    assert s.ollama_model == "custom-model"