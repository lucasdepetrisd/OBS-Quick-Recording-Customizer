import obswebsocket
from obswebsocket import obsws, events, requests

client = obswebsocket.obsws("localhost", 4444, "")
client.connect()
# client.call(obswebsocket.requests.GetVersion()).getObsWebsocketVersion()
# u'4.1.0'
client.call(obswebsocket.requests.GetFilenameFormatting())
print("Hi! I'm your new video\nWhat's my name?\nFilename:")
client.call(obswebsocket.requests.SetFilenameFormatting(input() + " - %MM-%DD %hh-%mm"))
client.call(obswebsocket.requests.StartRecording())
print(client.call(obswebsocket.requests.GetFilenameFormatting()))
client.call(obswebsocket.requests.SetFilenameFormatting("-%MM-%DD %hh-%mm-%ss"))
print(client.call(obswebsocket.requests.GetFilenameFormatting()))
client.disconnect()