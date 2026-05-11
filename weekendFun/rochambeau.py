player_one = input("Rock, paper, or scissors: ").strip().lower()
player_two = input("Rock, paper, or scissors: ").strip().lower()

if player_one == "rock":
    match player_two:
        case "rock":
            result = "draw"
        case "paper":
            result = "player two wins"
        case "scissors":
            result = "player one wins"

elif player_one == "paper":
    match player_two:
        case "rock":
            result = "player one wins"
        case "paper":
            result = "draw"
        case "scissors":
            result = "player two wins"

elif player_one == "scissors":
    match player_two:
        case "rock":
            result = "player two wins"
        case "paper":
            result = "player one wins"
        case "scissors":
            result = "draw"

print(result)

#player_one = input("Rock, paper, or scissors: ").strip().lower()
#player_two = input("Rock, paper, or scissors: ").strip().lower()

#rules = {
#    ("rock", "scissors"): "player one wins",
#    ("scissors", "paper"): "player one wins",
#    ("paper", "rock"): "player one wins",
#}

#if player_one == player_two:
#    result = "draw"
#elif (player_one, player_two) in rules:
#    result = rules[(player_one, player_two)]
#else:
#    result = "player two wins"

#print(result)


#choices = {"rock": 0, "paper": 1, "scissors": 2}

#p1 = choices[player_one]
#p2 = choices[player_two]

#result = (
#    "draw" if p1 == p2 else
#    "player one wins" if (p1 - p2) % 3 == 1 else
#    "player two wins"
#)

#print(result)
