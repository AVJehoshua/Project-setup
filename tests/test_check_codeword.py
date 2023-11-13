from lib.check_codeword import *

def test_if_codeword_is_correct():
    result = check_codeword("Absurd")
    assert result() == "Welcome to the Absurd Vault"

def test_if_codeword_is_close():
    result = check_codeword("And")
    assert result == "Close, try again"

def test_if_codeword_is_wrong():
    result = check_codeword("pizza")
    assert result == "You may not enter."

