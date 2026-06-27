def blackjack(score):
    if score == 21:
        return "BlackJack!"
    elif score > 21:
        return "Bust!"
    elif score >= 17 and score < 21:
        return "Nice Hand!"
    elif score < 17:
        return "Hit me!"
    
print(blackjack(21))
print(blackjack(24))
print(blackjack(19))
print(blackjack(10))
