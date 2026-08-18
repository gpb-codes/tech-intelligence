import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def _feed_xml():
    return """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Test Feed</title>
    <item>
      <title>OpenAI lanza un nuevo modelo</title>
      <link>https://example.com/post1</link>
      <guid>https://example.com/post1</guid>
      <description><![CDATA[<p>Anuncio del <b>nuevo modelo</b> de IA.</p>]]></description>
      <pubDate>Mon, 17 Aug 2026 10:00:00 GMT</pubDate>
    </item>
    <item>
      <title>GitHub actualiza su CLI</title>
      <link>https://example.com/post2</link>
      <guid>guid-2</guid>
      <description>Actualización de la CLI con nuevas funciones.</description>
      <pubDate>Tue, 18 Aug 2026 09:30:00 GMT</pubDate>
    </item>
  </channel>
</rss>
"""


def test_rss_parsing(db, monkeypatch):
    import feedparser

    from app.collector.rss import RSSAdapter
    from app.sources.models import Source

    source = Source(id="test-feed", name="Test", type="rss", url="https://example.com/feed.xml")

    def fake_fetch(self):
        return feedparser.parse(_feed_xml())

    # Probamos feedparser directamente con el XML
    parsed = feedparser.parse(_feed_xml())
    assert len(parsed.entries) == 2

    adapter = RSSAdapter(source)

    # Reemplazamos la descarga HTTP por el contenido local
    def fake_requests_get(url, timeout=30, headers=None):
        class FakeResp:
            content = _feed_xml().encode("utf-8")

            def raise_for_status(self):
                pass

        return FakeResp()

    monkeypatch.setattr("app.collector.rss.requests.get", fake_requests_get)
    articles = adapter.fetch()
    assert len(articles) == 2
    assert articles[0].title == "OpenAI lanza un nuevo modelo"
    assert articles[0].external_id == "https://example.com/post1"
    assert "nuevo modelo" in articles[0].content
    assert articles[0].published_at.startswith("2026-08-17")
    assert articles[0].source_type == "rss"


def test_rss_error(db, monkeypatch):
    from app.collector.rss import RSSAdapter
    from app.collector.base import FetchError
    from app.sources.models import Source

    source = Source(id="bad", name="Bad", type="rss", url="https://example.com/nope.xml")

    def fake_get(url, timeout=30, headers=None):
        import requests

        raise requests.RequestException("connection refused")

    monkeypatch.setattr("app.collector.rss.requests.get", fake_get)
    with pytest.raises(FetchError):
        RSSAdapter(source).fetch()