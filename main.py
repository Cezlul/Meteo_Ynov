import sys
sys.path.append('models/components')

from data_extractor import DataExtractor
from data_cleaner import DataCleaner
from data_visualizer import DataVisualizer
from station_selector import StationSelector
from date_filter import DateFilter
from data_exporter import DataExporter


# 1. EXTRAIRE
extractor = DataExtractor('data/raw/meteo_toulouse.csv')
data = extractor.extract()

# 2. NETTOYER
cleaner = DataCleaner(data)
data_clean = cleaner.clean()

# 3. VISUALISER
print(f"\nVUE GLOBALE - TOUTES LES DONNÉES")
visualizer = DataVisualizer(data_clean)
visualizer.show_stats()

# 4. ANALYSER PAR STATION
print(f"\nANALYSE PAR STATION")
selector = StationSelector(data_clean)
stations = selector.get_stations()


if stations is not None and len(stations) > 0:
    print(f"\n{len(stations)} station(s) trouvée(s)")
    
    # Analyser la première station
    station_id = stations[0]
    print(f"\nAnalyse de la station ID: {station_id}")
    
    data_station = selector.select_station(station_id)
    

    print(f"\nSTATISTIQUES STATION {station_id}")
    visualizer_station = DataVisualizer(data_station)
    visualizer_station.show_stats()


# 5. EXPORTER
print(f"\nEXPORT DES DONNÉES")
exporter = DataExporter(data_clean)
exporter.export('data/processed/meteo_clean.csv')
print("TRAITEMENT TERMINÉ")
