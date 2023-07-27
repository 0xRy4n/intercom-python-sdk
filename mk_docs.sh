#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pdoc --html "$SCRIPT_DIR/intercom_python_sdk" -o "$SCRIPT_DIR/docs" --force