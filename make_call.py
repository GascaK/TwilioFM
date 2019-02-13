from twilio.rest import Client
from twilio.twiml.voice_response import Dial, Number, VoiceResponse
from src.configuration import Config


class Call:
    ''' Twilio Rest API wrapper class

        The Call class contains the dialing out logic for the
        twiliofm app. Gathers all data from tfmp.ini. User must
        get all valid information from the Twilio Dashboard. info
        can be found @ www.twilio.com/console.
    '''

    def __init__(self):
        ''' __init__ for Call class no parameters

            Imports data from tfmp.ini using configuration.py
        '''

        self.config_save = Config()
        self.client = Client(
                             self.config_save.get_SID(), 
                             self.config_save.get_auth()
                             )
        self.twiml_file = self.config_save.get_twiml_bin()

    def dial_phone(self, outbound_dial):
        # Creates call to user_number then dials outbound_dial
        call = self.client.calls.create(
                    url=self.twiml_file,
                    to=self.config_save.get_user_number(),
                    from_=self.config_save.get_twilio_number()
                            )
        response = VoiceResponse()
        response.dial(outbound_dial)
        response.say('Goodbye')

if __name__ == '__main__':
    call = Call()
