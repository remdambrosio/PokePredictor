import requests

user_poke = input("Enter the name of a Pokemon: ").lower() #ask for pokemon name
url = "https://pokeapi.co/api/v2/pokemon/" + user_poke #use input to define appropriate URL
poke_request = requests.get(url) #set up request

poke_got = "0" #give request a placeholder value
while(poke_got == "0"):

    try: #try to get json for that pokemon
        poke_got = poke_request.json()
        
    except: #if any errors occur, that pokemon probably isn't real; ask for pokemon name again (TODO: improve by catching different errors, ex. network)
        print("That's not a real Pokemon. Not yet, anyway.")
        user_poke = input("Enter the name of a REAL Pokemon: ").lower()
        url = "https://pokeapi.co/api/v2/pokemon/" + user_poke
        poke_request = requests.get(url)

poke_types = [typ["type"]["name"] for typ in poke_got["types"]]

print(poke_types)