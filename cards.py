# Calculam valoarea medie a unei carti din jocul de RISK
import random

infantry = 0
cavalry = 0
artillery = 0

bonus = 0
nr_of_simulations = 100000
schimb_cand_se_poate = False

for i in range(nr_of_simulations):
   card_type = random.randint(1,3) # 1 = infantry, 2 = cavalry, 3 = artillery
   if card_type == 1:
      infantry += 1
   elif card_type == 2:
      cavalry += 1
   else:
      artillery += 1
   
   nr_cards = infantry + cavalry + artillery

   if nr_cards >= 5 or schimb_cand_se_poate:
      if infantry >= 1 and cavalry >= 1 and artillery >= 1:
         bonus += 10
         infantry -= 1
         cavalry -= 1
         artillery -= 1
      elif infantry >= 3:
         bonus += 4
         infantry -= 3
      elif cavalry >= 3:
         bonus += 6
         cavalry -= 3
      elif artillery >= 3:
         bonus += 8
         artillery -= 3
      

print("Bonus per card: " + str(bonus/nr_of_simulations))
   
nr_de_teritorii = 42
nr_de_jucatori = 4
nr_de_teritorii_pe_jucator = nr_de_teritorii / nr_de_jucatori

probabilitatea_sa_detin_un_teritoriu = 1 / nr_de_jucatori
print("Probabilitatea sa detin un teritoriu: " + str(probabilitatea_sa_detin_un_teritoriu))

probabilitatea_sa_detin_1_din_3_teritorii = 1 - (1 - probabilitatea_sa_detin_un_teritoriu)**3
print("Probabilitatea sa detin 1 din 3 teritorii: " + str(probabilitatea_sa_detin_1_din_3_teritorii))

bonus_cand_detin_un_teritoriu = 2
castig_mediu_pe_teritoriu_per_schimb_de_carti = bonus_cand_detin_un_teritoriu * probabilitatea_sa_detin_1_din_3_teritorii
print("Castig mediu pe teritoriu per schimb de carti: " + str(castig_mediu_pe_teritoriu_per_schimb_de_carti))

bonus_teritoriu_per_card = castig_mediu_pe_teritoriu_per_schimb_de_carti / 3
print("Bonus teritoriu per card: " + str(bonus_teritoriu_per_card))
