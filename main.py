import openai

class Recura:
    def __init__(self, api_key, organization = False):
        openai.api_key = api_key
        if organization: openai.organization = organization

    def route(self, inp):
        pass

    def vote(self, inp):
        pass

    def cache(self, inp):
        pass

