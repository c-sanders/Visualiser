#!/bin/bash

# Exit on errors, undefined variables and failed pipeline commands.

set -euo pipefail

# Define the directory containing the UML diagrams.

UML_DIR="./images/UML_class_diagrams"

# Create the output directory if it doesn't already exist.

mkdir -p "$UML_DIR"

# Find the Python source files.

declare -a FILES
declare -i counter

mapfile -d '' FILES < <(
    find ./ \
        -type d -path "./src/python/Visualiser/old" -prune -o \
        -type f \
        ! -path "./src/python/Visualiser/Visualiser.py" \
        -type f \
        ! -path "./src/python/PlotGenerators/QuaternionRotation/docs/conf.py" \
        -type f \
        ! -path "./src/python/PlotGenerators/QuaternionRotation/python/quaternion_rotation_over_unit_sphere.py" \
        -type f \
        ! -path "./src/python/PlotGenerators/QuaternionRotation/python/Utils.py" \
        -name "*.py" \
        -print0
)

# Report the number of files found.

printf "\n"
printf "Number of Python files found: %d\n" "${#FILES[@]}"
printf "\n"
read -p "Press Enter to continue..."
printf "\n"

for filename in "${FILES[@]}"
do

  echo ${filename}

done

printf "\n"
read -p "Press Enter to continue..."
printf "\n"

# Process each Python file.

counter=0

for filename in "${FILES[@]}"
do

  ((++counter))

  # Extract the Python module/class name.

  classname=$(basename "$filename" .py)

  printf "========================================\n"
  printf "File number: %d of %d\n" $counter "${#FILES[@]}"
  printf "========================================\n"
  printf "Processing: %s\n" "$filename"
  printf "Class name: %s\n" "$classname"
  printf "========================================\n"

  # Generate the UML class diagram.

  pyreverse \
    --init-hook='import sys; sys.setrecursionlimit(3000)' \
    -o html \
    -c "$classname" \
    --output-directory="$UML_DIR" \
    "$filename"

done

printf "\nUML diagram generation completed.\n"

exit 0
