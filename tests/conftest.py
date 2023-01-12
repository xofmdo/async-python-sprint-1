import json
import pytest

from models import CityModel, CombinedWeatherConditionsModel


@pytest.fixture()
def city_forecast():
    with open('tests/full_forecast.json', 'r') as file:
        return CityModel.parse_obj(json.load(file))


@pytest.fixture()
def city_data():
    tmp_model = {
        "city": "PARIS",
        "forecasts": {
            "forecasts": [
                {"date": "2022-05-26",
                 "hours":
                     [
                         {"hour": 0, "temp": 15, "condition": "cloudy"},
                         {"hour": 1, "temp": 14, "condition": "cloudy"},
                         {"hour": 2, "temp": 14, "condition": "overcast"},
                         {"hour": 3, "temp": 14, "condition": "overcast"},
                         {"hour": 4, "temp": 14, "condition": "overcast"},
                         {"hour": 5, "temp": 13, "condition": "overcast"},
                         {"hour": 6, "temp": 13, "condition": "overcast"},
                         {"hour": 7, "temp": 13, "condition": "overcast"},
                         {"hour": 8, "temp": 14, "condition": "cloudy"},
                         {"hour": 9, "temp": 14, "condition": "cloudy"},
                         {"hour": 10, "temp": 15, "condition": "light-rain"},
                         {"hour": 11, "temp": 15, "condition": "light-rain"},
                         {"hour": 12, "temp": 16, "condition": "cloudy"},
                         {"hour": 13, "temp": 17, "condition": "cloudy"},
                         {"hour": 14, "temp": 18, "condition": "cloudy"},
                         {"hour": 15, "temp": 19, "condition": "cloudy"},
                         {"hour": 16, "temp": 20, "condition": "cloudy"},
                         {"hour": 17, "temp": 20, "condition": "cloudy"},
                         {"hour": 18, "temp": 20, "condition": "cloudy"},
                         {"hour": 19, "temp": 20, "condition": "cloudy"},
                         {"hour": 20, "temp": 20, "condition": "cloudy"},
                         {"hour": 21, "temp": 18, "condition": "cloudy"},
                         {"hour": 22, "temp": 17, "condition": "cloudy"},
                         {"hour": 23, "temp": 16, "condition": "cloudy"}
                     ]},
                {"date": "2022-05-27",
                 "hours":
                     [
                         {"hour": 0, "temp": 15, "condition": "cloudy"},
                         {"hour": 1, "temp": 14, "condition": "clear"},
                         {"hour": 2, "temp": 13, "condition": "clear"},
                         {"hour": 3, "temp": 12, "condition": "clear"},
                         {"hour": 4, "temp": 11, "condition": "clear"},
                         {"hour": 5, "temp": 11, "condition": "clear"},
                         {"hour": 6, "temp": 11, "condition": "clear"},
                         {"hour": 7, "temp": 12, "condition": "clear"},
                         {"hour": 8, "temp": 12, "condition": "cloudy"},
                         {"hour": 9, "temp": 14, "condition": "cloudy"},
                         {"hour": 10, "temp": 14, "condition": "cloudy"},
                         {"hour": 11, "temp": 15, "condition": "cloudy"},
                         {"hour": 12, "temp": 16, "condition": "cloudy"},
                         {"hour": 13, "temp": 17, "condition": "cloudy"},
                         {"hour": 14, "temp": 18, "condition": "cloudy"},
                         {"hour": 15, "temp": 19, "condition": "cloudy"},
                         {"hour": 16, "temp": 20, "condition": "cloudy"},
                         {"hour": 17, "temp": 20, "condition": "cloudy"},
                         {"hour": 18, "temp": 19, "condition": "cloudy"},
                         {"hour": 19, "temp": 19, "condition": "cloudy"},
                         {"hour": 20, "temp": 19, "condition": "clear"},
                         {"hour": 21, "temp": 17, "condition": "clear"},
                         {"hour": 22, "temp": 15, "condition": "clear"},
                         {"hour": 23, "temp": 13, "condition": "clear"}]
                 },
                {"date": "2022-05-28",
                 "hours":
                     [
                         {"hour": 0, "temp": 12, "condition": "clear"},
                         {"hour": 1, "temp": 11, "condition": "clear"},
                         {"hour": 2, "temp": 10, "condition": "clear"},
                         {"hour": 3, "temp": 9, "condition": "clear"},
                         {"hour": 4, "temp": 9, "condition": "clear"},
                         {"hour": 5, "temp": 8, "condition": "clear"},
                         {"hour": 6, "temp": 8, "condition": "clear"},
                         {"hour": 7, "temp": 9, "condition": "clear"},
                         {"hour": 8, "temp": 11, "condition": "clear"},
                         {"hour": 9, "temp": 13, "condition": "clear"},
                         {"hour": 10, "temp": 15, "condition": "clear"},
                         {"hour": 11, "temp": 16, "condition": "clear"},
                         {"hour": 12, "temp": 17, "condition": "clear"},
                         {"hour": 13, "temp": 18, "condition": "clear"},
                         {"hour": 14, "temp": 18, "condition": "cloudy"},
                         {"hour": 15, "temp": 18, "condition": "cloudy"},
                         {"hour": 16, "temp": 19, "condition": "cloudy"},
                         {"hour": 17, "temp": 18, "condition": "cloudy"},
                         {"hour": 18, "temp": 18, "condition": "cloudy"},
                         {"hour": 19, "temp": 17, "condition": "cloudy"},
                         {"hour": 20, "temp": 16, "condition": "cloudy"},
                         {"hour": 21, "temp": 15, "condition": "cloudy"},
                         {"hour": 22, "temp": 14, "condition": "cloudy"},
                         {"hour": 23, "temp": 12, "condition": "clear"}]},
                {"date": "2022-05-29",
                 "hours":
                     [
                         {"hour": 0, "temp": 11, "condition": "clear"},
                         {"hour": 1, "temp": 11, "condition": "clear"},
                         {"hour": 2, "temp": 10, "condition": "clear"},
                         {"hour": 3, "temp": 8, "condition": "clear"},
                         {"hour": 4, "temp": 8, "condition": "clear"},
                         {"hour": 5, "temp": 7, "condition": "clear"},
                         {"hour": 6, "temp": 7, "condition": "clear"},
                         {"hour": 7, "temp": 7, "condition": "clear"},
                         {"hour": 8, "temp": 9, "condition": "cloudy"}]},
                {"date": "2022-05-30",
                 "hours":
                     [

                     ]
                 }
            ]
        }
    }
    data = CityModel.parse_obj(tmp_model)
    return data


@pytest.fixture()
def final_data():
    final_model = {
        "city": "PARIS",
        "data": [
            {"date": "2022-05-26", "daily_avg_temp": 17.64,
             "clear_weather_cond": 9},
            {"date": "2022-05-27", "daily_avg_temp": 17.36,
             "clear_weather_cond": 11},
            {"date": "2022-05-28", "daily_avg_temp": 17.0,
             "clear_weather_cond": 11},
            {"date": "2022-05-29", "daily_avg_temp": 0.0,
             "clear_weather_cond": 0},
            {"date": "2022-05-30", "daily_avg_temp": 0.0,
             "clear_weather_cond": 0}
        ],
        "total_avg_temp": 17.33,
        "total_clear_weather_cond": 31,
        "rating": 0
    }
    return final_model


@pytest.fixture()
def data_for_general():
    data_for_general_indicators = {
        "city": "PARIS",
        "data":
            [
                {"date": "2022-05-26", "daily_avg_temp": 17.64,
                 "clear_weather_cond": 9},
                {"date": "2022-05-27", "daily_avg_temp": 17.36,
                 "clear_weather_cond": 11},
                {"date": "2022-05-28", "daily_avg_temp": 17.0,
                 "clear_weather_cond": 11},
                {"date": "2022-05-29", "daily_avg_temp": 0.0,
                 "clear_weather_cond": 0},
                {"date": "2022-05-30", "daily_avg_temp": 0.0,
                 "clear_weather_cond": 0}]}
    data = CombinedWeatherConditionsModel.parse_obj(data_for_general_indicators)
    return data


@pytest.fixture()
def data_for_result():
    data = [
        {'city': 'MOSCOW', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 17.73,
             'clear_weather_cond': 7},
            {'date': '2022-05-27', 'daily_avg_temp': 13.09,
             'clear_weather_cond': 0},
            {'date': '2022-05-28', 'daily_avg_temp': 12.18,
             'clear_weather_cond': 0},
            {'date': '2022-05-29', 'daily_avg_temp': 12.0,
             'clear_weather_cond': 1},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}],
         'total_avg_temp': 13.75, 'total_clear_weather_cond': 8,
         'rating': 13},
        {'city': 'PARIS', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 17.64,
             'clear_weather_cond': 9},
            {'date': '2022-05-27', 'daily_avg_temp': 17.36,
             'clear_weather_cond': 11},
            {'date': '2022-05-28', 'daily_avg_temp': 17.0,
             'clear_weather_cond': 11},
            {'date': '2022-05-29', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 17.33,
         'total_clear_weather_cond': 31, 'rating': 8},
        {'city': 'LONDON',
         'data': [{
             'date': '2022-05-26',
             'daily_avg_temp': 17.36,
             'clear_weather_cond': 11},
             {
                 'date': '2022-05-27',
                 'daily_avg_temp': 16.27,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-28',
                 'daily_avg_temp': 14.64,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-29',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0},
             {
                 'date': '2022-05-30',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0}],
         'total_avg_temp': 16.09,
         'total_clear_weather_cond': 33,
         'rating': 10},
        {'city': 'BERLIN', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 19.27,
             'clear_weather_cond': 9},
            {'date': '2022-05-27', 'daily_avg_temp': 16.0,
             'clear_weather_cond': 6},
            {'date': '2022-05-28', 'daily_avg_temp': 13.64,
             'clear_weather_cond': 0},
            {'date': '2022-05-29', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 16.3,
         'total_clear_weather_cond': 15, 'rating': 9},
        {'city': 'BEIJING',
         'data': [{
             'date': '2022-05-26',
             'daily_avg_temp': 31.82,
             'clear_weather_cond': 11},
             {
                 'date': '2022-05-27',
                 'daily_avg_temp': 32.73,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-28',
                 'daily_avg_temp': 33.82,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-29',
                 'daily_avg_temp': 28.17,
                 'clear_weather_cond': 6},
             {
                 'date': '2022-05-30',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0}],
         'total_avg_temp': 31.64,
         'total_clear_weather_cond': 39,
         'rating': 3},
        {'city': 'KAZAN', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 12.55,
             'clear_weather_cond': 6},
            {'date': '2022-05-27', 'daily_avg_temp': 13.73,
             'clear_weather_cond': 0},
            {'date': '2022-05-28', 'daily_avg_temp': 14.73,
             'clear_weather_cond': 3},
            {'date': '2022-05-29', 'daily_avg_temp': 14.0,
             'clear_weather_cond': 1},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 13.75,
         'total_clear_weather_cond': 10, 'rating': 12},
        {'city': 'SPETERSBURG',
         'data': [{
             'date': '2022-05-26',
             'daily_avg_temp': 12.18,
             'clear_weather_cond': 3},
             {
                 'date': '2022-05-27',
                 'daily_avg_temp': 11.82,
                 'clear_weather_cond': 0},
             {
                 'date': '2022-05-28',
                 'daily_avg_temp': 11.64,
                 'clear_weather_cond': 0},
             {
                 'date': '2022-05-29',
                 'daily_avg_temp': 12.0,
                 'clear_weather_cond': 1},
             {
                 'date': '2022-05-30',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0}],
         'total_avg_temp': 11.91,
         'total_clear_weather_cond': 4,
         'rating': 15},
        {'city': 'VOLGOGRAD', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 22.09,
             'clear_weather_cond': 11},
            {'date': '2022-05-27', 'daily_avg_temp': 21.91,
             'clear_weather_cond': 11},
            {'date': '2022-05-28', 'daily_avg_temp': 25.64,
             'clear_weather_cond': 11},
            {'date': '2022-05-29', 'daily_avg_temp': 25.0,
             'clear_weather_cond': 1},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 23.66,
         'total_clear_weather_cond': 34, 'rating': 6},
        {'city': 'NOVOSIBIRSK',
         'data': [{
             'date': '2022-05-26',
             'daily_avg_temp': 24.91,
             'clear_weather_cond': 11},
             {
                 'date': '2022-05-27',
                 'daily_avg_temp': 22.45,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-28',
                 'daily_avg_temp': 23.27,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-29',
                 'daily_avg_temp': 22.2,
                 'clear_weather_cond': 5},
             {
                 'date': '2022-05-30',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0}],
         'total_avg_temp': 23.21,
         'total_clear_weather_cond': 38,
         'rating': 7},
        {'city': 'KALININGRAD', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 15.36,
             'clear_weather_cond': 9},
            {'date': '2022-05-27', 'daily_avg_temp': 12.82,
             'clear_weather_cond': 2},
            {'date': '2022-05-28', 'daily_avg_temp': 11.64,
             'clear_weather_cond': 1},
            {'date': '2022-05-29', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 13.27,
         'total_clear_weather_cond': 12, 'rating': 14},
        {'city': 'ABUDHABI',
         'data': [{
             'date': '2022-05-26',
             'daily_avg_temp': 34.82,
             'clear_weather_cond': 11},
             {
                 'date': '2022-05-27',
                 'daily_avg_temp': 34.45,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-28',
                 'daily_avg_temp': 33.82,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-29',
                 'daily_avg_temp': 34.0,
                 'clear_weather_cond': 2},
             {
                 'date': '2022-05-30',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0}],
         'total_avg_temp': 34.27,
         'total_clear_weather_cond': 35,
         'rating': 1},
        {'city': 'WARSZAWA', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 19.64,
             'clear_weather_cond': 11},
            {'date': '2022-05-27', 'daily_avg_temp': 14.0,
             'clear_weather_cond': 3},
            {'date': '2022-05-28', 'daily_avg_temp': 12.82,
             'clear_weather_cond': 0},
            {'date': '2022-05-29', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 15.49,
         'total_clear_weather_cond': 14, 'rating': 11},
        {'city': 'BUCHAREST',
         'data': [{
             'date': '2022-05-26',
             'daily_avg_temp': 27.45,
             'clear_weather_cond': 11},
             {
                 'date': '2022-05-27',
                 'daily_avg_temp': 26.09,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-28',
                 'daily_avg_temp': 27.82,
                 'clear_weather_cond': 11},
             {
                 'date': '2022-05-29',
                 'daily_avg_temp': 18.0,
                 'clear_weather_cond': 1},
             {
                 'date': '2022-05-30',
                 'daily_avg_temp': 0.0,
                 'clear_weather_cond': 0}],
         'total_avg_temp': 24.84,
         'total_clear_weather_cond': 34,
         'rating': 5},
        {'city': 'ROMA',
         'data': [{'date': '2022-05-26', 'daily_avg_temp': 29.0,
                   'clear_weather_cond': 11},
                  {'date': '2022-05-27',
                   'daily_avg_temp': 29.27,
                   'clear_weather_cond': 11},
                  {'date': '2022-05-28',
                   'daily_avg_temp': 25.55,
                   'clear_weather_cond': 11},
                  {'date': '2022-05-29', 'daily_avg_temp': 0.0,
                   'clear_weather_cond': 0},
                  {'date': '2022-05-30', 'daily_avg_temp': 0.0,
                   'clear_weather_cond': 0}],
         'total_avg_temp': 27.94, 'total_clear_weather_cond': 33,
         'rating': 4},
        {'city': 'CAIRO', 'data': [
            {'date': '2022-05-26', 'daily_avg_temp': 32.55,
             'clear_weather_cond': 11},
            {'date': '2022-05-27', 'daily_avg_temp': 33.18,
             'clear_weather_cond': 11},
            {'date': '2022-05-28', 'daily_avg_temp': 34.45,
             'clear_weather_cond': 11},
            {'date': '2022-05-29', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0},
            {'date': '2022-05-30', 'daily_avg_temp': 0.0,
             'clear_weather_cond': 0}], 'total_avg_temp': 33.39,
         'total_clear_weather_cond': 33, 'rating': 2}]

    return data
