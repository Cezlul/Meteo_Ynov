class StationSelector:
    
    def __init__(self, data):
        self.data = data
    
    def get_stations(self):
        if 'station' in self.data.columns:
            stations = self.data['station'].unique()
            print(f"\nStations disponibles : {list(stations)}")
            return stations
        else:
            print("⚠️ Pas de colonne 'station'")
            return []
    
    def select_station(self, station_name):
        """Filtre par station."""
        if 'station' in self.data.columns:
            filtered = self.data[self.data['station'] == station_name]
            print(f"{len(filtered)} lignes")
            return filtered
        else:
            print("⚠️ Pas de colonne 'station'")
            return self.data
