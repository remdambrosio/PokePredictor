import typing
import requests
from Pokemon import Pokemon
from Population import Population
from Personality import Personality


def get_poke() -> Pokemon:
    """Takes the user-entered pokemon name and creates a corresponding Pokemon object
    """
    user_poke_name = input("Enter the name of a Pokemon: ").lower()  # Ask for a pokemon name
    poke_url = "https://pokeapi.co/api/v2/pokemon/" + user_poke_name  # Use input to define appropriate URL
    poke_request: requests.Response = requests.get(poke_url)  # Set up request
    poke_got: typing.Union[str, dict] = "0"  # Give request a placeholder value
    while poke_got == "0":
        try:  # Try to get json for that pokemon
            poke_request.raise_for_status()
            poke_got = poke_request.json()
            break
        except requests.exceptions.RequestException as req_ex:
            if poke_request.status_code == 404:  # If a 404 error occurs, that pokemon probably isn't real; ask for pokemon name again
                print("We can't find a Pokemon with that name.")
                user_poke_name = input("Enter the name of a Pokemon: ").lower()
                poke_url = "https://pokeapi.co/api/v2/pokemon/" + user_poke_name
                poke_request = requests.get(poke_url)
            else:
                quit()
    return Pokemon(poke_got)  # Return a Pokemon object


# Establish Pokemon, Population, Personality

user_poke = get_poke()                                 # Create a Pokemon object from user-input name

pop = Population("Population_Data.csv")                # Create a Population object from .csv file

user_personality = Personality(user_poke, pop)         # Create a corresponding Personality object

# Test prints

print("========================================")
print(user_poke)
print("========================================")
print(user_personality)
print("========================================")

#print(user_poke.compare_stat_statement("Pokemon Height", pop))
#print(user_poke.compare_stat_statement("Pokemon Weight", pop))

#pop.plot_dist_marked("Pokemon Height", user_poke.height, user_poke.name)
#pop.plot_dist_marked("Pokemon Weight", user_poke.weight, user_poke.name)
#pop.plot_dist_marked("Attack Stat", user_poke.combat_stats[1][1], user_poke.name)