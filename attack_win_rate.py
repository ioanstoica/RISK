# RISK statistics
import random

# roll dice
def dice():
    return random.randint(1,6)

def attack_win_rate(nr_of_attackers = 3, nr_of_defenders = 2):
   attack_wins = 0
   defend_wins = 0

   for i in range(100000):
      # create the attackers dice rolls list
      attack_rolls = []
      for i in range(nr_of_attackers):
         attack_rolls.append(dice())
      # sort the list
      attack_rolls.sort(reverse=True)

      # create the defenders dice rolls list
      defend_rolls = []
      for i in range(nr_of_defenders):
         defend_rolls.append(dice())
      # sort the list
      defend_rolls.sort(reverse=True)

      # compare the highest dice rolls
      for i in range(min(nr_of_attackers, nr_of_defenders)):
         if attack_rolls[i] > defend_rolls[i]:
            attack_wins += 1
         else:
            defend_wins += 1

   print("Attackers: " + str(nr_of_attackers))
   print("Defenders: " + str(nr_of_defenders))
   print("Attack wins: " + str(attack_wins))
   print("Defend wins: " + str(defend_wins))
   print("Attack win chance: " + str(attack_wins/(attack_wins+defend_wins)))
   print("Defend win chance: " + str(defend_wins/(attack_wins+defend_wins)))

attack_win_rate(1, 1)

# + bonuses
def attack_win_rate(nr_of_attackers = 3, nr_of_defenders = 2, attack_bonus = 0, defend_bonus = 0, nr_of_simulations = 1000):
   attack_wins = 0
   defend_wins = 0

   for i in range(nr_of_simulations):
      # create the attackers dice rolls list
      attack_rolls = []
      for i in range(nr_of_attackers):
         attack_rolls.append(dice())
      # sort the list
      attack_rolls.sort(reverse=True)

      # create the defenders dice rolls list
      defend_rolls = []
      for i in range(nr_of_defenders):
         defend_rolls.append(dice())
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

   print("Attackers: " + str(nr_of_attackers) + " + " + str(attack_bonus) + " (zaruri + bonus)")
   print("Defenders: " + str(nr_of_defenders) + " + " + str(defend_bonus) + " (zaruri + bonus)")
   print("Attack wins: " + str(attack_wins))
   print("Defend wins: " + str(defend_wins))
   print("Attack win chance: " + str(attack_wins/(attack_wins+defend_wins)))
   print("Defend win chance: " + str(defend_wins/(attack_wins+defend_wins)))

attack_win_rate(3, 2, 1, 0, 100000)
