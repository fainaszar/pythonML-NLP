import json

from watson_developer_cloud import ConversationV1


conversation = ConversationV1(
	username='7cf3a2a6-1bc4-4a6e-89e8-b4fd61bec8d0',
	password='g72AJckbERFW',
	version='2016-09-20'
	)

workspace_id="bc873ebe-1c81-4386-abc0-c90ebfa91766"

response = conversation.message(
		workspace_id = workspace_id,
		input = {
			'text' : 'Welcome'
		}
	)

print(json.dumps(response,indent=2))