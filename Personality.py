from Population import Population
from Pokemon import Pokemon

class Personality:
    def __init__(self, user_poke: Pokemon, pop: Population):
        self.ope = self.set_trait("Defense Stat", user_poke, pop)               #openness: +phys def; flexible vs. rigid
        self.con = self.set_trait("Special Attack Stat", user_poke, pop)        #conscientiousness: +sp atk; strategic vs. carefree
        self.ext = self.set_trait("Attack Stat", user_poke, pop)                #extroversion: +phys atk; bombastic vs. peaceful
        self.agr = self.set_trait("Special Defense Stat", user_poke, pop)       #agreeableness: +sp def; supportive vs. independent
        self.neu = self.set_trait_neu(user_poke, pop)                           #neuroticism: -hp, +speed; robust vs. delicate
    
    def set_trait(self, stat: str, user_poke: Pokemon, pop: Population):
        """Sets personality trait to LOW if associated stat is much lower than mean; AVERAGE if +/- 15% of mean; HIGH if much higher than mean
        """
        basis = user_poke.compare_stat(stat, pop)
        if basis < 0:
            return "LOW"
        if basis > 0:
            return "HIGH"
        else:
            return "AVERAGE"
    
    def set_trait_neu(self, user_poke: Pokemon, pop: Population):
        """Sets neuroticism based on simplified aggregate of HP (negative weight) and Speed (positive weight)
        """
        aggregate = -1*(user_poke.compare_stat("Health Stat", pop)) + user_poke.compare_stat("Speed Stat", pop)
        if aggregate < 0:
            return "LOW"
        elif aggregate > 0:
            return "HIGH"
        else:
            return "AVERAGE"
        
    def __str__(self) -> str:
        return f"Openness to Experience: {self.ope}\n"\
            f"Conscientiousness: {self.con}\n"\
            f"Extroversion: {self.ext}\n"\
            f"Agreeableness: {self.agr}\n"\
            f"Neuroticism: {self.neu}"