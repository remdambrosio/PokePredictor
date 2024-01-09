import typing
from Population import Population
from Pokemon import Pokemon

class Personality:
    def __init__(self, user_poke: Pokemon, pop: Population):
        self.ope = self.set_trait("ope")
        self.con = self.set_trait("con")
        self.ext = self.set_trait("ext")
        self.agr = self.set_trait("agr")
        self.neu = self.set_trait("neu")
    
    def set_trait(self, trait: str):
        #TODO: WRITE SET_TRAIT METHOD

#IDEAS:
#extroversion: +phys atk; bombastic vs. secluded
#conscientiousness: +sp atk; strategic vs. careless
#openness: +phys def; adaptive vs. brittle
#agreeableness: +sp def; supportive vs. indifferent
#neuroticism: -hp; delicate vs. robust