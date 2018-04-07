from getId import getId
from writeToExcel import writeToExcel
import init

api_id=259155; api_hash='35af3efa56d9e0e159d44364aea5777f'
#phone = '+79313585883'
#username = '@ZaDaVid_PooCheredinik'

def main():
	#Initialization
	init.init()
	client = init.initClient()

	#Get info
	name = str(input("Enter name of Telegram channel (eg: @howdyho, but without @ - howdyho): "))
	limit = int(input("Enter limit of parse user (take into account - 1 member = 1 second): "))

	id = getId(client, name, limit)

	fileName = str(input("Enter name of excel file: "))

	writeToExcel(id, fileName)
	



if __name__ == "__main__":
	main()



