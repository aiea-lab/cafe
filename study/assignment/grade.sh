#!/bin/bash

readonly THIS_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd | xargs realpath)"
readonly ATTEMPTS_DIR="$THIS_DIR/attempts"
readonly SUBMISSION_DIR="${THIS_DIR}/src"
readonly FILENAME="main.py"
readonly LOG_FILENAME="output.log"
readonly INFO_FILENAME="info.json"

function main() {
    set -e
    trap exit SIGINT

    mkdir -p "$ATTEMPTS_DIR"

    COUNT=1
    while [ -d "$ATTEMPTS_DIR/$COUNT" ]; do
        ((COUNT++))
    done

    mkdir "$ATTEMPTS_DIR/$COUNT"

    ./grader.py -s $SUBMISSION_DIR -o $ATTEMPTS_DIR/$COUNT/$INFO_FILENAME 2>&1 | tee $ATTEMPTS_DIR/$COUNT/$LOG_FILENAME
    cp $SUBMISSION_DIR/$FILENAME $ATTEMPTS_DIR/$COUNT

    echo -e "\nLogged attempt #$COUNT to $ATTEMPTS_DIR/$COUNT"
    return $?
}

[[ "${BASH_SOURCE[0]}" == "${0}" ]] && main "$@"

