#!/usr/bin/env bash

# Find the installed path of torch
TORCH_PATH=$(python -c "import os; import torch; print(os.path.dirname(torch.__file__))")

# Check if the torch path was found
if [ -z "$TORCH_PATH" ]; then
    echo "Torch is not installed or not found."
    exit 1
fi

# Define the input pickle file and output HTML file
INPUT_PICKLE_FILE="$1"
OUTPUT_HTML_FILE="${INPUT_PICKLE_FILE%.pickle}.html"

# Check if the input pickle file is provided
if [ -z "$INPUT_PICKLE_FILE" ]; then
    echo "Usage: $0 <path_to_snapshot.pickle>"
    exit 1
fi

# Run the conversion command
python "$TORCH_PATH/cuda/_memory_viz.py" trace_plot "$INPUT_PICKLE_FILE" -o "$OUTPUT_HTML_FILE"

# Check if the conversion was successful
if [ $? -eq 0 ]; then
    echo "Conversion successful. Output HTML file: $OUTPUT_HTML_FILE"
else
    echo "Conversion failed."
    exit 1
fi
