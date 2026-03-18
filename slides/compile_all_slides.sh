#!/bin/bash
# Compile all lecture slides using cdl-slides (pip install cdl-slides)
# Produces HTML and PDF for each lecture*.md found in week*/ directories

SLIDES_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_FILE="$SLIDES_DIR/compilation_report.txt"

# Verify cdl-slides is installed
if ! command -v cdl-slides &> /dev/null; then
    echo "ERROR: cdl-slides not found. Install with: pip install cdl-slides"
    exit 1
fi

echo "Compilation Report - $(date)" > "$OUTPUT_FILE"
echo "======================================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

TOTAL=0
SUCCESS=0
FAILED=0

for md_file in "$SLIDES_DIR"/week*/lecture*.md; do
    [ -f "$md_file" ] || continue
    TOTAL=$((TOTAL + 1))
    dir=$(dirname "$md_file")
    base=$(basename "$md_file")

    echo "Compiling: $md_file"
    echo "" >> "$OUTPUT_FILE"
    echo "File: $md_file" >> "$OUTPUT_FILE"
    echo "---" >> "$OUTPUT_FILE"

    cd "$dir"
    if cdl-slides compile "$base" 2>> "$OUTPUT_FILE"; then
        echo "  ✓ Success" >> "$OUTPUT_FILE"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "  ✗ FAILED" >> "$OUTPUT_FILE"
        FAILED=$((FAILED + 1))
    fi
    cd - > /dev/null
done

echo "" >> "$OUTPUT_FILE"
echo "======================================" >> "$OUTPUT_FILE"
echo "Total: $TOTAL | Success: $SUCCESS | Failed: $FAILED" >> "$OUTPUT_FILE"

echo ""
echo "Compilation complete! Report saved to: $OUTPUT_FILE"
echo "Total: $TOTAL | Success: $SUCCESS | Failed: $FAILED"

if [ "$FAILED" -gt 0 ]; then
    echo ""
    echo "FAILURES:"
    grep -B1 "FAILED" "$OUTPUT_FILE"
    exit 1
fi
