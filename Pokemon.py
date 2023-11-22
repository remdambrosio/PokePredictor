class Pokemon:
    def __init__(self, poke_got):
        self.name = poke_got["name"].capitalize()
        self.id = poke_got["id"]
        self.types = [typ["type"]["name"] for typ in poke_got["types"]]
    
    def __str__(self):
        return f"Name: {self.name}\nID: {self.id}\nTypes: {', '.join(self.types)}"