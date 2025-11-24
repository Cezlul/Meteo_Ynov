import pandas as pd

class DataExtractor:
    
    def __init__(self, filepath):
        self.filepath = filepath
    
    def extract(self):
        data = pd.read_csv(
            self.filepath, 
            on_bad_lines='skip',
            sep=';'  
        )
        print({len(data)})
        return data