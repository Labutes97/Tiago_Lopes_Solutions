# 11.5.1 - Inheritance
# 11.5.2 - A hand of cards
from .deck_and_card import Deck, Card


class Hand(Deck):

    def __init__(self, name=""):
        """ By default the name will be empty """
        super().__init__()  # PyCharm wanted this because of the parent class. Idk why.
        self.cards = []
        self.name = name

    def add(self, card):
        """ Adds card from the deck """
        self.cards.append(card)  # Remove method is already inherited from Deck class

    def __str__(self):
        s = "Hand " + self.name  # Identifies the hand
        if self.is_empty():  # If empty program appends the words is empty
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)  # Why? I guess to print cards


# 11.5.3 - Dealing cards
# Added "deal" method

# 11.5.4 - Printing a Hand
# Added the method "deal" to the class Deck of chapter 11.4
deck = Deck()
deck.shuffle()
hand = Hand("frank")
deck.deal([hand], 5)
print(hand)

# Added "__str__" method


# 11.5.5 - The CardGame class
class CardGame:  # T implement specific games we can inherit from CardGame and add features for the new game
    def __init__(self):  # performs a significant computation, beyond initializing attributes
        self.deck = Deck()
        self.deck.shuffle()


# 11.5.6 - OldMaidHand class
class OldMaidHand(Hand):  # Getting a bit confused with this
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count


game = CardGame()
hand = OldMaidHand("frank")
game.deck.deal([hand], 13)
print(hand)

hand.remove_matches()
print(hand)


# 11.5.7 - OldMaidGame class # Need to review all of this
class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        """ Transverses the list of hands and invokes remove_matches on each """
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        for hand in self.hands:
            print(hand)


if __name__ == "__main__":  # Why doesnt the book example work?????
    game = OldMaidGame()
    game.play(["Allen", "Jeff", "Chris"])
