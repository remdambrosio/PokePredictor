import typing
import pandas as pd

class Population:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = None
        self.load()

    def load(self) -> None:
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found. Population data could not be accessed.")

    def print(self) -> None:
        print(self.data.head())

    def get_avg(self, stat: str) -> float:
        # Determine column name based on input stat
        if (stat == "height"):
            col = "Pokemon Height"
        elif (stat == "weight"):
            col = "Pokemon Weight"
        # Return mean of that column
        return self.data[col].mean()