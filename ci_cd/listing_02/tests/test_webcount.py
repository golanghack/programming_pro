from unittest.mock import Mock, patch
from webcount import most_common_word_in_web_page

def test_with_patch():
    mock_req = Mock()
    mock_req.get.return_value.text = 'xx yyy zzzz'
    with patch('webcount.webcount.requests', mock_req):
        result = most_common_word_in_web_page(
            ['x', 'y', 'z'], 'https://google.com',
        )
    assert result == 'z', 'function with test'
    assert mock_req.get.call_count == 1
    assert mock_req.get.call_args[0][0] == 'https://google.com', 'correct url'