import random

class Card:
    """ A class to describe cards in a pack """
    suits = ['S', 'H', 'D', 'C']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    long_values = {
        'A': 'Ace', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
        '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten',
        'J': 'Jack', 'Q': 'Queen', 'K': 'King'
    }
    long_suits = {'S': 'Spades', 'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs'}

    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        suit_index = self._card_number // 13
        return Card.suits[suit_index]

    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        value_index = self._card_number % 13
        return Card.values[value_index]

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return f"{self.get_value()}{self.get_suit()}"

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        return f"{Card.long_values[self.get_value()]} of {Card.long_suits[self.get_suit()]}"


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = [Card(i) for i in range(52)]

    def length(self):
        """ returns the number of cards still in the deck """
        return len(self._card_list)

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        if self._card_list:
            return self._card_list.pop(0)
        else:
            return None

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        self._card_list.append(new_card)


# Example usage:
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle_deck()
    print(f"Deck has {deck.length()} cards.\n")

    while deck.length() > 0:
        card = deck.take_top_card()
        print(card.get_long_name())
