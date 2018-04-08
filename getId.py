from telethon.tl.types import InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpc_error_list import UsernameInvalidError, UsernameNotOccupiedError, ChatAdminRequiredError

def getId(client, chatName, limit, debug=False):
	#Checking for not existing 
	try:
		resolve = client(ResolveUsernameRequest(chatName))
	except UsernameInvalidError:
		print("Incorrect name of chat! Try again.")
		return False
	except UsernameNotOccupiedError:
		print("Incorrect name of chat! Try again.")
		return False

	#Checking for chat or no
	try:
		access_hash = resolve.chats[0].access_hash
		chat_id = resolve.chats[0].id
	except IndexError:
		print("It's not a chat!")
		return False

	input_channel = InputChannel(chat_id, access_hash)
	filter = ChannelParticipantsSearch('')
	offset = 0
	hash = 0
	allId = []

	#Checking for channel/private chat
	try:
		client(GetParticipantsRequest(input_channel, filter, offset, limit, hash))
	except ChatAdminRequiredError:
		print('It is channel/private chat!')
		return False

	count = 0
	while True:
		if count == limit:
			break
		part = client(
			GetParticipantsRequest(input_channel, filter, offset, limit, hash), 
			)
		if not part.users:
			break
		allId.append(part.users[count].id)
		count+=1
		offset+=1
		print('{}/{}'.format(count, limit), end='\r')
		if debug:
			print(part.users[count].id)
	return allId

