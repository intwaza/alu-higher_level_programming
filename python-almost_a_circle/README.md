# Almost a Circle - Tests

## Quick Start

```bash
# Run all tests
python3 run_tests.py

# Run specific tests
python3 run_tests.py base
python3 run_tests.py rectangle
python3 run_tests.py square
```

## Files
- `test_base.py` - Base class tests (28)
- `test_rectangle.py` - Rectangle tests (25)  
- `test_square.py` - Square tests (23)
- `run_tests.py` - Test runner

## Alternative Usage
```bash
python3 -m unittest test_base.py -v
python3 -m unittest discover -v
make test  # if Makefile available
```

**Total: 76 tests covering all functionality**