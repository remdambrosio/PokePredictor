import pandas as pd
import matplotlib.pyplot as plt

class Population:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = None
        self.load()

    def load(self) -> None:
        """Loads population data from .csv file
        """
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found. Population data could not be accessed.")

    def print(self) -> None:
        """Prints summary of data
        """
        print(self.data.head())

    def get_unit(self, stat) -> str:
        """Gets appropriate unit for that stat
        """
        if (stat == "Pokemon Height"):
            unit = "metres"
        elif (stat == "Pokemon Weight"):
            unit = "kilograms"
        else:
            unit = "points"
        return unit

    def get_avg(self, stat: str) -> float:
        """Finds population mean for a given stat
        """
        return self.data[stat].mean()
    
    def plot_dist_marked(self, stat: str, marked_val: str, name: str):
        """Plots frequency histogram for a given stat, with a value highlighted
        """
        name = name.capitalize()
        unit = self.get_unit(stat)
        # Set visible range for x-axis
        plt.xlim(0, self.data[stat].max())
        # Plot graph
        plt.hist(self.data[stat], bins=1000)
        plt.title(f"{stat} Distribution ({name} Marked)")
        plt.xlabel(f"{stat} ({unit})")
        plt.ylabel("Frequency")
        # Mark the given value
        plt.axvline(x=marked_val, color="red", linestyle="--", linewidth=2)
        plt.show()