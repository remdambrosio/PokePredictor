import pandas as pd

class Population:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.load()

    def load(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found. Population data could not be accessed.")

    def print(self):
            print(self.data.head())
