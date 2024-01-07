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

    def get_col(self, stat) -> str:
        """Gets proper column name
        """
        if (stat == "height"):
            col = "Pokemon Height"
        elif (stat == "weight"):
            col = "Pokemon Weight"
        return col

    def get_col_unit(self, stat) -> tuple:
        """Gets proper column name and appropriate unit
        """
        if (stat == "height"):
            col = "Pokemon Height"
            unit = "metres"
        elif (stat == "weight"):
            col = "Pokemon Weight"
            unit = "kilograms"
        return col, unit

    def get_avg(self, stat: str) -> float:
        """Finds population mean for a given stat
        """
        # Determine column name based on input stat
        col = self.get_col(stat)
        # Return mean of that column
        return self.data[col].mean()
    
    def plot_dist_marked(self, stat: str, marked_val: str, name: str):
        """Plots frequency histogram for a given stat, with a value highlighted
        """
        name = name.capitalize()
        # Determine data to plot based on input stat
        col, unit = self.get_col_unit(stat)
        # Calculate mean and standard deviation
        mean = self.data[col].mean()
        std = self.data[col].std()
        # Set visible range for x-axis
        x_max = mean + std
        if (marked_val > x_max):
            x_max = marked_val
        # Plot graph
        plt.xlim(0, x_max)
        plt.hist(self.data[col], bins=1000)
        plt.title(f"{col} Distribution (vs. {name})")
        plt.xlabel(f"{col} ({unit})")
        plt.ylabel("Frequency")
        # Mark the given value
        plt.axvline(x=marked_val, color="red", linestyle="-", linewidth=2)
        plt.show()