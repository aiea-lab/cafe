#!/bin/bash

readonly THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd | xargs realpath)"

function main() {
    set -e
    trap exit SIGINT

    cp test-submissions/solution/solution.py submission/solution.py

    ./profiler.py grader.profile_target_without_timeout \
        -s $THIS_DIR/submission\
        -o solution_profile.json

    cp test-submissions/not_implemented/solution.py submission/solution.py
    echo "Complete Setup."

    return $?
    }

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"

