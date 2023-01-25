import pandas as pd
import matplotlib as plt
import seaborn as sns


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
        
        
        
    def monthly_average(self):
        """Calculating the average mf per month for certain site and species
        Returns
        -------
        monthly_ave_df
        dataframe containing the monthly average mole fraction
        """
         
        self.df["month"] = pd.DatetimeIndex(self.df["time"]).to_period('M')
            
        monthly_ave_df = self.df.groupby(["month"]).mean()
            
        monthly_ave_df.rename (columns = {"mf":"Monthly average mole fraction"}, inplace = True) 
            
        return monthly_ave_df
        
    def plot (self,data):
        """ Plot site and species data
        Parameters
        ----------
        data: pandas series
        Data to plot
        """
        self.data = data
 
                
            
        #Indexing columns for graph
        x = self.data.index.astype("str")
        y = self.data[self.data.columns[-1]]
        title = str(self.data.columns [-1])
            
        #Creating Plot
        fig,ax = plt.subplots(figsize(10,5)) 
        ax.plot (x,y,color = "orange", label = f"{self.species},{self.site}")
            
        #Setting up labels
        ax.set_title(title, fontsize = 14)
        ax.set_ylabel (f"Mole fraction of {self.species}/{self.unit}(scale:{self.scale})", fontsize = 11)
        ax.set_xlabel (f"Time {self.data.index.year[0]}",fontsize = 11)
            
        ax.grid(linestyle = "-")
            
        plt.legend()
        plt.show()
        
        
