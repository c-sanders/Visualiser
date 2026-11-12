#! /bin/bash

PYTHON="/home/craig/local/source_code/python/sine_wave/venv/bin/python"
PYTHON_FILE="./python/quaternion_rotation_over_unit_sphere.py"

LOGGING_LEVEL=10


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

exec "${PYTHON}" "${PYTHON_FILE}" "${LOGGING_LEVEL}" "False" "rotation" "0.577350" "0.577350" "0.577350" "720" "1" "0" "0"
