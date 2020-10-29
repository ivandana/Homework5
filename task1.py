INPUT_FILE = "scores.txt"
OUTPUT_FILE = "log.txt"
READ_MODE = "r"
WRITE_MODE = "w"

total =  0
count_student = 0
average_score = 0

try:
    rfile = open(INPUT_FILE, READ_MODE) 
    wfile = open(OUTPUT_FILE, WRITE_MODE)
    with rfile, wfile:
        for line in rfile:
            if line.isspace(): #if line is just a blank line
                continue
            text_content = line.rstrip('\n')
            name, scores = None, None
            try:
                name, scores = text_content.split(' ')
            except ValueError as e: # in cases where line just has one string.
                print (f'Unpacking {text_content} failed with error {e}')
                wfile.write(f"Bad score value for {text_content} ignored.\n")
            else:
                if not scores.isdigit():
                    wfile.write(f"Bad score value for {name} ignored.\n")
                else:
                    total = total + int(scores)
                    count_student += 1
                    average_score = int(total/count_student)
        wfile.write(f"\nThe class average is {str(average_score)} for {str(count_student)} students.")
except (OSError, IOError) as err:
    print(f"Error in reading from {INPUT_FILE} or {OUTPUT_FILE} with error {err}.")
except Exception as error:
    print(f"Exception raised when reading from {INPUT_FILE} or {OUTPUT_FILE } with error {error}.")
