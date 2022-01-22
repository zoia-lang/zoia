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

if [ -d src/grammar/cpp/grammar ]
then
    # On Linux, ANTLR puts an extra /grammar into the output path
    mv src/grammar/cpp/grammar/* src/grammar/cpp
    rmdir src/grammar/cpp/grammar
else
    # On Windows (with a bash interpreter), it doesn't - so move them there
    mv src/zoiaLexer.py src/grammar/zoiaLexer.py
    mv src/zoiaParser.py src/grammar/zoiaParser.py
    mv src/zoiaVisitor.py src/grammar/zoiaVisitor.py
fi

# === Generate the Python module
if [ -f .venv/bin/activate ] # Linux
then
    # shellcheck source=/dev/null
    source .venv/bin/activate
    echo "Using virtual environment."
elif [ -f .venv/Scripts/activate ] # Windows
then
    # shellcheck source=/dev/null
    source .venv/Scripts/activate
    echo "Using virtual environment."
else
    echo "Virtual environment not found, using system interpreter instead."
    echo "This is not recommended."
fi
python <<EOF
from speedy_antlr_tool import generate

generate(
    py_parser_path="src/grammar/zoiaParser.py",
    cpp_output_dir="src/grammar/cpp",
    entry_rule_names=["zoiaFile"],
)
EOF

# === Cleanup
# Delete the interp/tokens files, we don't need them
find src -name "*.interp" -delete
find src -name "*.tokens" -delete

# Trim trailing whitespace, ANTLR does not clean it up
find src/grammar -type f -exec sed -i 's/[ \t]*$//' {} \;

# Trim all trailing newlines at the end of the files, ANTLR loves
# leaving those behind as well
find src/grammar -type f -exec sed -i -e :a -e '/^\n*$/{$d;N;};/\n$/ba' {} \;
