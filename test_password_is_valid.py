import pytest
import re
from password_checker import password_is_valid

def test_password_is_valid():

    with pytest.raises(Exception):
        assert password_is_valid('') == Exception('password should exist')
        assert password_is_valid('tttdgjgjjhehjxdgj') == Exception('Password must have a minimum of 8 characters')
        assert password_is_valid('FTJTTJD57I9ETUGJ') == Exception('Password must have atleast one lowercase letter')
        assert password_is_valid('fdhdfhdfhhfdfhdfhdfh') == Exception('Password must have atleast one uppercase letter')
        assert password_is_valid('45tr7678sftfg') == Exception('Password must have atleast one digit')
        assert password_is_valid('45e45#$%^&&*(#$dxf)') == Exception('Password must have atleast one special character')


