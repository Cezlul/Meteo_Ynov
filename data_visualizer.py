class DataVisualizer:
    
    def __init__(self, data):
        self.data = data
    
    def show_stats(self):
        
        if 'temperature' in self.data.columns:
            print(f"Température moyenne : {self.data['temperature'].mean():.2f}°C")
            print(f"Température min : {self.data['temperature'].min():.2f}°C")
            print(f"Température max : {self.data['temperature'].max():.2f}°C")
        
        if 'humidite' in self.data.columns:
            print(f"Humidité moyenne : {self.data['humidite'].mean():.2f}%")
        
        if 'pression' in self.data.columns:
            print(f"Pression moyenne : {self.data['pression'].mean():.2f} Pa")
    
    def show_preview(self):
        print("\nAPERÇU")
        print(self.data.head())
        