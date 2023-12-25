import typing

class Pokemon:
    def __init__(self, poke_got: typing.Dict[str, typing.Any]):
        self.name: str = poke_got["name"]
        self.id: int = poke_got["id"]
        self.xp: int = poke_got["base_experience"]
        self.types: typing.List[str] = [typ["type"]["name"] for typ in poke_got["types"]]
        self.height: float = poke_got["height"] / 10
        self.weight: float = poke_got["weight"] / 10
    
    def __str__(self) -> str:
        self.name = self.name.title()
        self.types = [typ.title() for typ in self.types]

        return f"Name: {self.name}\n"\
            f"ID: {self.id}\n"\
            f"XP: {self.xp}\n"\
            f"Types: {', '.join(self.types)}\n"\
            f"Height: {self.height} m\n"\
            f"Weight: {self.weight} kg"
    
    def xp_stats(self) -> str:
        return f"{self.name} is worth {self.xp} Experience Points, which puts it in the top SOMETHING percentile.\n"