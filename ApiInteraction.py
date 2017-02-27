import apiai
import json
import abc
import logging
log = logging.getLogger(__name__)

class ApiAIResponse(object):
    def __init__(self, res):
        self.timestamp = res["timestamp"]
        result = res["result"]
        self.resolvedQuery = result["resolvedQuery"]
        self.action = result["action"]
        fulfillment = res["result"]["fulfillment"]
        self.agent_response = fulfillment["speech"]

class ApiInteraction(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        self.get_keys()
        self.ai = apiai.ApiAI(self.keys["clienttoken"])

    def get_keys(self):
        with open('login.key') as f:
            self.keys = json.loads(f.read())

    def make_request(self, input_req):
        request = self.ai.text_request()
        request.query = input_req
        httpresponse = request.getresponse().read()
        self.response = ApiAIResponse(json.loads(httpresponse))
        self.get_latest_response()
        log.info("Response recieved!")
        log.debug(httpresponse)

    def get_latest_response(self):
        print 'bot: ' + self.response.agent_response
