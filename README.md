# python-demo
A demo for `unmock` in Python, comparing `unmock` to `pook`.

Test files for either are locared in the matching directory - `tests_unmock` and `tests_pook`. Test files have identical naming to allow for easier comparison between functionality.

## Running
1. pook test suite:  
`pytest tests_pook`
2. unmock test suite:  
`pytest tests_unmock`
3. unmock flag test:
`pytest tests_unmock/test_pytest_flag.py --unmock`

### Test files
1. `test_basic.py` - Compares basic calls and functionality to either library, how to provide a mocked response from a service.
1. `test_pytest.py` - Compares pytest integration and functionality.
1. `test_usability.py` - Compares the different "interesting" options for usability (i.e. checking mock status, controlling whitelists, using context managers, etc).
1. `test_pytest_flag.py` - For `unmock` only; as `unmock` supports pytest with a CLI flag as well (i.e. running `pytests ... --unmock`).

### Table comparison
