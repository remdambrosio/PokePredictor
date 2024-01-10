import typing
from Population import Population
from Pokemon import Pokemon

class Personality:
    def __init__(self, user_poke: Pokemon, pop: Population):
        self.ope = self.set_trait()
        self.con = self.set_trait()
        self.ext = self.set_trait()
        self.agr = self.set_trait()
        self.ant = self.set_trait()
    
    def set_trait(self, stat: str, user_poke: Pokemon, pop: Population):
        #TODO: WRITE SET_TRAIT METHOD

#IDEAS:
#openness: +phys def; flexible vs. rigid
#conscientiousness: +sp atk; strategic vs. carefree
#extroversion: +phys atk; bombastic vs. peaceful
#agreeableness: +sp def; supportive vs. independent
#antineuroticism: +hp; robust vs. delicate