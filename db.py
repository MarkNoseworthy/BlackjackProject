
def writeWallet(amount):
    with open("money.txt", "w") as file:
        file.write(f"{amount}")
def readWallet():
    money = open("money.txt", "r")
    return money.read()

