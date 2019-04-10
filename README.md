# python-demo
A demo for `unmock` in Python, comparing `unmock` to `pook`.

Test files for either are locared in the matching directory - `tests_unmock` and `tests_pook`. Test files have identical naming to allow for easier comparison between functionality.

## Running
1. pook test suite: `pytest tests_pook`  
2. unmock test suite: `pytest tests_unmock`  
3. unmock flag test: `pytest tests_unmock/test_pytest_flag.py --unmock`  
4. Flask demo: `pytest webdev/test_flask.py`  
(Change mocking suite via in-file flag `TEST_MODE` to `None`, `"unmock"` or `"pook"`).

### Test files
1. `test_basic.py` - Compares basic calls and functionality to either library, how to provide a mocked response from a service.
1. `test_pytest.py` - Compares pytest integration and functionality.
1. `test_usability.py` - Compares the different "interesting" options for usability (i.e. checking mock status, controlling whitelists, using context managers, etc).
1. `test_pytest_flag.py` - For `unmock` only; as `unmock` supports pytest with a CLI flag as well (i.e. running `pytests ... --unmock`).

### Table comparison
###### The table ignores current malfunctions in `pook` (such as `off` not working or the whitelisting capabilities).

|Description|pook|unmock|
|-----------|----|------|
|Automatic mocks|| :heavy_check_mark: |
|Python 3.7 support|| :heavy_check_mark: |
|Support for `requests` library| :heavy_check_mark: | :heavy_check_mark: |
|Support for `urllib3` library| :heavy_check_mark: | :heavy_check_mark: |
|Support for `http.client` library| :heavy_check_mark: | :heavy_check_mark: |
|Support for `aiohttp` library| :heavy_check_mark: ||
|On missing mock|raises Exception|returns error response from requested host|
|Whitelisting URLs| :white_check_mark: (need to specify specific endpoints, query parameters and method used) | :heavy_check_mark:|
|Persistent mocks| :white_check_mark: (only if specified, otherwise one-off by default, or N-times if set) | :heavy_check_mark: |
|Access to mocked responses| :heavy_check_mark: (manually written by the user) | :heavy_check_mark: saved locally on file system|
|Speed| :heavy_check_mark: (instant, no HTTP request actually made) | :heavy_check_mark: simulates real access to actual end point (as a request is made via unmock cloud)|
|pytest integration| :white_check_mark: (only through decorators with limited functionality) | :heavy_check_mark: (with fixtures and plugin extension)|
