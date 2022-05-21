import obswebsocket

from obswebsocket import obsws, events, requests

def getFormat():
    return ws.call(requests.GetFilenameFormatting().getFilenameFormatting)

host = "localhost"
port = 4444
password = "password"

ws = obsws(host, port, password)

ws.connect()

# ws.call(obswebsocket.requests.GetVersion()).getObsWebsocketVersion()
# u'4.1.0'
ws.call(getFormat())

print("Hi! I'm your new video\nWhat's my name?\nFilename:")

ws.call(obswebsocket.requests.SetFilenameFormatting(input() + " - %MM-%DD %hh-%mm"))
ws.call(obswebsocket.requests.StartRecording())
print(getFormat())

ws.call(obswebsocket.requests.SetFilenameFormatting("-%MM-%DD %hh-%mm"))
print(getFormat())

ws.disconnect()    