from test11 import Phone

class Smartphone(Phone):

    def __init__(link, brand, model, storage):
        super().__init__(brand, model, storage)

    def internet(link):
        print("Using Internet")

    def touch(link):
        print("Scrolling")