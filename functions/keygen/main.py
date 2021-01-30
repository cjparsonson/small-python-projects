import string
import secrets


def keygen(parts=4, chars_per_part=8):
    """ Returns a random pass key in format xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx
     defaults to 4 parts of 8 characters if not specified.
     Utilizes upper case characters and digits only."""
    alphabet = string.ascii_uppercase + string.digits
    pass_key = [''.join(secrets.choice(alphabet) for i in range(chars_per_part)) for x in range(parts)]
    return '-'.join(pass_key)





