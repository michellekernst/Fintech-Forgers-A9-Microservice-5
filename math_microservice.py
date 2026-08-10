import time
import os

# names of the request and response files
request_file = "math_request.txt"
response_file = "math_response.txt"

# stores the last time the request file was processed
last_modified = 0

# create the files if they do not exist
open(request_file, "a").close()
open(response_file, "a").close()

# keep checking the request file
while True:
    try:
        # check if request file has data
        if request_file and open(request_file).read().strip():

            # check when the request file was last changed
            current_modified = os.path.getmtime(request_file)

            # only process if the file has changed
            if current_modified != last_modified:

                # remember this file change
                last_modified = current_modified

                # read the request
                with open(request_file) as f:
                    request = f.read().strip()

                # split the request
                parts = request.split()

                # first item is the operation
                operation = parts[0]

                # everything after the operation is a number
                numbers = [float(x) for x in parts[1:]]

                # perform the requested operation
                if operation == "add":
                    result = sum(numbers)

                elif operation == "sub":
                    result = numbers[0]

                    for number in numbers[1:]:
                        result -= number

                elif operation == "mul":
                    result = 1

                    for number in numbers:
                        result *= number

                elif operation == "div":
                    result = numbers[0]

                    for number in numbers[1:]:
                        result /= number

                else:
                    result = "unknown operation"

                # write the result to the response file
                with open(response_file, "w") as f:
                    f.write(str(result))

    except Exception as e:
        with open(response_file, "w") as f:
            f.write(f"error: {e}")

    # wait before checking again
    time.sleep(0.1)
