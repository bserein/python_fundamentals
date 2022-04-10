# Example of a custom module to be imported

# Core module
import re


def validate_email(email): # This function will validate an email address
    if len(email) > 7: # If the length of the email is greater than 7 characters (including the @ symbol)
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email)) # Return true if the email is valid and false if it's not
                             # The re.match function will return a match object if the email is valid and None if it's not