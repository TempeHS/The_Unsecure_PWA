##############################################
# RE = RegExr = Regular Expressions          #
# Read the documentation and tutorials       #
# https://docs.python.org/3/library/re.html  #
# https://docs.python.org/3/howto/regex.html #
##############################################

import re
import html
import bcrypt

def simple_check_password(password):
    if not issubclass(type(password), str):
        return False
    if len(password) < 8:
        return False
    if len(password) > 20:
        return False
    if re.search(r'[ ]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    # Password is returned encoded so it can't be accidently logged in a human readable format
    return True

def check_password(password):
    if not issubclass(type(password), str):
        raise TypeError("Expected a string")
    if len(password) < 8:
        raise ValueError("less than 8 characters")
    if len(password) > 20:
        raise ValueError("more than 10 characters")
    if re.search(r'[ ]', password):
        raise ValueError("contains ' ' space characters")
    if not re.search(r'[A-Z]', password):
        raise ValueError("does not contain uppercase letters")
    if not re.search(r'[a-z]', password):
        raise ValueError("does not contain lowercase letters")
    if not re.search(r'[0-9]', password):
        raise ValueError("does not contain a digit '0123456789'")
    if not re.search(r"[@$!%*?&]", password):
        raise ValueError("does not contain one of '@$!%*?&' special characters")
    # Password is returned encoded so it can't be accidently logged in a human readable format
    return password.encode()

def make_web_safe(string):
    return html.escape(string)

def check_email(email): 
    if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
        return True
    else:
        return False

def validate_name(name): 
    # Check if the name is valid (only alphabets allowed).
    if not name.isalpha(): 
        return False 
    return True 

def validate_number(number): 
    # Check if the name is valid (only alphabets allowed).
    if number.isalpha(): 
        return False 
    return True 

def salt_and_hash(password):
    return # to be implemented
        