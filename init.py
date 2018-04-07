from telethon import TelegramClient
from configparser import ConfigParser
import os #For clear terminal


def initClient(configName='config.ini'):
	#Take information from config.ini
	if not os.path.exists(configName):
		print("Don't inited!")
		return

	config = ConfigParser()
	config.read(configName)

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
			client.sign_in(phone, input('Enter the code: '))
		except:
			client.sign_in(password=input('Password: '))

	return client

def init(configName="config.ini"):
	#Init configParser
	config = ConfigParser()
	config.read(configName)

	#If has inited
	if os.path.exists(configName):
		isInit = config.get("Init", "isInit")
		if isInit == "true":
			return

	#Adding sections
	config.add_section("Init")
	config.add_section("TelegramAPI")
	config.add_section("Telegram")

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