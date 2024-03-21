import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1
        self.value += self.card_value(card)

    def card_value(self, card):
        if card.rank in ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']:
            return int(card.rank)
        elif card.rank in ['Jack', 'Queen', 'King']:
            return 10
        else:
            if self.value + 11 <= 21:
                return 11
            else:
                return 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def display_hands(player_hand, dealer_hand, hide_dealer_card=True):
    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(card)
    print(f"Total value: {player_hand.value}")

    print("\nDealer's Hand:")
    if hide_dealer_card:
        print("Hidden Card")
        for card in dealer_hand.cards[1:]:
            print(card)
    else:
        for card in dealer_hand.cards:
            print(card)
    print(f"Total value: {dealer_hand.value}")

def player_busts():
    print("Player busts! Dealer wins.")

def player_wins():
    print("Player wins!")

def dealer_busts():
    print("Dealer busts! Player wins.")

def dealer_wins():
    print("Dealer wins!")

def push():
    print("It's a tie! Push.")

def blackjack():
    print("Blackjack!")

def play_blackjack():
    deck = Deck()

    player_hand = Hand()
    dealer_hand = Hand()

    # Deal initial cards
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    # Display initial hands
    display_hands(player_hand, dealer_hand)

    # Check for player blackjack
    if player_hand.value == 21:
        blackjack()
        if dealer_hand.value == 21:
            push()
        else:
            player_wins()
        return

    # Player's turn
    while player_hand.value < 21:
        action = input("\nDo you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.add_card(deck.deal_card())
            display_hands(player_hand, dealer_hand)
        elif action == 's':
            break
        else:
            print("Invalid input! Please enter 'h' to hit or 's' to stand.")

    # Check for player bust
    if player_hand.value > 21:
        player_busts()
        return

    # Dealer's turn
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal_card())
        display_hands(player_hand, dealer_hand, hide_dealer_card=False)

    # Check for dealer bust
    if dealer_hand.value > 21:
        dealer_busts()
        return

    # Compare hands
    if player_hand.value == dealer_hand.value:
        push()
    elif player_hand.value > dealer_hand.value:
        player_wins()
    else:
        dealer_wins()

play_blackjack()
