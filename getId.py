from telethon.tl.types import InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

def getId(client, chatName, limit):
	#Get basic datas
	access_hash = client.invoke(ResolveUsernameRequest(chatName)).chats[0].access_hash
	chat_id = client.invoke(ResolveUsernameRequest(chatName)).chats[0].id
	input_channel = InputChannel(chat_id, access_hash)
	filter = ChannelParticipantsSearch('')
	offset = 0
	hash = 0
	allId = []

	count = 0
	while True:
		if count == limit:
			break
		part = client(
			GetParticipantsRequest(input_channel, filter, offset, limit, hash)
			)
		if not part.users:
			break
		allId.append(part.users[count].id)
		count+=1
		offset+=1
	return allId