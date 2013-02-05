from pauth.providers import PAuthProvider

class LinkedinProvider(PAuthProvider):
    def __init__(self):
        pass

    def configure(self, conf):
        pass

    def urls(self):
        return ()

    def callback(self, *args, **kwargs):
        pass

provider = LinkedinProvider()
