from test11 import Phone

ph1 = Phone("Samsung","B105E","5GB")
ph1.camera()
ph1.call()

ph2 = Phone("Iphone","12","128GB")
ph2.camera()
ph2.call()

print(ph1.model)
print(ph2.storage)