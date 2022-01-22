#!/bin/bash
# This script generates and builds the Zoia parser using ANTLR.
set -e

if [ ! -f scripts/antlr.jar ]
then
    echo "$(realpath scripts/antlr.jar) is missing. Run scripts/prereq.sh to download it."
    exit 1
fi

# Add antlr.jar to the classpath
CLASSPATH=".:$(realpath scripts/antlr.jar):$CLASSPATH"
export CLASSPATH

# === Generate the Python parser
java org.antlr.v4.Tool -Dlanguage=Python3 -o src -visitor -no-listener grammar/zoia.g4

# === Generate the C++ parser
java org.antlr.v4.Tool -Dlanguage=Cpp -o src/grammar/cpp -visitor -no-listener grammar/zoia.g4

# Stupid ANTLR places these incorrectly
mv src/grammar/cpp/grammar/* src/grammar/cpp
rmdir src/grammar/cpp/grammar

# === Generate the Python module
if [ -f .venv/bin/activate ]
then
    # shellcheck source=/dev/null
    source .venv/bin/activate
    echo "Using virtual environment."
else
    echo "Virtual environment not found, using system interpreter instead."
    echo "This is not recommended."
fi
python3 <<EOF
from speedy_antlr_tool import generate

generate(
    py_parser_path="src/grammar/zoiaParser.py",
    cpp_output_dir="src/grammar/cpp",
    entry_rule_names=["zoiaFile"],
)
EOF

# === Cleanup
# Delete the interp/tokens files, we don't need them
find src/grammar -name "*.interp" -delete
find src/grammar -name "*.tokens" -delete

# Trim trailing whitespace, ANTLR does not clean it up
find src/grammar -type f -exec sed -i 's/[ \t]*$//' {} \;

# Trim all trailing newlines at the end of the files, ANTLR loves
# leaving those behind as well
find src/grammar -type f -exec sed -i -e :a -e '/^\n*$/{$d;N;};/\n$/ba' {} \;
