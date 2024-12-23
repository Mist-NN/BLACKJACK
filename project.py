import random

def calculate(cards):
    sum = 0
    number_A = 0
    for card in cards:
        if card in ['J', 'Q', 'K']:
            sum += 10
        elif card == 'A':
            sum += 11
            number_A += 1
        else:
            sum += int(card)
    while sum > 21 and number_A > 0:
        sum -= 10
        number_A -= 1
    return sum

def display(player_cards, cp_cards, show_cp_card):
    print("你的牌:", player_cards, "总数:", calculate(player_cards))
    if show_cp_card:
        print("庄家的手牌:", cp_cards, "总数:", calculate(cp_cards))
    else:
        print("庄家的手牌:", [cp_cards[0], "*"])

def gameapp():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    player_cards = [deck.pop(), deck.pop()]
    cp_cards = [deck.pop(), deck.pop()]
    display(player_cards, cp_cards, False)

    while True:
        action = input("输入 'hit' 来拿牌，或 'stand' 来停牌：")
        if action == 'hit':
            player_cards.append(deck.pop())
            display(player_cards, cp_cards, False)
            if calculate(player_cards) > 21:
                print("爆牌！你输了。")
                return
        elif action == 'stand':
            break
        else:
            print("输入无效，请重新输入。")

    print("\n庄家的回合：")
    display(player_cards, cp_cards, True)
    while calculate(cp_cards) < 17:
        cp_cards.append(deck.pop())
        display(player_cards, cp_cards, True)
        if calculate(cp_cards) > 21:
            print("庄家爆牌！你赢了。")
            return

    player_total = calculate(player_cards)
    cp_total = calculate(cp_cards)
    if player_total > cp_total:
        print("你赢了！")
    elif player_total == cp_total:
        print("平局。")
    else:
        print("你输了。")

gameapp()