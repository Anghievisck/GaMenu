from lib import *
#Intro:
print("*************************************")
print("      Welcome to the Calculator      ")
print("*************************************")
print()

Prompt = "What operation do you want to do?\n 1. +			4. /\n 2. -                   5. Power\n 3. *  			6. Root\n>>> "

Var1 = GetInt(prompt = "Please enter the first value: ", list = None)
Var2 = GetInt(prompt = "Please enter the second value: ", list = None)
Op = GetOption(prompt = Prompt, list = [1,2,3,4,5,6])

while True:
	if Op == 1:
		total = Var1 + Var2
		print(total)
	elif Op == 2:
		total = Var1 - Var2
		print(total)
	elif Op == 3:
		total = Var1 * Var2
		print(total)
	elif Op == 4:
		total = Var1 / Var2
		print(total)
	elif Op == 5:
		total = Var1 ** Var2
		print(total)
	elif Op == 6:
		total = Var1 ** (1/Var2)
		print(total)
	print()

	Continuar = input("Want to do another calculation? 'Y' for yes and 'N' for no: ")

	while True:
		if Continuar not in ["Y", "y", "N", "n"]:
			print("Please, 'Y' or 'N'")
			Continuar = input("'Y' for yes and 'N' for no: ")
		else:
			break

	if Continuar in ["N", "n"]:
		break

	Var1 = GetInt(prompt = "Please enter the first value: ", list = None)
	Var2 = GetInt(prompt = "Please enter the second value: ", list = None)
	Op = GetOption(prompt = Prompt, list = [1,2,3,4,5,6])