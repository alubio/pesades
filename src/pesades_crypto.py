# -*- coding: utf-8 -*-
"""
PESADES specific crypto functions.
"""

import hashlib
import os
import base64

initialized = False

def initialize():
    """Initilize PESADES crypto engine"""
    if not crypto_initialized:
        crypto_initialized = True

def is_weakpassword(password):
    """Check if a password is weak"""
    from re import search
    while True:   
        if (len(password)<11): 
            flag = -1
            break
        elif not search("[a-z]", password): 
            flag = -1
            break
        elif not search("[A-Z]", password): 
            flag = -1
            break
        elif not search("[0-9]", password): 
            flag = -1
            break
        elif not search("[-_@$.,*#]", password): 
            flag = -1
            break
        else: 
            flag = 0
            break
    if flag ==-1:
        return True
    else:
        return False

def is_weakpassword_dummy(password):
    """Check if a password is weak"""
    from re import search
    while True:   
        # TODO if (len(password)<11): 
            #flag = -1
            #break
        if not search("[a-z]", password): 
            flag = -1
            break
        elif not search("[A-Z]", password): 
            flag = -1
            break
        elif not search("[0-9]", password): 
            flag = -1
            break
        # TODO elif not search("[-_@$.,*#]", password): 
            #flag = -1
            #break
        else: 
            flag = 0
            break
    if flag ==-1:
        return True
    else:
        return False

def get_hashedpassword(password):
    """Get the hash, in BASE64 format, of a password with salt"""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
    bytehash = salt + key
    b64genhash = base64.b64encode(bytehash)
    return b64genhash.decode('utf-8')

def is_passwordok(password, hash):
    """Compare password with hash"""
    bytehash = base64.b64decode(hash)
    salt = bytehash[:32]
    key = bytehash[32:]
    genkey = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
    return key == genkey
