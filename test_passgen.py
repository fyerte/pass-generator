import unittest
import base64
import string
from passgen import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        pwd = generate_password(10, False)
        self.assertEqual(len(pwd), 10)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in pwd))

    def test_custom_length(self):
        pwd = generate_password(20, False)
        self.assertEqual(len(pwd), 20)

    def test_special_chars_percentage(self):
        length = 20
        pwd = generate_password(length, True)
        specials = set('!@#$%^&*()-_=+[]{}|;:,.<>?/')
        special_count = sum(1 for c in pwd if c in specials)
        self.assertGreaterEqual(special_count, int(length * 0.10))
        self.assertLessEqual(special_count, int(length * 0.20))

    def test_base64_encoding(self):
        pwd = 'TestPassword123!'
        encoded = base64.b64encode(pwd.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        self.assertEqual(pwd, decoded)

if __name__ == '__main__':
    unittest.main()
