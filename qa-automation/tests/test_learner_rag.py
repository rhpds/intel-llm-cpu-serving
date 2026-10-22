"""Execute the Python checks learners actually copy, using synthetic API replies."""
import json
import re
import subprocess
import sys
from pathlib import Path
import pytest

PAGES = Path(__file__).resolve().parents[2] / "content/modules/ROOT/pages"

def run_check(tmp_path, marker, data):
    source = next(p.read_text() for p in PAGES.glob("*.adoc") if "<<'" + marker + "'" in p.read_text())
    code = re.search(r"<<'" + marker + r"'\n(.*?)\n" + marker, source, re.S).group(1)
    filename = {"WORKSPACE_PY": "workspace.json", "UPLOAD_PY": "upload.json", "EMBED_PY": "embeddings.json", "ANSWER_PY": "grounded-answer.json", "MEMBERSHIP_PY": "workspace-documents.json"}[marker]
    (tmp_path / filename).write_text(json.dumps(data))
    return subprocess.run([sys.executable, "-c", code], cwd=tmp_path, capture_output=True)

def test_repeated_workspace_uses_returned_slug(tmp_path):
    assert run_check(tmp_path, "WORKSPACE_PY", {"workspace": {"slug": "hr-assistant-2"}}).returncode == 0
    assert (tmp_path / "workspace-slug.txt").read_text() == "hr-assistant-2"

def test_embedding_uses_every_returned_location(tmp_path):
    paths = ["custom-documents/policy-uuid.json", "custom-documents/policy-other.json"]
    assert run_check(tmp_path, "UPLOAD_PY", {"success": True, "documents": [{"location": p} for p in paths]}).returncode == 0
    assert json.loads((tmp_path / "embeddings-request.json").read_text()) == {"adds": paths}

@pytest.mark.parametrize("data", [{"success": False, "documents": []}, {"success": True, "documents": [{}]}, {"success": True, "error": "failed", "documents": [{"location": "x"}]}])
def test_invalid_upload_stops_before_embedding(tmp_path, data):
    assert run_check(tmp_path, "UPLOAD_PY", data).returncode != 0
    assert not (tmp_path / "embeddings-request.json").exists()

@pytest.mark.parametrize("data", [{}, {"success": False}, {"success": True, "error": "failed"}])
def test_embedding_error_is_not_success(tmp_path, data):
    assert run_check(tmp_path, "EMBED_PY", data).returncode != 0

def test_grounded_answer_requires_fact_and_policy_source(tmp_path):
    good = {"type": "textResponse", "textResponse": "Use CEDAR-742.", "sources": [{"title": "northstar-policy.txt"}]}
    assert run_check(tmp_path, "ANSWER_PY", good).returncode == 0
    for update in ({"sources": []}, {"textResponse": "Use another code"}, {"error": "backend failed"}, {"sources": [{"title": "unrelated.txt"}]}):
        assert run_check(tmp_path, "ANSWER_PY", dict(good, **update)).returncode != 0


def test_embedding_acceptance_uses_workspace_response(tmp_path):
    assert run_check(tmp_path, "EMBED_PY", {"workspace": {"slug": "hr-assistant"}}).returncode == 0


def test_membership_requires_exact_uploaded_document(tmp_path):
    (tmp_path / "embeddings-request.json").write_text(json.dumps({"adds": ["custom-documents/policy-uuid.json"]}))
    good = {"workspace": [{"documents": [{"docpath": "custom-documents/policy-uuid.json"}]}]}
    assert run_check(tmp_path, "MEMBERSHIP_PY", good).returncode == 0
    for data in ({"workspace": []}, {"workspace": [{"documents": []}]}, {"workspace": [{"documents": [{"docpath": "another-file"}]}]}):
        assert run_check(tmp_path, "MEMBERSHIP_PY", data).returncode != 0
