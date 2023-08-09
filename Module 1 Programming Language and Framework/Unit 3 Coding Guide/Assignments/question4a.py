'''
Create a function that validates email addresses based on following set of rules:
- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. Make sure
there are no no disposable email providers such as yopmail.
Write unit tests to validate different email addresses against the rules, including valid and
invalid addresses (Use unittest module).

'''
import re


def validate_email_address(email_address: str) -> bool:
    """This function takes in email address and validates that email
    address based on the presence of "@", no space in the address and
    vaalid email providers such as yahoo, gmail and outlook.

    Args:
        email_address (str): email address to be validates

    Returns:
        bool: True if email address is valid else False
    """
    valid_providers = ['yahoo', 'gmail', 'outlook']
    email_format = r'^[a-zA-Z0-9._%+-]+@[a-ZA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_address, email_format):
        return False

    domain = email_address.split("@")[1].lower()

    if 'yopmail' in domain:
        return False
    
    if any(provider in domain for provider in valid_providers):
        return True
    
    return False


