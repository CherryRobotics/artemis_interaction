from ApiInteraction import ApiInteraction, ApiAIResponse
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
                    datefmt='%s',)
class ArtemisInteraction(ApiInteraction):
    def __init__(self):
        super(ArtemisInteraction, self).__init__()

    ########### Define Artemis Specific intents here ###########

if __name__ == '__main__':
    ai = ArtemisInteraction()
    user_input = ''
    while user_input != 'close':
        user_input = raw_input("me: ")
        ai.make_request(user_input)
