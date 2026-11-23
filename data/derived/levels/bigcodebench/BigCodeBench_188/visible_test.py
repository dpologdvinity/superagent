from solution import task_func
from solution import *  # BigCodeBench official harness runs test and solution
                          # in one namespace; this keeps module constants resolved.
import unittest
from unittest.mock import patch, MagicMock, ANY

class TestCases(unittest.TestCase):

    def setUp(self):
        self.geocode_patch = patch('geopy.geocoders.Photon.geocode', return_value=MagicMock(latitude=0, longitude=0))
        self.mock_geocode = self.geocode_patch.start()
        self.addCleanup(self.geocode_patch.stop)

    def test_return_type(self):
        """Test that the function returns a folium.Map object."""
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}}
        result = task_func(locations)
        self.assertIsInstance(result, folium.Map)

    @patch('folium.Map')
    @patch('folium.Marker')
    def test_marker_creation(self, mock_marker, mock_map):
        """Test that markers are added to the map for each location."""
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': {'Lat': 1, 'Lon': 1}}
        task_func(locations)
        self.assertEqual(mock_marker.call_count, len(locations))

    @patch('geopy.geocoders.Photon.geocode')
    def test_different_locations(self, mock_geocode):
        mock_geocode.return_value = MagicMock(latitude=40.7128, longitude=-74.006)
        locations = {'Loc1': {'Lat': 0, 'Lon': 0}, 'Loc2': 'New York, USA'}
        result = task_func(locations)
        mock_geocode.assert_called_once_with('New York, USA')
