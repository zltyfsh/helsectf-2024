#!/bin/sh

# For å hindre misbruk er kun 13 forskjellige tegn tillatt i python-programmet:
#   not+cipher(*)
#
# Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget
# i /lol/hemmeligmappe/flagg.txt

URL=https://helsectf2024-2da207d37b091b1b4dff-not-cipher.chals.io/

program='print(*open(repr(int())))'

curl "$URL/?program=${program}"
