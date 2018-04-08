from getId import getId
from writeToExcel import writeToExcel
from inviteToChannel import inviteToChannel
from help import welcom
import init

from sqlite3 import OperationalError

api_id=259155; api_hash='35af3efa56d9e0e159d44364aea5777f'
#phone = '+79313585883'
#username = '@ZaDaVid_PooCheredinik'

def main():
	welcom()

	#Initialization
	init.initConfig()
	try:
		client = init.initClient()
	except OperationalError:
		print("Database is locked. It maybe you close app when it parse ids.\nWait, and if it no work, delete config.ini,\n@<your username>.session and @<your username>.session-journal")
		return

	#Get info
	name = str(input("Enter name of Telegram channel (eg: @howdyho, but without @ - howdyho): "))
	limit = int(input("Enter limit of parse user (take into account - 1 member = 1/4 of second): "))

	while True:
		id = getId(client, name, limit)
		if not id:
			name = str(input("Enter name of Telegram channel (eg: @howdyho, but without @ - howdyho): "))
			id = getId(client, name, limit)
		else:
			break

	channelInvite = str(input("Enter name of Telegram channel (eg: @savemdk, but without @ - savemdk) to invite users in it: "))

	while True:
		inviting = inviteToChannel(client, channelInvite, id)
		if not inviting:
			channelInvite = str(input("Enter name of Telegram channel (eg: @savemdk, but without @ - savemdk) to invite users in it: "))
			inviting = inviteToChannel(client, channelInvite, id)
		else:
			break

	fileName = str(input("Enter name of excel file: "))
	writeToExcel(id, fileName)
	



if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nStoping...")
		exit()



