from abc import ABC, abstractclassmethod
import sys  


class IPropertyListener(object):

    @abstractclassmethod
    def on_proprety_listener(self, source, name ,value):
        pass


    