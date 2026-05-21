#!/bin/bash

readonly THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd | xargs realpath)"

function main() {
    set -e
    trap exit SIGINT

    ./profiler.py grader.profile_target_without_timeout \
        -s test-submissions/solution \
        -o solution_profile.json

    echo "Setup Succeeded"

    return $?
    }

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"

