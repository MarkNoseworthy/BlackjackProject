import random
import  db
def cardDeck():
    cardSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cardRanks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "Jack", "Queen", "King"]
    cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    deck = []
    for suit in cardSuits:
        for rank in cardRanks:
            deck.append([suit, rank])
    return deck


def cardsDealt(deck, cardValues):
    playerHand = []
    dealerHand = []

    playerScore = 0
    dealerScore = 0

def main():
    print("BLACKJACK")
    print("Blackjack payout is 3:2")
    print()
    print(cardDeck())

    playAgain = "y"
    while playAgain == "y":

        money = db.readWallet()
        print("Money: ", money)
        betAmount = float(input("Bet amount: "))
        if betAmount < 5 or betAmount > 1000:
            print("Bet needs to be between 5 and 1000, try again.")
            print()
            continue

        print("DEALER'S SHOW CARD:")
        print()

        print("YOUR CARDS:")
        print()

        playAgain = input("Play again? (y/n): ")
        print()

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()