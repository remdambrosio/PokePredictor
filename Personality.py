from Population import Population
from Pokemon import Pokemon

class Personality:
    def __init__(self, user_poke: Pokemon, pop: Population):
        self.ope = self.set_trait("Defense Stat", user_poke, pop)               #openness: +phys def; flexible vs. rigid
        self.con = self.set_trait("Special Attack Stat", user_poke, pop)        #conscientiousness: +sp atk; strategic vs. carefree
        self.ext = self.set_trait("Attack Stat", user_poke, pop)                #extroversion: +phys atk; bombastic vs. peaceful
        self.agr = self.set_trait("Special Defense Stat", user_poke, pop)       #agreeableness: +sp def; supportive vs. independent
        self.ant = self.set_trait("Health Stat", user_poke, pop)                #antineuroticism: +hp; robust vs. delicate
    
    def set_trait(self, stat: str, user_poke: Pokemon, pop: Population):
        """Sets trait to -1 if associated stat is much lower than mean; 0 if +/- 15% of mean; 1 if much higher than mean
        """
        return user_poke.compare_stat(stat, pop)