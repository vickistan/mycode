import hashlib
m = hashlib.md5()
m.update("Nobody inspects")
m.update(" the spammish repetition")
print m.digest()
print m.digest_size
print m.block_size
