import pandas as pd
import matplotlib as plt
import seaborn as sns
from datetime import datetime

species_data = "data/species_info.csv"
species_df = pd.read_csv(species_data, index_col = "species")

#Creating a data class that stores the data and metadata given
class Data:
    def __init__(self, site,species):
        """Initialise class 

        Parameters
        ----------
        site : str
            Site code of measurement location
        species : str
            Name of gas species
        scale : str
        """
        #  Store name of species 
        self.species = species
        
        # Store site code
        self.site = site 
        
        #Storing path and loading data for each site and specific species.
        self.path = f"data/{site}_{species}.csv"
        self.df = pd.read_csv(self.path)
        
        #creating self for calibration scale and units as string to use for a graph in future.
        
        self.scale = str(species_data["scale"][self.species])
        self.units = str(species_data["scale"][self.species])
        
        def monthly_average(self):
            """"Calculating the average mf per month for certain site and species
            Returns
            -------
            monthly_ave_df
                df containing the monthly average mf
            """"
            self.df["month"] = pd.DatetimeIndex(self.df["time"]).to_period('M')
            
            monthly_ave_df = self.df.groupby(["month"]).mean()
            
            monthly_ave_df.rename (columns = {"mf":"Monthly average mole fraction"}, inplace = True) 
            
            return monthly_ave_df

        
        
