import random
import  db
def cardDeck():
    cardSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cardRanks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "Jack", "Queen", "King"]

    deck = []
    for suit in cardSuits:
        for rank in cardRanks:
            deck.append([rank, suit])
        random.shuffle(deck)
    return deck

def deal(deck):
    hand = []
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand

def hit(hand, deck):
    card = deck.pop()
    hand.append(card)
    return hand

def score(hand):
    total = 0
    cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for card in hand:
        if card == "10" or card == "Jack" or card == "Queen" or card == "King":
            total += cardValues[9]
        elif card == "Ace":
            if total >= 11:
                total += cardValues[0]
            else:
                total += cardValues[10]
        elif card == "2":
            total += cardValues[1]
        elif card == "3":
            total += cardValues[2]
        elif card == "4":
            total += cardValues[3]
        elif card == "5":
            total += cardValues[4]
        elif card == "6":
            total += cardValues[5]
        elif card == "7":
            total += cardValues[6]
        elif card == "8":
            total += cardValues[7]
        elif card == "9":
            total += cardValues[8]
    return total

def main():
    print("BLACKJACK")
    print("Blackjack payout is 3:2")
    print()
    deck = cardDeck()
    playerHand = deal(deck)
    dealerHand = deal(deck)
    playerScore = score(playerHand)
    dealerScore = score(dealerHand)

    playAgain = "y"
    while playAgain == "y":

        money = db.readWallet()
        if money < "5":
            print("Money:", money)
            buyChips = input("\nWould you like to buy 50 worth of chips? (y/n): ")
            if buyChips == "y":
                amount = float(money) + 50
                db.writeWallet(amount)
            else:
                break
        else:
            print("Money:", money)
            amount = float(input("Bet amount: "))
            if amount < 5 or amount > 1000:
                print("Bet must be between 5 and 1000, try again.")
                print()
            elif float(amount) > float(money):
                print("Insufficient funds, try again.")
                print()
            else:
                print()
                print("DEALER'S SHOW CARD:")
                print(f"{dealerHand[0][0]} of {dealerHand[0][1]}")
                print()
                print("YOUR CARDS:")
                print(f"{playerHand[0][0]} of {playerHand[0][1]}\n{playerHand[1][0]} of {playerHand[1][1]}")
                print()
                while True:
                    stand = input("Hit or stand? (hit/stand): ")
                    print()
                    if stand == "hit":
                        hit(playerHand, deck)
                        print("YOUR CARDS:")
                        print(f"{playerHand[0][0]} of {playerHand[0][1]}\n{playerHand[1][0]} of {playerHand[1][1]}"
                              f"\n{playerHand[2][0]} of {playerHand[2][1]}")
                        print()
                    else:
                        break
                print("DEALER'S CARDS:")
                print(f"{dealerHand[0][0]} of {dealerHand[0][1]}\n{dealerHand[1][0]} or {dealerHand[1][1]}")
                print()
                print(f"YOUR POINTS: {playerScore}")
                print(f"DEALER'S POINTS: {dealerScore}")
        playAgain = input("Play again? (y/n): ")
        print()

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()