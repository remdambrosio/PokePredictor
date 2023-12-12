import requests
from Pokemon import Pokemon

#Ask user for a pokemon name, then use PokeAPI to create an appropriate Pokemon object

user_poke_name = input("Enter the name of a Pokemon: ").lower() #Ask for pokemon name
poke_url = "https://pokeapi.co/api/v2/pokemon/" + user_poke_name #Use input to define appropriate URL
poke_request = requests.get(poke_url) #Set up request

poke_got = "0" #Give request a placeholder value
while(poke_got == "0"):

    try: #Try to get json for that pokemon
        poke_request.raise_for_status()
        poke_got = poke_request.json()
        break

    except requests.exceptions.RequestException as req_ex:

        if poke_request.status_code == 404: #If a 404 error occurs, that pokemon probably isn't real; ask for pokemon name again
            print("That's not a real Pokemon. Not yet, anyway.")
            user_poke = input("Enter the name of a REAL Pokemon: ").lower()
            poke_url = "https://pokeapi.co/api/v2/pokemon/" + user_poke
            poke_request = requests.get(poke_url)

        else:
            quit()

user_poke = Pokemon(poke_got) #Use poke_got dictionary to create a corresponding Pokemon object

print(user_poke)
print(user_poke.xp_stats())

