#!/usr/bin/env bash
set -euo pipefail
echo '[golden] Running golden test + pytest'
pytest -q
