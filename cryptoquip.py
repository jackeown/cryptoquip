#!/usr/bin/python3

import time

def clear():
	print(chr(27)+"[2J")


class colors:
    old = '\033[94m'
    new = '\033[96m'
    endc = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



clear()

promptPart = " "
prompt = ""
while promptPart != "":
	promptPart = input("enter encrypted words separated by spaces: ").upper()
	prompt += (promptPart+"\n")


alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
sub = {letter: "_" for letter in alphabet}


def displaySub(sub):
	print(f"{colors.old}{alphabet}{colors.endc}")
	print(f"{colors.new}{''.join([sub[x] for x in alphabet])}{colors.endc}")

def displayQuip(prompt, sub):
	clear()
	translated = []
	for letter in prompt:
		if letter in alphabet:
			if sub[letter] != "_":
				translated.append(f"{colors.new}{sub[letter]}{colors.endc}")
			else:
				translated.append(f"{colors.old}{letter}{colors.endc}")
		else:
			translated.append(letter)		
	print("".join(translated))
	displaySub(sub)

while any(sub[letter]=="_" for letter in set(alphabet).intersection(prompt)):
	displayQuip(prompt, sub)
	
	evidence = ""
	while "=" not in evidence:
		evidence = input("Enter Evidence (e.g. X=Y): ")
	
	x,y = evidence.split("=")
	x = x.strip().upper()[0]
	y = y.strip().upper()[0]
	
	sub[x] = y

displayQuip(prompt, sub)
print("Congratulations!!!")
