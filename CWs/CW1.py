number = input("What's your phone number")
if '+1' in number or number.endswith("2"):
    pass
elif '+7' in number or number.startswith('8'):
    print("Как дела в России?")
elif '+4' in number:
    print("Как дела в Англии?")
else:
    print("Как дела в мире?")

