 #! /usr/bin/python3

import base64

def encode_b64(cleartext):
    cleartext_bytes = cleartext.encode("ascii")

    encoded_bytes = base64.b64encode(cleartext_bytes)
    encoded = encoded_bytes.decode("ascii")

    return encoded

def decode_b64(encoded):
    encoded_bytes = encoded.encode("ascii")

    cleartext_bytes = base64.b64decode(encoded_bytes)
    cleartext = cleartext_bytes.decode("ascii")

    return cleartext

