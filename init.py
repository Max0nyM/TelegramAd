from telethon import TelegramClient
from configparser import ConfigParser
import os #For clear terminal


def initClient(configName='config.ini'):
	#Checkin if not inited
	if not os.path.exists(configName):
		print("Config file doesn't exist!")
		return

	#Init config to read
	config = ConfigParser()
	config.read(configName)

	#Get basic information
	api_id = config.get("TelegramAPI", "api_id")
	api_hash = config.get("TelegramAPI", "api_hash")
	phone = config.get("Telegram", "phone")
	username = config.get("Telegram", "username")

	#Init client
	client = TelegramClient(username, api_id, api_hash)
	client.connect()

	#If not .session file
	if not client.is_user_authorized():
		client.send_code_request(phone)
		try:
			client.sign_in(phone, input('Enter the code which you had in your telegram: '))
		except:
			client.sign_in(password=input('Enter password: '))

	return client

def initConfig(configName="config.ini"):
	#Init configParser
	config = ConfigParser()
	config.read(configName)

	#If has inited
	if os.path.exists(configName):
		#Code below maybe deleted, because if file not exist it not inited
		isInit = config.get("Init", "isInit")
		if isInit == "true":
			return

	#Adding sections
	config.add_section("Init") #is init
	config.add_section("TelegramAPI") #api_id and api_hash
	config.add_section("Telegram") #username and phone

	#Printing welcom
	print("**INIT DATA**")

	#Input data
	api_id = str(input("Enter your api_id: "))
	api_hash = str(input("Enter your api_hash: "))
	phone = str(input("Enter your phone: "))
	username = str(input("Enter your username (eg: @David_Cherednik): "))

	#Setting config
	config.set("Init", "isInit", "true")

	config.set("TelegramAPI", "api_id", api_id)
	config.set("TelegramAPI", "api_hash", api_hash)

	config.set("Telegram", "phone", phone)
	config.set("Telegram", "username", username)

	#Writing to config
	with open(configName, 'w') as file:
		config.write(file)

	#Printing successfull
	os.system("cls")
	print("**SUCCESSFULL**")
	os.system("cls")