#!/usr/bin/env python3
import CCCFunctions
import netTools
import printSystem
from getpass import getuser as user
from pygments import highlight, lexers, formatters
import json

def doHelp(verbose):
	printSystem.p("Displaying help dialog", 'v', verbose)
	printSystem.p("devices\t\t\tShows the scanned devices", 'i')
	printSystem.p("forget <\033[93;1mChromeCastIP\033[0m>\tShows a menu to forget certain WiFi networks for the specified <\033[93;1mChromeCastIP\033[0m>", 'i')
	printSystem.p("help\t\t\tDisplays the current dialog", 'i')
	printSystem.p("id <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates certificate data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("info <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates general data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("locale <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates locale data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("lan <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates saved network data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("reboot <\033[93;1mChromeCastIP\033[0m>/all\tReboots the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("reset <\033[93;1mChromeCastIP\033[0m>/all\tResets the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("scan\t\t\tScans for ChromeCast devices", 'i')
	printSystem.p("timezone <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates timezone data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	printSystem.p("quit\t\t\tExits ChromeCastControl", 'i')
	printSystem.p("verbose\t\t\tShows cools messages like this! Currently: '\033[93;1m" + str(verbose) + "\033[90;2m'", 'v', True)
	printSystem.p("wifi <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates all WiFi netoworks from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'p')

def multiDeviceHandler(CCDevices, command, arguments, type, verbose):

	if len(arguments) == 0:
		printSystem.p("Need to specify the IP (argument 1), like so: '\033[93;1m" + command + " " + netTools.getPrivateIP() + "\033[0m'", 'e')
	else:
		if arguments[0] == "all":
			printSystem.p("All scanned targets selected", 'v', verbose)
			if len(CCDevices) == 0:
				printSystem.p("There are no devices found, please use '\033[93;1mscan\033[0m' first!", 'e')
			else:
				printSystem.p("Action: " + type, 'v', verbose)
				for IP in [i[0] for i in CCDevices]:
					printSystem.p(IP + ":", 'i')
					if type == "id":
						for i in highlight(json.dumps(CCCFunctions.CCID(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							printSystem.p(i, 's')
						print()
					elif type == "info":
						for i in highlight(json.dumps(CCCFunctions.CCInfo(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							printSystem.p(i, 's')
						print()
					elif type == "lan":
						for i in highlight(json.dumps(CCCFunctions.CCSavedNetworks(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							printSystem.p(i, 's')
						print()
					elif type == "locale":
						for i in highlight(json.dumps(CCCFunctions.CCLocales(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							printSystem.p(i, 's')
						print()
					elif type == "reboot":
						printSystem.p("Rebooting...", 'v', verbose)
						CCCFunctions.CCReboot(arguments[0])
					elif type == "reset":
						printSystem.p("Resetting...", 'v', verbose)
						CCCFunctions.CCFactoryReset(arguments[0])
					elif type == "timezone":
						for i in highlight(json.dumps(CCCFunctions.CCTimeZones(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							printSystem.p(i, 's')
						print()
					elif type == "wifi":
						for i in highlight(json.dumps(CCCFunctions.CCScanNetworks(IP, 15), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							printSystem.p(i, 's')
						print()
		else:
			printSystem.p("Verifying target: " + arguments[0], 'v', verbose)
			if CCCFunctions.CCVerify(arguments[0]):
				printSystem.p("Target verified", 'v', verbose)
				if type == "id":
					for i in highlight(json.dumps(CCCFunctions.CCID(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						printSystem.p(i, 's')
				elif type == "info":
					for i in highlight(json.dumps(CCCFunctions.CCInfo(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						printSystem.p(i, 's')
				elif type == "lan":
					for i in highlight(json.dumps(CCCFunctions.CCSavedNetworks(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						printSystem.p(i, 's')
				elif type == "locale":
					for i in highlight(json.dumps(CCCFunctions.CCLocales(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						printSystem.p(i, 's')
				elif type == "reboot":
					printSystem.p("Rebooting: " + arguments[0], 'v', verbose)
					CCCFunctions.CCReboot(arguments[0])
				elif type == "reset":
					printSystem.p("Resetting: " + arguments[0], 'v', verbose)
					CCCFunctions.CCFactoryReset(arguments[0])
				elif type == "timezone":
					for i in highlight(json.dumps(CCCFunctions.CCTimeZones(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						printSystem.p(i, 's')
				elif type == "wifi":
					for i in highlight(json.dumps(CCCFunctions.CCScanNetworks(arguments[0], 15), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						printSystem.p(i, 's')
			else:
				printSystem.p(arguments[0] + " is not a valid ChromeCast device", 'e')

def quitCCC(verbose, exitCode = 0):
	printSystem.p("Exitting CCC", 'v', verbose)
	printSystem.doHeart("Thank you for using ChromeCastControl!", 2)
	printSystem.p("Exit code: " + str(exitCode), 'v', verbose)
	exit(exitCode)

def toggleVerbose(verbose):
	printSystem.p("Verbose toggled", 'v', verbose)
	return not verbose

verbose = False
commands = [
	["devices", "cc", "chromecasts", "hosts"],
	["forget", "delete", "remove", "del"],
	["help", "h", "?"],
	["id", "identity", "identifier"],
	["info", "enum", "enumerate", "recon", "reconnaissance"],
	["lan", "savednetwork", "savednetworks", "localnetwork", "localnetworks"],
	["locale", "locales", "langs", "languages"],
	["quit", "q", "exit", "bye"],
	["reboot", "restart", "power"],
	["reset", "factory", "facreset", "format"],
	["scan", "map", "detect"],
	["timezone", "timezones", "tz", "time"],
	["verbose", "v"],
	["wifi", "enumwifi", "scanwifi", "wifiscan", "wifienum"]
]
CCDevices = []
selectedMenuItem = -1

printSystem.doHeart("Welcome, " + user() + ", to ChromeCastControl!")
printSystem.p("Try '\033[93;1mhelp\033[0m' for a list of commands", 'i')

while True:
	try:
		userInput = printSystem.i("CCC> ", 'i')
	except KeyboardInterrupt:
		printSystem.p("KeyboardInterupt detected, closing CCC", 'v', verbose)
		quitCCC(verbose, 1)
	print()

	if userInput[:1] == "/":
		printSystem.p("Easter egg?", 'v', verbose)
		printSystem.p("Hey, this isn't Minecraft!", 'w')
		print()
		userInput = userInput[1:]

	command = userInput.split()[0]
	arguments = userInput.split()[1:]

	if any(command in i for i in commands):
		if command in [i for i in commands if i[0] == "devices"][0]:
			if len(CCDevices) == 0:
				printSystem.p("There are no devices found, please use '\033[93;1mscan\033[0m' first!", 'e')
			elif len(CCDevices) == 1:
				printSystem.p("There was one device found:", 'w')
				printSystem.p(CCDevices[0][1]["name"] + " (" + CCDevices[0][0] + ")", 's')
			else:
				printSystem.p("There were '\033[93;1m" + str(len(CCDevices)) + "\033[0m' devices found:", 's')
				for i in CCDevices:
					printSystem.p(i[1]["name"] + " (" + i[0] + ")", 's')

		elif command in [i for i in commands if i[0] == "forget"][0]:
			printSystem.p("Verifying target: " + arguments[0], 'v', verbose)
			if CCCFunctions.CCVerify(arguments[0]):
				printSystem.p("Target verified", 'v', verbose)
				savedNetworkArray = CCCFunctions.CCSavedNetworks(arguments[0])

				for i in savedNetworkArray:
					printSystem.p("[" + str(savedNetworkArray.index(i)) + "] " + i["ssid"] + " (" + str(i["wpa_id"]) + ")")

				while selectedMenuItem not in range(0, len(savedNetworkArray)):
					printSystem.p("Not a valid selection: " + selectedMenuItem, 'v', verbose)
					selectedMenuItem = int(printSystem.i("CCC>Forget> ", 'i'))

				printSystem.p("Forgetting WiFi network: " + savedNetworkArray[selectedMenuItem]["ssid"], 'v', verbose)
				CCCFunctions.CCForgetWiFi(arguments[0], str(savedNetworkArray[selectedMenuItem]["wpa_id"]))
			else:
				printSystem.p(arguments[0] + " is not a valid ChromeCast device", 'e')

		elif command in [i for i in commands if i[0] == "help"][0]:
			doHelp(verbose)

		elif command in [i for i in commands if i[0] == "id"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "id", verbose)

		elif command in [i for i in commands if i[0] == "info"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "info", verbose)

		elif command in [i for i in commands if i[0] == "lan"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "lan", verbose)

		elif command in [i for i in commands if i[0] == "locale"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "locale", verbose)

		elif command in [i for i in commands if i[0] == "quit"][0]:
			quitCCC(verbose)

		elif command in [i for i in commands if i[0] == "reboot"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "reboot", verbose)

		elif command in [i for i in commands if i[0] == "reset"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "reset", verbose)

		elif command in [i for i in commands if i[0] == "scan"][0]:
			printSystem.p("Clearing device list", 'v', verbose)
			CCDevices = []
			for i in netTools.parsePortScan(netTools.portScan(netTools.getPrivateIP(), 8008), netTools.getPrivateIP())[0]:
				printSystem.p("Verifying: " + i, 'v', verbose)
				if CCCFunctions.CCVerify(i):
					printSystem.p("Verified: " + i, 'v', verbose)
					printSystem.p("Device found: " + i + " (" + CCCFunctions.CCInfo(i)["name"] + ")", 's')
					CCDevices.append([i, CCCFunctions.CCInfo(i)])
				else:
					printSystem.p(i + " is not a valid ChromeCast device (port: '\033[93;1m8008\033[0m' open!)", 'w')

		elif command in [i for i in commands if i[0] == "timezone"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "timezone", verbose)

		elif command in [i for i in commands if i[0] == "verbose"][0]:
			printSystem.p("Toggling verbose (" + str(verbose) + " -> " + str(toggleVerbose(verbose)) + ")", 'i')
			verbose = toggleVerbose(verbose)

		elif command in [i for i in commands if i[0] == "wifi"][0]:
			printSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "wifi", verbose)

		else:
			printSystem("An unknown error has occured!", "e")

	else:
		printSystem.p("Unknown command. Try '\033[93;1mhelp\033[0m' for a list of commands", 'e')