"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card == 'A':
        return 1
    elif card in ['J', 'Q', 'K']:
        return 10
    elif card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(card)
    else:
        raise ValueError("Invalid card value")
    
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """


def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return (card_one, card_two) 
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """


def value_of_ace(card_one, card_two):
    if ('A' in [card_one, card_two]):
        return 1        
    elif value_of_card(card_one) + value_of_card(card_two) + 11 <= 21:
        return 11
    else:
        return 1
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """


def is_blackjack(card_one, card_two):
    if ('A' in [card_one, card_two]) and any(card in ['K', 'Q', 'J', '10'] for card in [card_one, card_two]):
        print('blackjack', value_of_card(card_one), value_of_card(card_two))
        return True
    else:
        return False
        
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """


def can_split_pairs(card_one, card_two):
    if ['K', 'Q', 'J'] in [card_one, card_two]:
        return True
    elif value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]:
        print('double down', value_of_card(card_one), value_of_card(card_two))
        return True
    else:
        return False
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
