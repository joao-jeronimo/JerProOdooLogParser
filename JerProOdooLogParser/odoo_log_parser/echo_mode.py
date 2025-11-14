# -*- coding: utf-8 -*-

class EchoMode:
    @classmethod
    def get_echo_plugin(self, mode):
        """
        Returna a function to convert a log digest into a string
        to be printed-out to the user.
            mode    The name of a mode.
        """
        if mode == 'python':
            return repr
        else:
            return None
