# -*- coding: utf-8 -*-
import math
import requests


FLIGHTS_URL = "https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json"


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """

    def convert_to_radians(degrees):
        """Convert lat lon to radians."""
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def get_flight_json():
    """Return json of flight info."""
    flight_json = requests.get(FLIGHTS_URL).json()
    return flight_json


def create_flight_graph(flight_json):
    """Return dictionary with city as key and values are connecting cities and lat lon."""
    flight_dict = {}
    lat_lon_dict = {}
    for idx in range(len(flight_json)):
        key = flight_json[idx]['city']
        value = flight_json[idx]['destination_cities']
        value2 = flight_json[idx]['lat_lon']
        flight_dict[key] = value
        lat_lon_dict[key] = value2
    return flight_dict, lat_lon_dict


def find_path(flight_dict, start_city, end_city, path=[]):
    """Return a flight path between two cities."""
    stack = [start_city]
    while stack:
        cur_city = stack.pop()
        if cur_city not in flight_dict:
            return None
        if cur_city not in path:
            path.append(cur_city)
            for city in flight_dict[cur_city]:
                if city == end_city:
                    path.append(end_city)
                    return path
            for city in flight_dict[cur_city]:
                if city not in path:
                    stack.append(city)


def get_lat_lon(city):
    """Return latitude and longitude given a city."""
    flight_json = get_flight_json()
    lat_lon_dict = create_flight_graph(flight_json)[1]
    lat_lon = lat_lon_dict[city]
    return lat_lon


def get_path(start_city, end_city):
    """Returns path between two cities and the distance of the path."""
    flight_json = get_flight_json()
    flight_dict = create_flight_graph(flight_json)[0]
    path = find_path(flight_dict, start_city, end_city, path=[])
    total_distance = 0
    for idx in range(len(path)):
        if idx < len(path) - 1:
            point1 = get_lat_lon(path[idx])
            point2 = get_lat_lon(path[(idx + 1)])
            distance = calculate_distance(point1, point2)
            total_distance += distance
    return path, total_distance
