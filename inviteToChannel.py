from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.errors.rpc_error_list import UsernameInvalidError, UsernameNotOccupiedError, ChatAdminRequiredError
from telethon.tl.types import InputChannel, InputUser



def inviteToChannel(client, channel, id_list):
	#Checking for not existing 
	try:
		resolve = client(ResolveUsernameRequest(channel))
	except UsernameInvalidError:
		print("Incorrect name of channel! Try again.")
		return False
	except UsernameNotOccupiedError:
		print("Incorrect name of channel! Try again.")
		return False

	chat_id = resolve.chats[0].id
	access_hash = resolve.chats[0].access_hash

	input_channel = InputChannel(chat_id, access_hash)
	
	for id in id_list:
		input_user = InputUser(id, 0)
		InviteToChannelRequest(input_channel, input_user)

	return True

