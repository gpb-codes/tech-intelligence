import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database.connection import get_connection
from app.database.schema import init_db


@pytest.fixture
def db(tmp_path):
    conn = get_connection(tmp_path / "test.db")
    init_db(conn)
    yield conn
    conn.close()


@pytest.fixture
def settings(tmp_path):
    from app.utils.config import Settings

    s = Settings()
    s.vault_path = tmp_path / "vault"
    s.database_path = tmp_path / "database" / "test.db"
    s.log_dir = tmp_path / "logs"
    s.vault_path.mkdir(parents=True, exist_ok=True)
    return s