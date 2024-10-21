import data_handler as sanitiser
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='security_log.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

if __name__ == '__main__':
    print (f"Does 'password' meet security requirements: {sanitiser.simple_check_password("password")}" )
    print (f"Make <HTML> web safe: {sanitiser.make_web_safe('<html>')}")
    print (f"Is 'name@example.com' an email address: {sanitiser.check_email('name@example.com')}")
    print (f"Is '123!' an name: {sanitiser.validate_name('123!')}")
    print (f"Is '1234567890' a number: {sanitiser.validate_number('1234567890')}")
    print ("--PYTHONIC EXCEPTION HANDLING--")

#################################################################
# Improved password checking with Pythonic exception handling   #
# & conversion to a byte string for privacy                     #
# Documentation: https://docs.python.org/3/tutorial/errors.html #
# Note: the password as been stored as a variable to make it    #
# easy for you to test the code. It is best pratice to pass the #
# date on entry to be validated first before storing.           #
#################################################################

    #password = "!1234abcD&"
    password = 123
    try:
        print (f"The password as the byte string : {sanitiser.check_password(password).hex()} is ready to be encryted" )
    except TypeError:
        logger.error(f"Type errors for password:{password}")
        print("TypeError has been logged")
    except ValueError as inst:
        print(f"Not a valid password because it has {inst.args}.")
    except Exception as inst:
        print(f"Log as a {type(inst)}")