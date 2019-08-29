import unittest
import mock
#from src.user_repository import get_user
#from src.dal import get
from src.utils.algorithms import reverse_words, pow_mod, is_prime


class TestStringMethods(unittest.TestCase):
    # @mock.patch("src.user_repository.get", mock.MagicMock(return_value="TEST"))
    # def test_upper(self):
    #    self.assertEqual(get_user(5), 'TEST')
    def test_reverse_word(self):
        self.assertEqual(reverse_words("mcvn.vcvg"), 'vcvg.mcvn')

    def test_pow_mod(self):
        self.assertEqual(pow_mod(125, 140, 141), 115)

    def test_is_prime(self):
        self.assertEqual(is_prime(7051), True) 
