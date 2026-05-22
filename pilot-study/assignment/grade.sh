#!/bin/bash

readonly THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd | xargs realpath)"
readonly ATTEMPTS_DIR="$THIS_DIR/attempts"

function main() {
    set -e
    trap exit SIGINT

    mkdir -p "$ATTEMPTS_DIR"

    COUNT=1
    while [ -d "$ATTEMPTS_DIR/$COUNT" ]; do
        ((COUNT++))
    done

    mkdir "$ATTEMPTS_DIR/$COUNT"

    cp submission/solution.py $ATTEMPTS_DIR/$COUNT
    ./grader.py -s submission/ -o $ATTEMPTS_DIR/$COUNT/info.json 2>&1 | tee $ATTEMPTS_DIR/$COUNT/output.log

    echo -e "\nLogged attempt #$COUNT to $ATTEMPTS_DIR/$COUNT"
    return $?
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"

