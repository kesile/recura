import openai, os

openai.api_key = "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"

from manual.functions import makeFunctions
from methods.chat import chat
from methods.embed import embed
from methods.training import trainFile
from methods.route import route

buckets = {
    "Tech Companies" : "This is for tech companies.",
    "Research And Innovation" : "This is for research companies.",
    "Fitness And Wellness" : "This is for companies in health, fitness, and wellness.",
    "Aerospace" : "This is for brands that operate in the Aerospace..",
    "Others" : "This is for brands who don't fit into the other categories."
}

instructions = makeFunctions(buckets)

companies = [
    "Apple",
    "Google",
    "Microsoft",
    "Amazon",
    "Facebook",
    "Tesla",
    "Nvidia",
    "Intel",
    "IBM",
    "Adobe",
    "IBM Research",
    "MIT Media Lab",
    "Stanford Research Institute",
    "Xerox PARC",
    "Bell Labs",
    "CERN",
    "Broad Institute",
    "SRI International",
    "Lawrence Livermore National Laboratory",
    "Max Planck Society",
    "Nike",
    "Under Armour",
    "Lululemon",
    "Fitbit",
    "Peloton",
    "GNC",
    "24 Hour Fitness",
    "Life Time",
    "Equinox",
    "MyFitnessPal",
    "Boeing",
    "Lockheed Martin",
    "SpaceX",
    "Blue Origin",
    "Northrop Grumman",
    "Airbus",
    "Boeing",
    "Raytheon Technologies",
    "Virgin Galactic",
    "Rocket Lab",
    "Coca-Cola",
    "Procter & Gamble",
    "General Electric",
    "Johnson & Johnson",
    "Walmart",
    "McDonald's",
    "Toyota",
    "Samsung",
    "Visa",
    "Mastercard",
    "Sony",
    "IBM Watson",
    "Intel",
    "Salesforce",
    "Cisco",
    "Oracle",
    "Netflix",
    "Adobe",
    "Uber",
    "Lyft",
    "Airbnb",
    "Twitter",
    "Snap Inc.",
    "Spotify",
    "Dropbox",
    "Zoom Video Communications",
    "Slack Technologies",
    "Fitbit",
    "GoPro",
    "Garmin",
    "Pfizer",
    "Merck & Co.",
    "Abbott Laboratories",
    "Novartis",
    "Bayer",
    "GSK",
    "AstraZeneca",
    "Hewlett-Packard",
    "Dell Technologies"
]


class Router:
    def __init__(self, buckets):
        self.buckets = buckets
        pass

    def trainWithFile(self, file, batchSize=10):
        instructions = makeFunctions(self.buckets)
        trainFile(file, instructions, chat, embed, batchSize)
    
    def route(self, question):
        return route(question, embed)



os.system("clear")
    

x = Router(buckets)
x.trainWithFile(companies)
while True:
    query = input("~ ")
    print(x.route(query))