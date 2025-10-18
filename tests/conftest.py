import os
import re
import sys
import json
import subprocess
from pathlib import Path
import shutil
import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "sudoku_perm"

def have_console_script() -> bool:
    return shutil.which("sudoku-perm") is not None

def run_cli(args, use_console=False):
    if use_console or (not SCRIPT.exists()):
        cmd = ["sudoku-perm"] + args
    else:
        cmd = [str(SCRIPT)] + args
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=str(ROOT),
        env={**os.environ, "PYTHONUNBUFFERED": "1"},
    )
    return proc.returncode, proc.stdout

@pytest.fixture(scope="session")
def cli():
    use_console = not SCRIPT.exists() and have_console_script()
    def _runner(*args):
        return run_cli(list(args), use_console=use_console)
    return _runner

def strip_ansi(s: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", s)

@pytest.fixture
def no_ansi():
    return strip_ansi
