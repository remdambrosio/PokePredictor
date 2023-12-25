import typing
import pandas as pd

class Population:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.data: typing.Optional[pd.DataFrame] = None
        self.load()

    def load(self) -> None:
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found. Population data could not be accessed.")

    def print(self) -> None:
        print(self.data.head())