import time

# names of the request and response files
request_file = "math_request.txt"
response_file = "math_response.txt"


def calculate(operation, *numbers):
    # clear the old response
    open(response_file, "w").close()

    # format the request
    request = operation + " " + " ".join(str(number) for number in numbers)

    # send the request
    with open(request_file, "w") as f:
        f.write(request)

    # wait for a new response
    while True:
        with open(response_file) as f:
            response = f.read().strip()

        if response:
            return response

        time.sleep(0.1)