from unittest.mock import Mock, patch
from webcount import most_common_word_in_web_page

def test_with_patch():
    mock_req = Mock()
    mock_req.get.return_value.text = 'aa bbb c'
    with patch('webcount.webcount.requests', mock_req):
        result = most_common_word_in_web_page(
            ['a', 'b', 'c'], 'https://python.org'
        )
    assert result == 'a', 'function with test'

def test_fake_client():
    class TestResponse():
        text = 'xx yyy, zzzz'

    class TestUserAgent():
        def get(self, url):
            return TestResponse()

    result = most_common_word_in_web_page(
    words=['the', 'google'],
    target_url='https://google.com',
    user_agent=TestUserAgent()
    )
    assert result == 'google', 'testing with fake client'