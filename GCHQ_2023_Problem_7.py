#!/usr/bin/env python3

'''
Script:     GCHQ_2023_Problem_7.py
Author:     Jeff VanSickle
Created:    20231214

Script outputs the deciphered statements from Question 7 of the GCHQ
Christmas Challenge 2023. Cipher alphabet was derived by hand on my
whiteboard.
'''

import string

reg_alphabet = string.ascii_uppercase
cipher_alphabet = 'FNAOD*ILB*RSECHKT*U*VW*YM*'

enciphered_stmts = ["Agklq ldhum qom ndem.", "Gembqgax c 4-hmqqmk vdke.", "Hddp mumkxvomkm.", "Ycxim gq'l umkx diugdsl."]

for stmt in enciphered_stmts:
    deciphered_stmt = ''
    for stmt_char in stmt.upper():
        # Punctuation won't be found. Avoid -1 printing * for these.
        translatable_char_pos = reg_alphabet.find(stmt_char)

        if translatable_char_pos != -1:
            deciphered_stmt += cipher_alphabet[translatable_char_pos]
        else:
            deciphered_stmt += stmt_char

    # Output the hidden message(s)!
    print(deciphered_stmt)
