import pytest
import re
from password_checker import password_is_ok

def test_password_is_ok():
    assert password_is_ok('') == False
    assert password_is_ok('on') == False
    assert password_is_ok('FTJTTJD57I9ETUGJ') == True
