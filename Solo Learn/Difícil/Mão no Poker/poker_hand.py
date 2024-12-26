from collections import Counter

def poker_hand_rank(hand):
    # Helper to evaluate card values and suits
    values_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                    '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    cards = hand.split()
    values = sorted([values_order[card[:-1]] for card in cards])
    suits = [card[-1] for card in cards]
    
    # Count occurrences of values and suits
    value_counts = Counter(values)
    suit_counts = Counter(suits)
    
    is_flush = len(suit_counts) == 1
    is_straight = len(values) == 5 and (values[-1] - values[0] == 4) and len(value_counts) == 5
    is_royal = values == [10, 11, 12, 13, 14]
    
    if is_flush and is_royal:
        return "Royal Flush"
    elif is_flush and is_straight:
        return "Straight Flush"
    elif 4 in value_counts.values():
        return "Four of a Kind"
    elif 3 in value_counts.values() and 2 in value_counts.values():
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in value_counts.values():
        return "Three of a Kind"
    elif list(value_counts.values()).count(2) == 2:
        return "Two Pairs"
    elif 2 in value_counts.values():
        return "One Pair"
    else:
        return "High Card"

# Sample Input and Output
hand = input()
print(poker_hand_rank(hand))  # Output: Two Pairs