from __future__ import annotations

import json
import re
from pathlib import Path

NOTEBOOK = Path("notebooks/colab_a100_vllm.ipynb")
RUNBOOK = Path("COLAB.md")


def _sources() -> list[str]:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    return ["".join(cell["source"]) for cell in notebook["cells"]]


def test_notebook_is_valid_json_with_compiling_code_cells():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    assert len(notebook["cells"]) >= 20
    code_cells = [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    ]
    assert len(code_cells) >= 10
    for index, source in enumerate(code_cells):
        compile(source, f"notebook-code-{index}", "exec")


def test_notebook_covers_the_r2_pipeline_steps():
    sources = _sources()
    text = "\n".join(sources)
    for marker in (
        "ENABLE_NATIVE_TOOL_CALLS",
        "PERSIST_TO_DRIVE",
        "wishrec.materialize",
        "vllm serve",
        "Qwen/Qwen3-8B-AWQ",
        "Qwen/Qwen3-Embedding-0.6B",
        "wishrec.harness.endpoint_check",
        "wishrec.harness.smoothing",
        "wishrec.detector.train",
        "wishrec.harness.runner",
        "wishrec.harness.report",
        "--shards",
        "--smoothed",
        "files.download",
        "r2-artifacts",
        "EXPECTED_LEVELS_SHA256",
        "ALLOW_LEVELS_DRIFT",
        "levels tasks.jsonl sha256",
        "derived coverage",
        "INSTALL_VALIDATION_REQUIREMENTS",
        "requirements-validation.txt",
        "dry-run passes",
        "ModuleNotFoundError units",
        "CLEAR_CACHE_FOR_DRY_RUN",
        "dry run finished in",
        "data_provenance.json",
    ):
        assert marker in text, marker
    assert "--split heldout" not in text


def test_notebook_never_embeds_a_token_literal():
    text = "\n".join(_sources())
    patterns = (
        r"ghp_[A-Za-z0-9]{20,}",
        r"github_pat_[A-Za-z0-9_]{20,}",
        r"hf_[A-Za-z0-9]{20,}",
        r"sk-[A-Za-z0-9]{20,}",
    )
    for pattern in patterns:
        assert not re.search(pattern, text), pattern
    # The clone must not put a token in a URL.
    assert "x-access-token:$" not in text
    assert "x-access-token@" not in text


def test_runbook_covers_resume_troubleshooting_and_operator_checks():
    text = RUNBOOK.read_text(encoding="utf-8")
    for marker in (
        "What is verified locally vs by the operator",
        "## 1. Before you start",
        "## 2. Run order and expected wall-clock",
        "## 3. Step details",
        "## 4. Resume after a disconnect or session end",
        "## 5. Alternative: run vLLM in Colab, harness locally",
        "## 6. Troubleshooting",
        "## 7. Operator checklist",
        "GPU-hours",
        "cloudflared",
        "ngrok",
        "held-out",
        "make levels",
        "vLLM",
        "token",
    ):
        assert marker in text, marker
    assert "18 GPU-hours" in text


def test_repo_docs_point_at_the_r2_notebook_and_runbook():
    plan = Path("PLAN.md").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    for text in (plan, readme):
        assert "notebooks/colab_a100_vllm.ipynb" in text
        assert "COLAB.md" in text
    assert "local_fake_dry_run" in readme
    assert ".local-dry-run" in Path(".gitignore").read_text(encoding="utf-8")
