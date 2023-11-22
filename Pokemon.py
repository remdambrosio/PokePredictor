class Pokemon:
    def __init__(self, poke_got):
        self.name = poke_got["name"]
        self.id = poke_got["id"]
        self.types = [typ["type"]["name"] for typ in poke_got["types"]]
        
        self.height = poke_got["height"] / 10
        self.weight = poke_got["weight"] / 10
    
    def __str__(self):
        self.name = self.name.title()
        self.types = [typ.title() for typ in self.types]

        return f"Name: {self.name}\n"\
            f"ID: {self.id}\n"\
            f"Types: {', '.join(self.types)}\n"\
            f"Height: {self.height} m\n"\
            f"Weight: {self.weight} kg"