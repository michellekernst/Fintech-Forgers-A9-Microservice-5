    import time

    # names of the request and response files
    request_file = "math_request.txt"
    response_file = "math_response.txt"

    # create the files if they do not exist
    open(request_file, "a").close()
    open(response_file, "a").close()

    # keep checking the request file
    while True:
        try:
            # read the request
            with open(request_file) as f:
                request = f.read().strip()

            # only process the file if it has something in it
            if request:
                # split the request into the operation and numbers
                parts = request.split()

                # first item is the operation
                operation = parts[0]

                # everything after the operation is a number, add to array
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

                # clear the request file after processing it
                open(request_file, "w").close()

        # write any errors to the response file
        except Exception as e:
            with open(response_file, "w") as f:
                f.write(f"error: {e}")

        # wait a little before checking again
        time.sleep(0.1)