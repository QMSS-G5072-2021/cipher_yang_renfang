from cipher_ry2403 import cipher_ry2403 
import pytest 

def test_cipher_single():
    example = 'test'
    expected = 'vguv'
    actual = cipher_ry2403.cipher(example,2,True)
    assert actual == expected,'not works for a single word'
