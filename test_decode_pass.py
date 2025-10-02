import unittest
import base64
import os
from decode_pass import decode_password

class TestDecodePass(unittest.TestCase):
    def setUp(self):
        self.test_pwd = 'UnitTest123!'
        self.b64_pwd = base64.b64encode(self.test_pwd.encode()).decode()
        self.b64_file = 'unittest_b64.txt'
        with open(self.b64_file, 'w') as f:
            f.write(self.b64_pwd)

    def tearDown(self):
        if os.path.exists(self.b64_file):
            os.remove(self.b64_file)

    def test_decode_password(self):
        # Capture output
        import io
        import sys
        captured = io.StringIO()
        sys.stdout = captured
        decode_password(self.b64_file)
        sys.stdout = sys.__stdout__
        self.assertIn(self.test_pwd, captured.getvalue())

if __name__ == '__main__':
    unittest.main()
