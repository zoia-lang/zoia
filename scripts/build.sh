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
find src/grammar -name "*.interp" -delete
find src/grammar -name "*.tokens" -delete

# Trim trailing whitespace, ANTLR does not clean it up
find src/grammar -type f -exec sed -i 's/[ \t]*$//' {} \;

# Trim all trailing newlines at the end of the files, ANTLR loves
# leaving those behind as well
find src/grammar -type f -exec sed -i -e :a -e '/^\n*$/{$d;N;};/\n$/ba' {} \;
