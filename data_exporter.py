import os

class DataExporter:
    
    def __init__(self, data):
        self.data = data
    
    def export(self, filepath):
        print(f"Export vers : {filepath}")
        
        # Créer le dossier s'il n'existe pas
        dossier = os.path.dirname(filepath)
        if dossier and not os.path.exists(dossier):
            os.makedirs(dossier)
            print(f"Dossier créé : {dossier}")
        
        self.data.to_csv(filepath, index=False)
        print(f"({len(self.data)} lignes)")