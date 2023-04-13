import random
import  db
def cardDeck():
    deck = []

    cardSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cardRanks = [ "2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "Jack", "Queen", "King", "Ace"]

    for suit in cardSuits:
        for rank in cardRanks:
            deck.append([rank, suit])
        random.shuffle(deck)
    print(deck)
    return deck

deck = cardDeck()
def deal():
    hand = []
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand


def playerCards(hand):
    for card in hand:
        print(f"{card[0]} of {card[1]}")

def dealerCards(hand):
    for card in hand:
        print(f"{card[0]} of {card[1]}")

def hit(hand):
    card = deck.pop()
    hand.append(card)

def score(hand):
    total = 0
    cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for card in hand:
        for i in card:
            if i == "10" or i == "Jack" or i == "Queen" or i == "King":
                total += cardValues[9]
            elif i == "Ace":
                while total < 11:
                    choose = input("Choose 1 or 11: ")
                    if choose == 1:
                        total += cardValues[0]
                    else:
                        total += cardValues[10]
                else:
                    total += cardValues[0]
            elif i == "2":
                total += cardValues[1]
            elif i == "3":
                total += cardValues[2]
            elif i == "4":
                total += cardValues[3]
            elif i == "5":
                total += cardValues[4]
            elif i == "6":
                total += cardValues[5]
            elif i == "7":
                total += cardValues[6]
            elif i == "8":
                total += cardValues[7]
            elif i == "9":
                total += cardValues[8]
    return total

def hasBlackJack(playerHand, dealerHand):
    if score(playerHand) == 21:
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("Blackjack! You win!")
        print()

def results(playerHand, dealerHand):
    if score(dealerHand) > 21:
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("Dealer busted.")
        print()
    if score(playerHand) > 21:
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("You busted.")
        print()
    elif score(playerHand) > score(dealerHand) and score(playerHand) <= 21:
        if score(playerHand) == 21:
            print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
            print()
            print("Blackjack! You win!")
            print()
        else:
            print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
            print()
            print("Congratulations, you win!")
            print()
    elif score(dealerHand) > score(playerHand) and score(dealerHand) <= 21:
        if score(dealerHand) == 21:
            print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
            print()
            print("Sorry, you lose. Dealer has Blackjack!")
            print()
        else:
            print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
            print()
            print("Sorry. You lose.")
            print()
    elif score(dealerHand) == score(playerHand):
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("Tied. Bet amount returned.")
        print()


def bet():
    money = db.readWallet()
    if money < "5":
        print("Money:", money)
        buyChips = input("\nWould you like to buy 50 worth of chips? (y/n): ")
        if buyChips == "y":
            amount = float(money) + 50
            db.writeWallet(amount)
    else:
        print("Money:", money)
        amount = float(input("Bet amount: "))
        if amount < 5 or amount > 1000:
            print("Bet must be between 5 and 1000, try again.")
            print()
        elif float(amount) > float(money):
            print("Insufficient funds, try again.")
            print()


def main():
    print("BLACKJACK")
    print("Blackjack payout is 3:2")
    print()


    playAgain = "y"
    while playAgain == "y":
        money = db.readWallet()
        amount = bet()
        playerHand = deal()
        dealerHand = deal()

        print()
        print("DEALER'S SHOW CARD:")
        dealerCards(dealerHand)
        score(dealerHand)
        print(score(dealerHand))
        print()
        print("YOUR CARDS:")
        playerCards(playerHand)
        score(playerHand)
        hasBlackJack(playerHand, dealerHand)
        print(score(playerHand))
        print()
        while score(playerHand) < 21 and score(playerHand) != 21:
            stand = input("Hit or stand? (hit/stand): ")
            print()
            if stand == "hit":
                hit(playerHand)
                print(f"YOUR CARDS: ")
                playerCards(playerHand)
                score(playerHand)
                print(score(playerHand))
                print()
            else:
                break
        while score(dealerHand) <= score(playerHand) or score(dealerHand) < 17:
            hit(dealerHand)
            print("DEALER'S CARDS:")
            dealerCards(dealerHand)
            print()
            score(playerHand)
            score(dealerHand)
        results(playerHand, dealerHand)
        playAgain = input("Play again? (y/n): ")
        print()

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()