import re

def password_is_valid(password):
    #1. Password should exist
    if len(password) == 0:
        raise Exception("Password does not exist")
        
    #2. Password should be longer than 8 charactersitics 
    elif (len(password)<8):
        raise Exception("Password must have a minimum of 8 characters")

    #3. Password should have at least one lowercase letter
    elif not re.search("[a-z]",password):
        raise Exception("Password must have atleast one lowercase letter")

    #4.	password should have at least one uppercase letter
    elif not re.search("[A-Z]",password):
        raise Exception("Password must have atleast one uppercase letter")

    #5.	password should at least have one digit
    elif not re.search("[0-9]",password):
        raise Exception("Password must have atleast one digit")

    #6.	password should have at least one special character
    elif not re.search("[!@#$%^&*]",password):
        raise Exception("Password must have atleast one special character")

    
    else:
         print("password is valid")

password_is_valid

# password_is_ok function

def password_is_ok(password):
    if len(password) <= 8:
        return False
    else:
        if re.search('[a-z]', password):
            return True
        elif re.search('[A-Z]', password):
            return True
        elif re.search('[0-9]', password):
            return True
        else:
            return False

password_is_ok