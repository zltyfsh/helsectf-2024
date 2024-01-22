sekvens = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA"

words = [
"AjAA",
"AiAA",
"kAAl",
"AAnA",
"AiAA",
"hAAi",
"AnAA",
"iAAj",
"pAAq",
"QAAR",
"AAlA",
"AYAA",
"LAAM",
"AgAA",
"AgAA",
"AAiA",
"AiAA",
"WAAX",
"mAAn",
"nAAo",
"jAAk",
"AZAA",
"AlAA",
"LAAM",
"AqAA"
]

flag = ""
for w in words:
    for i in range(len(sekvens)):
        if w == sekvens[i:i+4]:
            flag += chr(i)
            break

print(flag)
