#!/usr/bin/env bash

PYTHON="/home/craig/qt-terminal-env/bin/python"
PYTHON_FILE="./src/python/Visualiser/Visualiser.py"


if [[ ! -x "${PYTHON}" ]];
then

    printf 'Error: Python interpreter not found: %s\n' "${PYTHON}" >&2

    exit 1

fi

if [[ ! -f "${PYTHON_FILE}" ]];
then

    printf 'Error: Python script not found: %s\n' "${PYTHON_FILE}" >&2

    exit 1

fi

exec "${PYTHON}" "${PYTHON_FILE}"
