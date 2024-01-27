from pwn import *
io = remote("helsectf2024-2da207d37b091b1b4dff-stateofgo.chals.io", 443, ssl=True)
io.interactive()

# offset: 299
# byte: 20
# flag: helsectf{redeclaring_a_Go_variable_can_shadow_another!}
