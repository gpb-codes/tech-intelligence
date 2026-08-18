"""Tests del cliente Git (sin tocar repositorios reales)."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest


@pytest.fixture
def git_dir(tmp_path):
    d = tmp_path / "repo"
    d.mkdir()
    subprocess.run(["git", "init"], cwd=str(d), capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=str(d), capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=str(d), capture_output=True)
    return d


def test_commit_creates_commit(git_dir):
    from app.gitutils import git as g

    (git_dir / "file.md").write_text("# Hola", encoding="utf-8")
    assert g.commit(git_dir, "tech-intelligence: sync 2026-08-17") is True


def test_commit_no_changes_no_empty_commit(git_dir):
    from app.gitutils import git as g

    assert g.commit(git_dir, "tech-intelligence: sync 2026-08-17") is False


def test_is_repo_and_init(git_dir, tmp_path):
    from app.gitutils import git as g

    assert g.is_repo(git_dir) is True
    assert g.is_repo(tmp_path) is False
    assert g.init(tmp_path) is True
    assert g.init(tmp_path) is False


def test_forbidden_commands_rejected(git_dir):
    from app.gitutils import git as g

    with pytest.raises(g.GitError):
        g.commit(git_dir, "reset --hard ahora")