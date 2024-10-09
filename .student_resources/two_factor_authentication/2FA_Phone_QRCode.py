#############################################################
# This program uses the Google Authenticator App            #
# Avialable in Google Play Store & Apple App Store          #
# Everytime you compile and run the code you need to update #
# the QRCode image and rescan the QRCode in the app         #
#############################################################

import pyotp  # pip install pyotp
import time
import qrcode # pip install qrcode

def gen_key():
    return pyotp.random_base32()

def gen_url(key):
    return pyotp.totp.TOTP(key).provisioning_uri(name="bob", issuer_name = '2fa App')

def verify_code(key: str, code: str):
    totp = pyotp.TOTP(key)
    return totp.verify(code)

key = gen_key()

totp = pyotp.TOTP(key)

uri = gen_url(key)

#print(uri)

qrcode.make(uri).save("newCode.png")

while True:
    #print(totp.verify(input("Enter code: ")))
    code = input("Enter code: ")
    print(verify_code(key, code))
