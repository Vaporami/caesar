import pytest, vigenere
@pytest.mark.parametrize("string, key, expected", [("Hello world!", "\n", "Rovvy*\x81y|vn+"), (chr(255), "\n", chr(9))])
def test_cipher(string, key, expected):
    assert vigenere.cipher(string, key) == expected

@pytest.mark.parametrize("string, key, expected", [("Rovvy*\x81y|vn+", "\n", "Hello world!"), (chr(9), "\n", chr(255))])
def test_decipher(string, key, expected):
    assert vigenere.decipher(string, key) == expected
