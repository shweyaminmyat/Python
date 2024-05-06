class Phone():

    def __init__(attach, brand, model, storage):
        attach.brand = brand
        attach.model = model
        attach.storage = storage

    def camera(attach):
        print(attach.brand + "is filming. Cha Luck!")

    def call(attach):
        print(attach.brand + "is calling tu tu tu...")
