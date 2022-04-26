#!/bin/bash
# This script downloads all build prerequisites for wizparse.
set -e

ANTLR_VER='4.10.1'

# Download the latest ANTLR release.
curl https://www.antlr.org/download/antlr-"$ANTLR_VER"-complete.jar --output scripts/antlr.jar
curl https://www.antlr.org/download/antlr4-cpp-runtime-"$ANTLR_VER"-source.zip --output /tmp/cpp_antlr_src.zip

# Unzip and copy over the C++ sources (src folder only, not the solutions etc.)
rm -rf /tmp/cpp_antlr_src
mkdir /tmp/cpp_antlr_src
7z x /tmp/cpp_antlr_src.zip -o/tmp/cpp_antlr_src -y
rm -rf src/grammar/cpp/antlr4_runtime
cp -r /tmp/cpp_antlr_src/runtime/src src/grammar/cpp/antlr4_runtime
