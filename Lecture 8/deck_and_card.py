# 11.4.1 - Composition
# 11.4.2 - Card objects
# 11.4.3 - Class attributes and the __str__ method


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # These can be used by any method of the class
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def cmp(self, other):  # We can decide which suits are more important, we need to order them
        # Check the suits  # Because they are in a list, clubs is equal to 0, diamonds to 1, hence we can do the below
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # Suits are the same... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # Ranks are the same... it's a tie

        return 0

    def __eq__(self, other):  # Defines new relational operators
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


card1 = Card(1, 11)
print(card1)

card2 = Card(1, 3)
print(card2)
print(card2.suits[1])  # Accesses the class attributes

card1.suits[1] = "Swirly Whales"  # Due to aliasing, this change will affect all the cards
print(card1)
print(card2)
card1.suits[1] = "Diamonds"

# 11.4.4 - Comparing cards
card1 = Card(1, 11)
card2 = Card(1, 3)
card3 = Card(1, 11)
print(card1 < card2)
print(card1 == card3)


# 11.4.5 - Decks
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):  # Iterates 4 times and enumerates suits from 0 to 3
            for rank in range(1, 14):  # Iterates 13 times and enumerates ranks from 1 to 13
                self.cards.append(Card(suit, rank))  # Appends a total of 52 (13*4) cards

    def __str__(self):  # Alternative to a simple "for card in self.cards: print(card)
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        rng = random.Random()  # Create a random generator
        num_cards = len(self.cards)
        for i in range(num_cards):  # We get the length of te list
            j = rng.randrange(i, num_cards)  # We choose a random card that hasn't been shuffled yet
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])  # Swaps the current with the selected card

    def shuffle_2(self):
        import random
        rng = random.Random()  # Create a random generator
        rng.shuffle(self.cards)  # Random number generator object has a shuffle method. Easier

    def remove(self, card):  # Takes a card as a parameter, removes it, and returns True if the card is in the deck
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()  # Removes and returns the top card

    def is_empty(self):  # Checks if there are any cards left
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break  # Break if out of cards
            card = self.pop()  # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)  # Add the card to the hand


red_deck = Deck()  # We can instantiate some decks
blue_deck = Deck()

# 11.4.6 - Printing the deck
# Added the "__str__" method
print(red_deck)  # Cool  # Even though the result appears on 52 lines, it is one long string that contains newlines

# 11.4.7 - Shuffling the deck
# Added the "shuffle" and "shuffle_2" method

# 11.4.8 - Removing and dealing cards
# Added "remove", "pop" and "is_empty" method

# Because of chapter 11.5.3 I added the method "deal" to the class Deck