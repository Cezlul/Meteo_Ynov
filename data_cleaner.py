class DataCleaner:
    
    def __init__(self, data):
        self.data = data
    
    def clean(self):
        
        # Sélectionne seulement les colonnes qui nous intéressent
        colonnes = ['heure_de_paris', 'temperature', 'humidite', 'pression', 'type_de_station', 'id']
        colonnes_presentes = [col for col in colonnes if col in self.data.columns]
        self.data = self.data[colonnes_presentes]
        
        # Renommer pour simplifier
        if 'id' in self.data.columns:
            self.data = self.data.rename(columns={'id': 'station'})
        
        if 'heure_de_paris' in self.data.columns:
            self.data = self.data.rename(columns={'heure_de_paris': 'date'})
        
        # SUppresion des valeurs manquantes
        self.data = self.data.dropna()
        
        print({len(self.data)})
        return self.data