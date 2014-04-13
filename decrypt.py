from __future__ import print_function

import binascii
import json
import subprocess

from Crypto.Cipher import AES

ctRaw = subprocess.check_output(["node", "encrypt.js"])
print("[decrypt.py] Ciphertext:", ctRaw)

ctJSON = json.loads(ctRaw)
iv = binascii.a2b_base64(ctJSON["iv"])

# TODO: Trim IV semantically.
iv = iv[0:13]

ct = binascii.a2b_base64(ctJSON["ct"])
print("[decrypt.py] IV length:", len(iv))
print("[decrypt.py] IV:", iv.encode("hex"))

tag_num_bytes = ctJSON["ts"] / 8
print("[decrypt.py] Tag size (bytes):", tag_num_bytes)
tag = ct[-tag_num_bytes:]
print("[decrypt.py] Tag:", tag.encode("hex"))

key = "\x00"*16
cipher = AES.new(key, AES.MODE_CCM, iv[0:13])
plaintext = cipher.decrypt_and_verify(ct[:-tag_num_bytes], tag)
print("[decrypt.py] Plaintext:", plaintext)
