import typing
import requests
import pandas as pd
import matplotlib.pyplot as plt
from Pokemon import Pokemon
from Population import Population
from Personality import Personality

# Establish Pokemon from API (updates automatically) and population data from CSV (saved locally)

pop = Population("Population_Data.csv")       # Create a Population object from .csv file
user_poke = Pokemon()                         # Create a Pokemon object from user-inputted name
user_personality: Personality(user_poke, pop) # Create a corresponding Personality object

# Test prints

print(user_poke)
print(user_poke.compare_stat_statement("Pokemon Height", pop))
print(user_poke.compare_stat_statement("Pokemon Weight", pop))
print(user_poke.combat_stats)

# Test graphs

pop.plot_dist_marked("Pokemon Height", user_poke.height, user_poke.name)
pop.plot_dist_marked("Pokemon Weight", user_poke.weight, user_poke.name)
pop.plot_dist_marked("Attack Stat", user_poke.combat_stats[1][1], user_poke.name)