#! /usr/bin/python

from Crypto.Cipher import AES
import base64
import os, random


def encryption(privateInfo):
	privateInfo = 'This is just a string'
	BLOCK_SIZE = 16
	PADDING = '{'

	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

	secret = os.urandom(BLOCK_SIZE)
	print 'encryption key: ', secret

	cipher = AES.new(secret)

	encoded = EncodeAES(cipher, privateInfo)

	print 'Encrypted string:', encoded
