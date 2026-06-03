#!/bin/bash

readonly THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd | xargs realpath)"
readonly SUBMISSION_DIR="${THIS_DIR}/src"
readonly TEST_DIR="${THIS_DIR}/test-submissions"
readonly SOLUTION_PROFILE_NAME="solution_profile.json"
readonly FILENAME="main.py"

function main() {
    set -e
    trap exit SIGINT

    cp $TEST_DIR/solution/$FILENAME $SUBMISSION_DIR/$FILENAME

    ./profiler.py grader.profile_target_without_timeout \
        -s $SUBMISSION_DIR \
        -o $SOLUTION_PROFILE_NAME

    cp $TEST_DIR/not_implemented/$FILENAME $SUBMISSION_DIR/$FILENAME
    echo "Complete Setup."

    return $?
    }

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"

