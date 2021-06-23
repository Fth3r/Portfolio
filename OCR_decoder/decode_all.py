# a program to test all of the decoding modules thus far

import affine, atbash, b64, caesar

message = "This is my super secret message!"

cz = caesar.encode_cz(message)
base = b64.encode_b64(message)
atb = atbash.find_atb(message)
aff = affine.encode_aff(message)

if __name__ == "__main__":
    print(cz)
    print(base)
    print(atb)
    print(aff)

    print("Caesar: ", caesar.decode_cz(cz))
    print("Base64: ", b64.decode_b64(base))
    print("Atbash: ", atbash.find_atb(atb))
    print("Affine: ", affine.decode_aff(aff))