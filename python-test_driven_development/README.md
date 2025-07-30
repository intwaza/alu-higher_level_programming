# Python Test Driven Development

This project contains Python functions with comprehensive testing using doctest and unittest.

## Files

- `0-add_integer.py` - Adds two integers
- `2-matrix_divided.py` - Divides all elements of a matrix  
- `3-say_my_name.py` - Prints a person's name
- `4-print_square.py` - Prints a square with # characters
- `5-text_indentation.py` - Formats text with indentation
- `6-max_integer.py` - Finds maximum integer in a list

## Testing

Run doctests:
```bash
python3 -m doctest -v ./tests/0-add_integer.txt
python3 -m doctest -v ./tests/2-matrix_divided.txt
python3 -m doctest -v ./tests/3-say_my_name.txt
python3 -m doctest -v ./tests/4-print_square.txt
python3 -m doctest -v ./tests/5-text_indentation.txt
```

Run unittests:
```bash
python3 -m unittest tests.6-max_integer_test
```

## Usage

```python
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
print(add_integer(1, 2))  # Output: 3
```