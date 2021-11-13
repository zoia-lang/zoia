#!/bin/bash
# Collection of useful functions and aliases when working on zoia.
# Use via `source scripts/aliases.sh` from the top level.

CLASSPATH=".:$(realpath scripts/antlr.jar)"
export CLASSPATH

ZOIA_TMP_DIR="$(realpath tmp/grammar)"

# Parses a zoia file provided as the command line argument, regardless
# of what your cwd is.
function parse_zoia() {
    test_file="$1"
    if [ -z "$test_file" ]
    then
        echo "Missing argument: path to file"
        return 1
    fi

    real_file=$(realpath "$test_file")
    if [ ! -f "$real_file" ]
    then
        echo "$real_file does not exist or is not a file."
        return 2
    fi

    cwd="$(pwd)"
    if [ ! -d "$ZOIA_TMP_DIR" ]
    then
        echo "$ZOIA_TMP_DIR does not exist. Run scripts/build.sh to create it."
        return 3
    fi

    cd "$ZOIA_TMP_DIR" || return
    java org.antlr.v4.gui.TestRig zoia zoiaFile "$real_file" "${@:2}"
    cd "$cwd" || return
}
