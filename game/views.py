import random
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def play_game(request):
    choose_option = request.data.get("choose_option")
    attempts = request.data.get("attempts")

    if choose_option not in ["keep", "change"] or not isinstance(attempts, int):
        return Response({"error": "Invalid input"}, status=400)

    wins, losses = 0, 0

    for _ in range(attempts):
        doors = [0, 0, 1]  # Two goats (0) and one car (1)
        random.shuffle(doors)
        player_choice = random.randint(0, 2)

        if choose_option == "keep":
            if doors[player_choice] == 1:
                wins += 1
            else:
                losses += 1

        elif choose_option == "change":
            # Monty reveals a goat from the other two doors
            remaining_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
            monty_reveal = random.choice(remaining_doors)

            # Change to the last unopened door
            final_choice = [i for i in range(3) if i != player_choice and i != monty_reveal][0]
            if doors[final_choice] == 1:
                wins += 1
            else:
                losses += 1

    return Response({"wins": wins, "losses": losses})
