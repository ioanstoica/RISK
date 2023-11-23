# RISK statistics
import random


# roll dice
def dice(nr_faces=6):
    return random.randint(1, nr_faces)


def cost_per_unit(win_rate):
    return round((100 - win_rate) / win_rate, 2)


def attack_win_rate(
    nr_of_attackers_6=3,
    nr_of_attackers_8=0,
    attack_bonus=0,
    nr_of_defenders_6=2,
    nr_of_defenders_8=0,
    defend_bonus=0,
    nr_of_simulations=1000,
    verbose=False,
):
    attack_wins = 0
    defend_wins = 0

    nr_of_attackers = nr_of_attackers_6 + nr_of_defenders_8
    nr_of_defenders = nr_of_defenders_6 + nr_of_defenders_8

    for i in range(nr_of_simulations):
        # create the attackers dice rolls list
        attack_rolls = []
        for i in range(nr_of_attackers_6):
            attack_rolls.append(dice(6))
        for i in range(nr_of_attackers_8):
            attack_rolls.append(dice(8))
        # sort the list
        attack_rolls.sort(reverse=True)

        # create the defenders dice rolls list
        defend_rolls = []
        for i in range(nr_of_defenders_6):
            defend_rolls.append(dice(6))
        for i in range(nr_of_defenders_8):
            defend_rolls.append(dice(8))
        # sort the list
        defend_rolls.sort(reverse=True)

        # compare first dice rolls using bonuses
        if attack_rolls[0] + attack_bonus > defend_rolls[0] + defend_bonus:
            attack_wins += 1
        else:
            defend_wins += 1

        # compare the highest dice rolls
        for i in range(1, min(nr_of_attackers, nr_of_defenders)):
            if attack_rolls[i] > defend_rolls[i]:
                attack_wins += 1
            else:
                defend_wins += 1
    if verbose:
        print(
            "Attackers: "
            + str(nr_of_attackers)
            + " + "
            + str(attack_bonus)
            + " (zaruri + bonus)"
        )
        print(
            "Defenders: "
            + str(nr_of_defenders)
            + " + "
            + str(defend_bonus)
            + " (zaruri + bonus)"
        )
        print("Attack wins: " + str(attack_wins))
        print("Defend wins: " + str(defend_wins))
        print("Attack win chance: " + str(attack_wins / (attack_wins + defend_wins)))
        print("Defend win chance: " + str(defend_wins / (attack_wins + defend_wins)))

    win_rate = attack_wins / (attack_wins + defend_wins)
    return round(win_rate * 100, 2)


def attack_win_rate_game_of_thrones(
    nr_of_attackers=3,
    knights=0,
    siege_engine=0,
    nr_of_defenders=2,
    fortifications=0,
    nr_of_simulations=1000,
):
    nr_of_defenders_6 = nr_of_defenders
    nr_of_defenders_8 = 0
    if fortifications:
        nr_of_defenders_6 = 0
        nr_of_defenders_8 = nr_of_defenders

    return attack_win_rate(
        nr_of_attackers_6=max(0, nr_of_attackers - siege_engine),
        nr_of_attackers_8=min(nr_of_attackers, siege_engine),
        attack_bonus=knights,
        nr_of_defenders_6=nr_of_defenders_6,
        nr_of_defenders_8=nr_of_defenders_8,
        defend_bonus=0,
        nr_of_simulations=nr_of_simulations,
    )


nr_of_simulations = 1000

# For all possible combinations of 1 to 3 attackers, 1 to 2 defenders, 0 to 2 knigts, 0 to (2-knights) siege engine and 0 to 1 fortifications, calculate the win rate, and crete a table with the results.
with open("results_game_of_thrones.csv", "w") as out:
    out.write(
        "Attackers, Knights, Siege Engine, Defenders, Fortifications, Win rate, Cost per unit %\n"
    )
    for nr_of_attackers in range(1, 4):
        for knights in range(0, 3):
            for siege_engine in range(0, 3 - knights):
                for nr_of_defenders in range(1, min(3, nr_of_attackers + 1)):
                    for fortifications in range(0, 2):
                        out.write(
                            str(nr_of_attackers)
                            + ", "
                            + str(knights)
                            + ", "
                            + str(siege_engine)
                            + ", "
                            + str(nr_of_defenders)
                            + ", "
                            + str(fortifications)
                            + ", ",
                        )
                        win_rate = attack_win_rate_game_of_thrones(
                            nr_of_attackers=nr_of_attackers,
                            knights=knights,
                            siege_engine=siege_engine,
                            nr_of_defenders=nr_of_defenders,
                            fortifications=fortifications,
                            nr_of_simulations=nr_of_simulations,
                        )
                        out.write(str(win_rate) + ", ")
                        out.write(str(cost_per_unit(win_rate=win_rate)))
                        out.write("\n")
