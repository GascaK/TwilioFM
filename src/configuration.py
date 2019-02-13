import configparser as cfgpar


class Config:
    '''Configuration wrapper for tfmp.ini

        Config class utilizes configparser to load in .ini 
        files on windows. Getters and setters for all fields
        in (T)wilio(F)ile(M)aker(P)ro.ini
    '''

    def __init__(self):
        '''__init__ takes no arguments and puts the file in global scope.

            Reads in from src/tfmp.ini verify all information is
            correct before utilizing getters.
            TODO: Implement setters in main app window.
        '''

        self.config = cfgpar.ConfigParser()
        self.config.read('src/tfmp.ini')

    def _config_write(self):
        # Save changes to ini
        with open('src/tfmp.ini', 'w') as configfile:
            self.config.write(configfile)
        configfile.close()

    def set_SID(self, new_value):
        # Set new SID for Twilio
        self.config['Twilio Info']['accountsid'] = new_value
        self._config_write()

    def get_SID(self):
        # Get SID for Twilio
        return self.config['Twilio Info']['accountsid']

    def set_auth(self, new_value):
        # Set Auth Token for Twilio
        self.config['Twilio Info']['authtoken'] = new_value
        self._config_write()

    def get_auth(self):
        # Get Auth Token for Twilio
        return self.config['Twilio Info']['authtoken']

    def set_twilio_number(self, new_value):
        # Set Twilio number, to include +1
        self.config['Twilio Info']['twilionumber'] = new_value
        self._config_write()

    def get_twilio_number(self):
        # Get Twilio number
        return self.config['Twilio Info']['twilionumber']

    def set_twiml_bin(self, new_value):
        self.config['Twilio Info']['twimlbin'] = new_value
        self._config_write()

    def get_twiml_bin(self):
        return self.config['Twilio Info']['twimlbin']

    def set_user_number(self, new_value):
        # Set user number for call
        self.config['User Info']['usernumber'] = new_value
        self._config_write()

    def get_user_number(self):
        # Get user number for call
        return self.config['User Info']['usernumber']
