import pytest
import source.service as service
import unittest.mock as mock



 
# def test_get_user(mock_get_user_id):
#     mock_get_user_id.return_value = "Mocked Abhishek"
#     user_name = service.get_user_id(1)

#     assert user_name == "Mocked Abhishek"



import pytest
import requests
import unittest.mock as mock
from source.service import get_user  # adjust path as needed

@mock.patch("source.service.requests.get")  # 👈 patch where it's used, not where it's from
def test_get_user_success(mock_get):
    # 1. Create a mock response object
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Abhishek"}]
    
    # 2. Assign mock response to requests.get
    mock_get.return_value = mock_response

    # 3. Call the actual function (which is now using the mock)
    result = get_user()

    # 4. Assert
    assert result == [{"id": 1, "name": "Abhishek"}]
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users")


"""
| Line                                         | What's Happening                                              |
| -------------------------------------------- | ------------------------------------------------------------- |
| `@mock.patch("source.service.requests.get")` | Replaces `requests.get` with a mock, only inside `get_user()` |
| `mock_response = mock.Mock()`                | Create a fake response object                                 |
| `mock_response.status_code = 200`            | Simulate a successful HTTP call                               |
| `mock_response.json.return_value = [...]`    | Simulate JSON content from the API                            |
| `mock_get.return_value = mock_response`      | When `requests.get` is called, return this fake response      |
| `result = get_user()`                        | Call your real function — now using mocked `requests.get()`   |
| `assert result == ...`                       | Ensure your function handles the response correctly           |
| `mock_get.assert_called_once_with(...)`      | Optional: Confirm correct URL was used                        |

"""

##### Important ---> ✅ Rule of Mocking: Patch "where it is used, not where it is defined."

@mock.patch("source.service.requests.get")
def test_get_user_error(mock_get):
    # Simulate failed response
    mock_response = mock.Mock()
    mock_response.status_code = 404  # ❌ not 200
    mock_get.return_value = mock_response

    # Now test that the function raises HTTPError
    with pytest.raises(requests.HTTPError):
        get_user()