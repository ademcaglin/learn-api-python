import unittest
import mock
from src.user_repository import get_user
from src.dal import get
from src.reverse_word import reverse_word

class TestStringMethods(unittest.TestCase):
    @mock.patch("src.user_repository.get", mock.MagicMock(return_value="TEST"))
    def test_upper(self):
        self.assertEqual(get_user(5), 'TEST')
    def test_reverse_word(self):
        self.assertEqual(reverse_word("mcvn.vcvg"), 'vcvg.mcvn')