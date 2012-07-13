from pauth.providers import PAuthProvider

class LinkedinProvider(PAuthProvider):
    def __init__(self):
        pass

    def configure(self, conf):
        pass

    def name(self):
        return "google"

provider = LinkedinProvider()
