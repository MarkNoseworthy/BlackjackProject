import random
import db

# Creating the deck.
def cardDeck():
    deck = []

    cardSuits = ["\u2663", "\u2665", "\u2666", "\u2660"]
    cardRanks = ["2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "J", "Q", "K", "A"]

    for suit in cardSuits:
        for rank in cardRanks:
            deck.append([rank, suit])
    random.shuffle(deck)
    return deck

# Dealing player's hand.
def deal(deck):
    hand = []
    for i in range(2):
        hand.append(deck.pop(0))
    return hand

# Dealing dealer's hand.
def dealerDeal(deck):
    dealerHand = []
    dealerHand.append(deck.pop(0))
    return dealerHand

# Printing player's hand.
def playerCards(hand):
    for card in hand:
        print(*card)

# Printing dealer's hand.
def dealerCards(hand):
    for card in hand:
        print(*card)

# Hitting for player's and dealer's hand.
def hit(hand, deck):
    hand.append(deck.pop(0))

# Keeping track of score.
def score(hand):
    total = 0
    cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for card in hand:
        for i in card:
            if i == "10" or i == "J" or i == "Q" or i == "K":
                total += cardValues[9]
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
            elif i == "A":
                if total >= 11:
                    total += cardValues[0]
                else:
                    total += cardValues[10]
    return total

# Determining the results of the round.
def results(playerHand, dealerHand, bet):
    money = db.readWallet()
    if score(playerHand) > score(dealerHand) and score(playerHand) <= 21:
        if score(playerHand) == 21:
            print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
            print()
            print("Blackjack! You win!")
            print()
            amount = float(money) + bet * 1.5
            db.writeWallet(round(amount, 2))

        else:
            print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
            print()
            print("Congratulations, you win!")
            print()
            amount = float(money) + bet * 1.5
            db.writeWallet(round(amount, 2))

    if score(playerHand) < score(dealerHand) <= 21:
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

    if score(playerHand) > 21:
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("You busted.")
        print()

    elif score(dealerHand) > 21:
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("Dealer busted.")
        print()
        amount = float(money) + bet * 1.5
        db.writeWallet(round(amount, 2))

    elif score(dealerHand) == score(playerHand):
        print(f"YOUR POINTS: {score(playerHand)}\nDEALER'S POINTS: {score(dealerHand)}")
        print()
        print("Tied. Bet amount returned.")
        print()
        amount = float(money) + bet
        db.writeWallet(round(amount, 2))

# Main BlackJack Game application.
def main():
    print("BLACKJACK")
    print("Blackjack payout is 3:2")
    print()

    playAgain = "y"
    while playAgain == "y":

        deck = cardDeck()
        money = db.readWallet()

        if float(money) < 5:
            print("Money:", money)
            buyChips = input("\nWould you like to buy 50 worth of chips? (y/n): ")

            if buyChips == "y":
                amount = float(money) + 50
                db.writeWallet(amount)
        money = db.readWallet()
        print()

        while float(money) >= 5:
            print("Money:", money)
            bet = float(input("Bet amount: "))

            if bet < 5 or bet > 1000:
                print("Bet must be between 5 and 1000, try again.")
                print()

            elif float(bet) > float(money):
                print("Insufficient funds, try again.")
                print()

            else:
                amount = float(money) - bet
                db.writeWallet(round(amount, 2))
                break

        if float(money) < 5:
            print("Money:", money)
            buyChips = input("\nWould you like to buy 50 worth of chips? (y/n): ")

            if buyChips == "y":
                amount = float(money) + 50
                db.writeWallet(amount)

        playerHand = deal(deck)
        dealerHand = dealerDeal(deck)

        print()
        print("DEALER'S SHOW CARD:")
        dealerCards(dealerHand)
        score(dealerHand)
        print()

        print("YOUR CARDS:")
        playerCards(playerHand)
        score(playerHand)
        print()

        while score(playerHand) < 21 and score(playerHand) != 21:
            stand = input("Hit or stand? (hit/stand): ")
            print()

            if stand == "hit":
                hit(playerHand, deck)
                print(f"YOUR CARDS: ")
                playerCards(playerHand)
                score(playerHand)
                print()

            else:
                break

        while score(dealerHand) <= score(playerHand) < 21 and score(playerHand) != 21 or score(dealerHand) < 17:
            hit(dealerHand, deck)

            print("DEALER'S CARDS:")
            dealerCards(dealerHand)
            print()
            score(dealerHand)
        results(playerHand, dealerHand, bet)

        playAgain = input("Play again? (y/n): ")
        print()

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()