Basic key generator function for use in larger projects.

This version supports upper case ascii characters and digits 0-9.

Based on the Python secrets module to ensure better randomization.

Output xxxxxxxx-xxxxxxxx-xxxxxxx-xxxxxxxx

# Examples 

Generate the default 8 character per section, 4 section password.

'''
keygen()
'''

Generate a customized password.

'''
keygen(3, 5)
'''

Will output: xxxxx-xxxxx-xxxxx