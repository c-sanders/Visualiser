#!/bin/bash


# Exit on errors, undefined variables and failed pipeline commands.

set -euo pipefail


echo $0
echo $1

# Check usage.

if [[ $# -lt 1 ]]; then

  printf "Usage: %s file.py [file2.py ...]\n" "$(basename "$0")" >&2
  exit 1

else

  printf "The correct number of command line args were passed to this script.\n"

fi

# Define the directory containing the UML diagrams.

UML_DIR="./images/UML_class_diagrams"

# Create the output directory if it doesn't already exist.

mkdir -p "$UML_DIR"

# Take the files from the command line, checking each one.

declare -a FILES=()
declare -i counter


printf "\n"
printf "About to process command line args\n"
printf "$@\n"

arg=$1

printf "arg = %s\n" $arg

for arg in "$@"
do
  if [[ ! -f "$arg" ]]; then
    printf "Error: '%s' is not a file.\n" "$arg" >&2
    exit 1
  fi
  if [[ "$arg" != *.py ]]; then
    printf "Error: '%s' is not a Python (.py) file.\n" "$arg" >&2
    exit 1
  fi
  FILES+=("$arg")
done

printf "\nNumber of Python files to process: %d\n" "${#FILES[@]}"

# Process each Python file.

counter=0

for filename in "${FILES[@]}"
do

    ((++counter))

    # Extract the Python module/class name.

    classname=$(basename "$filename" .py)

    # printf "========================================\n"
    # printf "File number: %d of %d\n" "$counter" "${#FILES[@]}"
    printf "========================================\n"
    printf "Processing: %s\n" "$filename"
    printf "Class name: %s\n" "$classname"
    printf "========================================\n"

    # Generate the UML class diagram.

    # pyreverse \
    #   -o html \
    #   -c "$classname" \
    #   --output-directory="$UML_DIR" \
    #   "$filename"

    pyreverse -o html \
              "$filename"

    if [[ -f "classes.html" ]]; then

        destfile="${UML_DIR}/${classname}.html"

        echo "File exists : classes.html"
        echo ${destfile}

        mv -vf classes.html ${destfile}

    else

        exit 1

    fi

    printf "UML diagram generation completed.\n"

done


exit 0