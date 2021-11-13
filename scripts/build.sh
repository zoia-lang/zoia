#!/bin/bash
# This script generates and builds wizparse using ANTLR.

if [ ! -f scripts/antlr.jar ]
then
    echo "$(realpath scripts/antlr.jar) is missing. Run scripts/prereq.sh to download it."
    exit 1
fi

# Add antlr.jar to the classpath
CLASSPATH=".:$(realpath scripts/antlr.jar):$CLASSPATH"
export CLASSPATH

# Generate the parser
java org.antlr.v4.Tool -Dlanguage=Python3 -o src grammar/zoia.g4

# Delete the interp/tokens files, we don't need them
find src -name "*.interp" -delete
find src -name "*.tokens" -delete
