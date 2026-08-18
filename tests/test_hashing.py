from app.utils.hashing import canonical_url, content_hash, title_hash


def test_content_hash_normalizes():
    a = content_hash("  Hello   World  ")
    b = content_hash("hello world")
    assert a == b
    assert a is not None


def test_content_hash_none():
    assert content_hash("") is None
    assert content_hash(None) is None


def test_title_hash():
    assert title_hash("Título  A") == title_hash("título a")


def test_canonical_url():
    assert canonical_url("HTTPS://Example.com/Path/") == "https://example.com/Path"
    assert canonical_url("https://a.com/x#frag") == "https://a.com/x"
    assert canonical_url(None) is None