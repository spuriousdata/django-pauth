from abc import ABCMeta, abstractmethod, abstractproperty

class PAuthProvider(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def configure(self, conf):
        """
        Configure provider object.
        """
        pass

    @abstractmethod
    def urls(self):
        """
        return urls needed by provider
        """
        pass

    @property
    def name(self):
        """
        return provider object name
        """
        return self.__class__.__name__


