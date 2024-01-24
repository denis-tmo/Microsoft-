"""
Check the validity of password input by users
"""

import re

"""
Check if password is valid anr return True, False otherwise
"""
def is_valid_password(password):

    # Assume the password is invalid
    valid = False
    while not valid:  
        # At least one lowercase letter
        if not re.search("[a-z]", password):
            break
        # At least one digit
        elif not re.search("[0-9]", password):
            break
        # At least one uppercase letter
        elif not re.search("[A-Z]", password):
            break
        # At least one special character '$', '#' or '@'
        elif not re.search("[$#@]", password):
            break
        # Length should be between 6 and 12 characters
        elif (len(password) < 6 or len(password) > 12):
            break
        else:
            # All conditions are met, set 'valid' to True
            valid = True
            break

    return valid

password = 'asqwr@,aF#,wE*,We'
# If 'valid' remains True, print "Not a Valid Password"
valid = is_valid_password(password)
print(f'valid = {valid}')
