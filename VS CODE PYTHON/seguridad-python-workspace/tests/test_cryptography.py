import unittest
from FontCode import _cryptography

class TestCryptography(unittest.TestCase):

    def setUp(self):
        pass

    def test_encrypt_decrypt(self):
        original_text = "This is a test"
        encrypted_text = _cryptography.encrypt(original_text)
        decrypted_text = _cryptography.decrypt(encrypted_text)

        self.assertEqual(original_text, decrypted_text)

    def test_encrypt(self):
        original_text = "This is a test"
        encrypted_text = _cryptography.encrypt(original_text)

        self.assertNotEqual(original_text, encrypted_text)

    def test_decrypt(self):
        original_text = "This is a test"
        encrypted_text = _cryptography.encrypt(original_text)
        decrypted_text = _cryptography.decrypt(encrypted_text)

        self.assertNotEqual(encrypted_text, decrypted_text)

if __name__ == '__main__':
    unittest.main()