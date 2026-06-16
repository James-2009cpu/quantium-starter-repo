#!/usr/bin/env bash
#
# run_tests.sh
#
# Continuous-integration helper for the Soul Foods Sales Visualiser.
# It:
#   1. activates the project virtual environment,
#   2. runs the Dash test suite with pytest, and
#   3. exits 0 if every test passed, or 1 if anything went wrong.

# Always run from the directory that contains this script, so the
# relative paths below work no matter where the script is invoked from.
cd "$(dirname "$0")" || exit 1

# 1. Activate the virtual environment.
#    Linux/macOS venvs put the activate script in venv/bin, while
#    Windows venvs put it in venv/Scripts. Support both.
if [ -f "venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    # shellcheck disable=SC1091
    source venv/Scripts/activate
else
    echo "ERROR: could not find the virtual environment activate script." >&2
    echo "Expected venv/bin/activate or venv/Scripts/activate." >&2
    exit 1
fi

# 2. Execute the test suite.
python -m pytest test_app.py
status=$?

# 3. Return 0 on success, 1 on any failure.
if [ $status -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed (pytest exit code: $status)."
    exit 1
fi
