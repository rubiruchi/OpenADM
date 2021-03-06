import httplib
import json

class SwitchAdder(object):

    def __init__(self, server):
        self.server = server

    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/omniui/add/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret

pusher = SwitchAdder('localhost')

flow1 = {
    "switch":"00:00:00:00:00:00:00:01",
    "cookie":"0",
    "priority":"3000",
    "ingressPort":"1",
    #"ether-type":"2048",
    #"srcIP":"140.113.10.10",
    "active":"true",
    "actions":"output=2",
    "command":"ADD"
    }

pusher.set(flow1)
