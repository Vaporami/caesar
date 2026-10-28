import pytest, caesar
@pytest.mark.parametrize("string, key, expected", [("Hello world!", 1, "Ifmmp!xpsme\""), (chr(255), 33, " "), (chr(0), -155, "e")])
def test_cipher(string, key, expected):
    assert caesar.cipher(string, key) == expected

@pytest.mark.parametrize("string, key, expected", [("Ifmmp!xpsme\"", 1, "Hello world!"), (" ", 33, chr(255)), ("e", -155, chr(0))])
def test_decipher(string, key, expected):
    assert caesar.decipher(string, key) == expected
