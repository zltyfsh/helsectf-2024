import os

code = open("main.go","rb").read()
print("Mitt Go program kompilerer fint, men viser ikke flagget? Jeg som trodde Go aldri kunne gjøre noe feil!?\n")
#run_code(code)

for c, i in code:
    print(f"%3i : %c", i, c)
