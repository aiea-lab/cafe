#!/bin/bash

readonly THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd | xargs realpath)"
readonly SUBMISSION_DIR="${THIS_DIR}/src"
readonly TEST_DIR="${THIS_DIR}/test-submissions"
readonly SOLUTION_PROFILE_NAME="solution_profile.json"
readonly FILENAME="main.py"

function main() {
    set -e
    trap exit SIGINT

    python3 -m cafe.cli.profile -s $TEST_DIR/solution "grader.BFS" -o $SOLUTION_PROFILE_NAME
    echo "Complete Setup."

    return $?
    }

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"

