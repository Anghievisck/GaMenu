from lib import * #My libary uses prompt, ErrorPrompt and list for costumizating the 'Get' functions
from random import randint as rint
import pickle

#intro!!
print("*************************************")
print("  Welcome to the RPG Sheet Editor!!  ")
print("*************************************\n")

ListOfOptions = "RPG Sheet Editor:\n 1. Create a Sheet\n 2. Show a Sheet\n 3. Get Health and Details\n 4. Level Up\n 5. Roll a dice\n 6. Save a Sheet\n 7. Load a Sheet\n 8. Exit editor\n\nSelect a option: "
Options = range(1, 9)

RangeForStats = range(1, 21)

Min = 1

Doing = ""

Name = ""
Class = ""
Race = ""
Health = ""
BaseSTR = ""
BaseDEX = ""
BaseCON = ""
BaseINT = ""
BaseWIS = ""
BaseCHA = ""

SaveState = {"Name": Name, "Class": Class, "Race": Race, "Health": Health, "STRstat": BaseSTR, "DEXstat": BaseDEX, "CONstat": BaseCON, "INTstat": BaseINT, "WISstat": BaseWIS, "CHAstat": BaseCHA}

#def Main():
while True:

	Doing = GetOption(prompt = ListOfOptions, list = Options)

# This is the 'Create a sheet' option
	while Doing == 1:
		while True:

			# This asks the users Nickname
			Name = input("What is your name? ")
			Confirmation = GetStr(prompt = f"Is '{Name}' your name? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break
		while True:
			# This asks the users Class
			Class = input("What is your Class? ")
			Confirmation = GetStr(prompt = f"Is '{Class}' your class? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break
		while True:
			# This asks the users Class
			Race = input("What is your Race? ")
			Confirmation = GetStr(prompt = f"Is '{Race}' your race? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break
		#This asks the users intial Strenght
		while True:
			BaseSTR = GetInt(prompt="What is your STR stat? ", list= [*RangeForStats])
			Confirmation = GetStr(prompt = "Are you sure? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Dexterity
		while True:
			BaseDEX = GetInt(prompt="What is your DEX stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt = "Are you sure? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Constituition
		while True:
			BaseCON = GetInt(prompt="What is your CON stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt = "Are you sure? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Intelligence
		while True:
			BaseINT = GetInt(prompt="What is your INT stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt = "Are you sure? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Wisdom
		while True:
			BaseWIS = GetInt(prompt="What is your WIS stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt = "Are you sure? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		# This asks the users intial Charisma
		while True:
			BaseCHA = GetInt(prompt="What is your CHA stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt = "Are you sure? ", ErrorPrompt = "'Y' or 'N'!")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		SaveState = {"Name": Name, "Class": Class, "Race": Race, "Health": Health, "STRstat": BaseSTR, "DEXstat": BaseDEX, "CONstat": BaseCON, "INTstat": BaseINT, "WISstat": BaseWIS, "CHAstat": BaseCHA}

		# This create a confirmation, so if the user is unsatisfied with the sheet created, he can redo it
		while True:
			Confirmation = GetStr(prompt = "Do you want to redo everything? ")
			if Confirmation == "Y":
				while True:
					print("ARE YOU SURE?")
					Confirmation = GetStr(prompt = ">>> ")
					if Confirmation == "Y":
						break
					else:
						break
			elif Confirmation == "N":
				print()
				Doing = GetOption(prompt = ListOfOptions, list = Options)
				break

# This is the 'Show a sheet' option
	while Doing == 2:

		if Name == "":
			print("There is no sheet yet, create or load a sheet...")
			print()
			break
		else:
			for key, value in SaveState.items():
				print(key,": ",value)
				print()
			break

# NOT WORKING YET
# This is the 'Get Health and Details' option
	while Doing == 3:
		print("under development\n")
		break

# This is the 'Level Up' option
	while Doing == 4:
		Points = Dice(EspecifictRoll = "D20")
		print()
		for key, value in SaveState.items():
			print(key,": ",value)
			print()
		
		while Points != 0:
			
			SelectedStat = GetOption(prompt = "Select a stat:\n 1. STR		4. INT\n 2. DEX		5. WIS\n 3. CON		6. CHA\n\n>>> ", list = [1, 2, 3, 4, 5, 6])

			SpentPoints = GetInt(prompt = f"Avaible Points: {Points}\nHow many points do you want to use?\n>>> ", list = [*range(1,Points+1)])

			if SelectedStat == 1:
				SaveState["STRstat"] = SaveState["STRstat"] + SpentPoints

			if SelectedStat == 2:
				SaveState["DEXstat"] = SaveState["DEXstat"] + SpentPoints

			if SelectedStat == 3:
				SaveState["CONstat"] = SaveState["CONstat"] + SpentPoints

			if SelectedStat == 4:
				SaveState["INTstat"] = SaveState["INTstat"] + SpentPoints

			if SelectedStat == 5:
				SaveState["WISstat"] = SaveState["WISstat"] + SpentPoints

			if SelectedStat == 6:
				SaveState["CHAstat"] = SaveState["CHAstat"] + SpentPoints
			
			Points = Points - SpentPoints
		
		with open("SheetLog", "wb") as f:
			pickle.dump(SaveState, f)
		print("Update saved!\n")
		break

# This is the 'Roll a dice' option
	while Doing == 5:
		Dice()
		break

# This is the 'Save the sheet' option
	while Doing == 6:
		SaveState = {"Name": Name, "Class": Class, "Race": Race, "Health": Health, "STRstat": BaseSTR, "DEXstat": BaseDEX, "CONstat": BaseCON, "INTstat": BaseINT, "WISstat": BaseWIS, "CHAstat": BaseCHA}
		Confirmation = GetStr(prompt = "Do you want to save the current sheet? ('y' for yes, and 'n' for no): ")
		if Confirmation == "Y":
			pass
		elif Confirmation == "N":
			print("Exiting Save\n")
			break
		with open("SheetLog", "wb") as f:
			pickle.dump(SaveState, f)
		print("\nSaved!\n")
		break

# This is the 'Load a sheet' option
	while Doing == 7:
		Confirmation = GetStr(prompt = "Do you want to load a sheet? ('y' for yes, and 'n' for no): ")
		if Confirmation == "Y":
			pass
		elif Confirmation == "N":
			print("Exiting Load\n")
			break
		with open("SheetLog", "rb") as f:
			SaveState = pickle.load(f)
		print("\nLoaded!\n")
		Name = None
		break

# This is the 'Exit editor' option
	if Doing == 8:
		Confirmation = GetStr(prompt="Do your really want to exit? ")
		if Confirmation in ["N", "n"]:
			print("Ok, then\n")
		else:
			print("Existing 'RPG Sheet Editor'")
			break

#if __name__ == "__main__":
	#Main()