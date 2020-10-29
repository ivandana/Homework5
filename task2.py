from collections import Counter
import sys

ENGLISH_ALPHABET_COUNT = 26

INPUT_FILE = "book.txt"
OUTPUT_FILE = "summary.txt"
READ_MODE = 'r'
WRITE_MODE = 'w'

try:
    with open(INPUT_FILE, READ_MODE) as file:
        data = file.read()
except (OSError, IOError) as err:
    print(f"Error in reading from {INPUT_FILE} with error {err}.")
    sys.exit(0)
except Exception as error:
    print(f"Exception raised when reading from {INPUT_FILE} with error {error}.")
    sys.exit(0)

# Returns list of tuples containing unique alphabet as key and count as value.
results = Counter(data.lower())
try:
    # Will replace file and re-write if it already exists.
    output_file = open(OUTPUT_FILE, WRITE_MODE)
    with output_file:
        counter = 0
        for item in sorted(results.items()):
            if item[0].isalpha():  # Only consider alphabets, ignore other characters.
                counter += 1  # count number of unique alphabets
                output_file.write(f"{str(item[0]).capitalize()} {str(item[1])}\n")

        if counter == ENGLISH_ALPHABET_COUNT:
            output_file.write("\nIt has all letters.")
        else:
            output_file.write("\nIt doesn't have all letters.")
except (OSError, IOError) as err:
    print(f"Error in opening/writing to {OUTPUT_FILE} with error {err}.")
    sys.exit(0)