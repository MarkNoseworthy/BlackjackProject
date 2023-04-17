import sys

def writeWallet(amount):
    with open("money.txt", "w") as file:
        file.write(f"{amount}")
def readWallet():
    money = []
    try:
        money = open("money.txt", "r")
    except FileNotFoundError:
        print("Could not find money file!\nExiting program. Bye!")
        sys.exit(1)
    except Exception as e:
        print("Unknown exception, closing program.")
        print(type(e), e)
        sys.exit(1)
    return money.read()


