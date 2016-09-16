import flight_paths


def test_get_flight_json():
    """Test function returns a json file as a list."""
    flight_json = flight_paths.get_flight_json()
    assert isinstance(flight_json, list)


def test_create_flight_graph_flight_dict():
    """Test flight dictionary returned."""
    flight_json = flight_paths.get_flight_json()
    result = flight_paths.create_flight_graph(flight_json)
    assert 'New York City' in result[0]['Boston']


def test_create_flight_graph_latlon_dict():
    """Test latlon dictionary returned."""
    flight_json = flight_paths.get_flight_json()
    result = flight_paths.create_flight_graph(flight_json)
    assert result[1]['Boston'] == [42.36306, -71.00639]


def test_find_path():
    """Test a path between two cities is returned included start and end city."""
    flight_json = flight_paths.get_flight_json()
    flight_dict = flight_paths.create_flight_graph(flight_json)[0]
    path = flight_paths.find_path(flight_dict, 'Boston', 'Seattle', path=[])
    assert isinstance(path, list)


def test_find_path_city_not_in_flight_dict():
    """Test a path between two cities returns None if city doesn't exist."""
    flight_json = flight_paths.get_flight_json()
    flight_dict = flight_paths.create_flight_graph(flight_json)[0]
    path = flight_paths.find_path(flight_dict, 'Victors Town', 'Seattle', path=[])
    assert path is None


# def test_find_path_start_direct_flight_to_end():
#     """Test a path between two cities is direct flight."""
#     flight_json = flight_paths.get_flight_json()
#     flight_dict = flight_paths.create_flight_graph(flight_json)[0]
#     path = flight_paths.find_path(flight_dict, 'Boston', 'London', path=[])
#     assert path == ['Boston', 'London']


def test_calculate_distance():
    """Test calculate distance returns distance in miles from two lat_longs."""
    point1 = flight_paths.get_lat_lon('Boston')
    point2 = flight_paths.get_lat_lon('Seattle')
    assert flight_paths.calculate_distance(point1, point2) == 2488.919156778198
