import typing
import requests
from Population import Population

class Pokemon:
    def __init__(self):
        # Ask for user-input name, then use PokeAPI to get data
        poke_name = input("Enter the name of a Pokemon: ").lower()
        poke_url = "https://pokeapi.co/api/v2/pokemon/" + poke_name  # Use input to define appropriate URL
        poke_request: requests.Response = requests.get(poke_url)  # Set up request
        poke_got: typing.Union[str, dict] = "0"  # Give request a placeholder value
        # Try to get .json for that pokemon name
        # If a 404 error occurs, that pokemon probably isn't real; ask for pokemon name again
        while poke_got == "0":
            try:
                poke_request.raise_for_status()
                poke_got = poke_request.json()
                break
            except requests.exceptions.RequestException as req_ex:
                if poke_request.status_code == 404:  
                    print("We can't find a Pokemon with that name.")
                    poke_name = input("Enter the name of a Pokemon: ").lower()
                    poke_url = "https://pokeapi.co/api/v2/pokemon/" + poke_name
                    poke_request = requests.get(poke_url)
                else:
                    quit()
        # Assign basic stats based on PokeAPI data
        self.name = poke_got["name"]
        self.id = poke_got["id"]
        self.types = [typ["type"]["name"] for typ in poke_got["types"]]
        self.height = poke_got["height"] / 10
        self.weight = poke_got["weight"] / 10
        # Parse through PokeAPI "stats" entry to get the combat stats
        # In order: "hp", "attack", "defense", "special-attack", "special-defense", "speed"
        self.combat_stats = []
        for stat_entry in poke_got["stats"]:
            pair = (stat_entry["stat"]["name"], stat_entry["base_stat"])
            self.combat_stats.append(pair)
    
    def __str__(self) -> str:
        self.name = self.name.title()
        self.types = [typ.title() for typ in self.types]

        return f"Name: {self.name}\n"\
            f"ID: {self.id}\n"\
            f"Types: {', '.join(self.types)}\n"\
            f"Height: {self.height} m\n"\
            f"Weight: {self.weight} kg"
    
    def compare_stat(self, stat: str, pop: Population) -> int:
        """Returns -1 if Pokemon's stat is much lower than mean; 0 if +/- 15% of mean; 1 if much higher than mean
        """
        if stat == "Pokemon Height":
            poke_stat = self.height
        elif stat == "Pokemon Weight":
            poke_stat = self.weight
        elif stat == "Health Stat":
            poke_stat = self.combat_stats[0][1]
        elif stat == "Attack Stat":
            poke_stat = self.combat_stats[1][1]
        elif stat == "Defense Stat":
            poke_stat = self.combat_stats[2][1]
        elif stat == "Special Attack Stat":
            poke_stat = self.combat_stats[3][1]
        elif stat == "Special Defense Stat":
            poke_stat = self.combat_stats[4][1]
        elif stat == "Speed Stat":
            poke_stat = self.combat_stats[5][1]
        pop_avg = round(pop.get_avg(stat), 1)
        if poke_stat < pop_avg - pop_avg*0.15:
            return -1
        elif poke_stat > pop_avg + pop_avg*0.15:
            return 1
        else:
            return 0

    def compare_stat_statement(self, stat: str, pop: Population) -> str:
        """Generates a statement comparing one of this Pokemon's stats to the population mean
        """
        pop_avg = round(pop.get_avg(stat), 1)
        compare = self.compare_stat(stat, pop)
        # Generate statement for height
        if stat == "Pokemon Height":
            s1 = f"{self.name} is {self.height} metres tall, compared to the population's mean height of {pop_avg} metres. "
            if compare == 1:
                s2 = "That's one tall Pokemon!"
            elif compare == -1:
                s2 = "That's kinda short!"
            else:
                s2 = "That's pretty average!"
            return s1 + s2
        # Generate statement for weight
        elif stat == "Pokemon Weight":
            s1 = f"{self.name} weighs {self.weight} kilograms, compared to the population's mean weight of {pop_avg} kilograms. "
            if compare == 1:
                s2 = "This one's a heavyweight!"
            elif compare == -1:
                s2 = "This one's a lightweight!"
            else:
                s2 = "That's pretty average!"
            return s1 + s2
        else:
            return "ERROR: Invalid stat for comparison via compare_stat_statement"