from pwn import *
io = remote("helsectf2024-2da207d37b091b1b4dff-joppe2.chals.io", 443, ssl=True)
io.interactive()
