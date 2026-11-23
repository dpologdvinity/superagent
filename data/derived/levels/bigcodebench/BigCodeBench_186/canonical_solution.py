from geopy.distance import geodesic
import folium

def task_func(dic):
    """
    Generates a Folium map with markers for specified locations and calculates the geodesic
    distances between each pair of locations.

    Parameters:
        dic (dict): A dictionary with location names as keys and their latitudes and longitudes
                    as values (e.g., {'Location': {'Lat': latitude, 'Lon': longitude}}).

    Returns:
        tuple: A tuple containing a Folium map object and a dictionary with pairs of location
               names as keys and their distances in kilometers as values.

    Raises:
        ValueError: If the input dictionary is empty.

    Requirements:
    - geopy.distance.geodesic
    - folium

    Examples:
    >>> result = task_func({'Place1': {'Lat': 0, 'Lon': 0}, 'Place2': {'Lat': 0, 'Lon': 1}})
    >>> isinstance(result, tuple) and len(result) == 2
    True
    >>> isinstance(result[0], folium.folium.Map) and isinstance(result[1], dict)
    True
    """
    if not dic:
        raise ValueError("Input dictionary is empty.")
    locations = [(k, v['Lat'], v['Lon']) for k, v in dic.items()]
    distances = {}

    folium_map = folium.Map(location=[locations[0][1], locations[0][2]], zoom_start=4)

    for i in range(len(locations)):
        folium.Marker([locations[i][1], locations[i][2]], popup=locations[i][0]).add_to(folium_map)

        for j in range(i + 1, len(locations)):
            distance = geodesic((locations[i][1], locations[i][2]), (locations[j][1], locations[j][2])).kilometers
            distances[(locations[i][0], locations[j][0])] = distance

    return folium_map, distances
