class Pokemon:
    def __init__(self, poke_got):
        self.id = poke_got["id"]
        self.types = [typ["type"]["name"] for typ in poke_got["types"]]
    
    def __str__(self):
        return f"Pokemon ID: {self.id}\nTypes: {', '.join(self.types)}"