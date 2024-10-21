###########################################################################
# Beginner code snippets, the bcrypt library has a range of other methods #
# https://pypi.org/project/bcrypt/                                        #
###########################################################################

import bcrypt

# Plain text password
my_password = "I Am All The Jedi"

# UTF-8 is the default Python chaarcter set
my_encoded_password = my_password.encode()

# Salt to add to password before Hashing
salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

# Hashed Password
hashed_password = bcrypt.hashpw(password=my_encoded_password, salt=salt)

print(f"How actual password will appear in logs etc: {my_encoded_password.hex()}")

# Python print statement will decode it but if the variable is logged, it will be logged as a string of bytes
print(f"Actual Password: {my_encoded_password.decode()}")

# Print Hashed Password
print(f"Hashed Password: {hashed_password.decode()}")

# Check if a plain text password matches a hashed password. It returns a Boolean value.
print(f"Are they the same password: {bcrypt.checkpw(my_encoded_password, hashed_password)}")
