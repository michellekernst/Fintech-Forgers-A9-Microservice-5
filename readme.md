# Math Microservice

A simple Python microservice that performs math operations using `.txt` files as the communication pipeline.

## How It Works

The service watches the file `math_request.txt` and writes the result to `math_response.txt`.

## Files

The microservice uses `math_microservice.py` as well as `math_helper.py` to import helper functions to more easily call the microservice.

The `.txt` files are created automatically if they do not exist.

## Using the Helper Functions

Instead of manually writing to the request file, you can use `math_helper.py`.

```python
from math_client import calculate

print(calculate("add", 10, 20, 30))
print(calculate("sub", 100, 20, 5))
print(calculate("mul", 2, 3, 4))
print(calculate("div", 100, 2, 5))
```

Output:

```text
60.0
75.0
24.0
10.0
```

## Supported Operations

### Addition

```python
calculate("add", 10, 20, 30)
```

Result:

```text
60.0
```

### Subtraction

```python
calculate("sub", 100, 20, 5)
```

Result:

```text
75.0
```

### Multiplication

```python
calculate("mul", 2, 3, 4)
```

Result:

```text
24.0
```

### Division

```python
calculate("div", 100, 2, 5)
```

Result:

```text
10.0
```

## Manual Requests

You can also use the request file directly.

Put this in `math_request.txt`:

```text
add 10 20 30
```

The service will write the result to `math_response.txt`:

```text
60.0
```

After processing the request, the service clears `math_request.txt`. It is recommended your main program clears `math_response.txt` after reading it to avoid reading the wrong response with later operations.

## Changing the File Names

The file names can be changed at the top of both Python files:

```python
request_file = "math_request.txt"
response_file = "math_response.txt"
```

Make sure both files (the microservice and helper functions) use the same names.