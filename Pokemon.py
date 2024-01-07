import typing
from Population import Population

class Pokemon:
    def __init__(self, poke_got: typing.Dict[str, typing.Any]):
        self.name = poke_got["name"]
        self.id = poke_got["id"]
        self.types = [typ["type"]["name"] for typ in poke_got["types"]]
        self.height = poke_got["height"] / 10
        self.weight = poke_got["weight"] / 10
    
    def __str__(self) -> str:
        self.name = self.name.title()
        self.types = [typ.title() for typ in self.types]

        return f"Name: {self.name}\n"\
            f"ID: {self.id}\n"\
            f"Types: {', '.join(self.types)}\n"\
            f"Height: {self.height} m\n"\
            f"Weight: {self.weight} kg"
    
    def compare_stat(self, stat: str, pop: Population) -> str:
        """Generates a statement comparing one of this Pokemon's stats to the population mean
        """
        # Get stat for this Pokemon and the population average
        poke_stat = getattr(self, stat)
        pop_avg = round(pop.get_avg(stat), 1)
        # Generate statement for height
        if (stat == "height"):
            s1 = f"{self.name} is {poke_stat} metres tall, compared to the population's mean height of {pop_avg} metres. "
            if (poke_stat > pop_avg):
                s2 = "That's one tall Pokemon!"
            elif (poke_stat < pop_avg):
                s2 = "That's kinda short!"
            else:
                s2 = "That's pretty darn average!"
            return s1 + s2
        # Generate statement for weight
        elif (stat == "weight"):
            s1 = f"{self.name} weighs {poke_stat} kilograms, compared to the population's mean weight of {pop_avg} kilograms. "
            if (poke_stat > pop_avg):
                s2 = "This one's a heavyweight!"
            elif (poke_stat < pop_avg):
                s2 = "This one's a lightweight!"
            else:
                s2 = "That's pretty darn average!"
            return s1 + s2