# import logging
# import threading
# import subprocess
# import multiprocessing

from api_client import YandexWeatherAPI
from tasks import (
    DataFetchingTask,
    DataCalculationTask,
    DataAggregationTask,
    DataAnalyzingTask,
)
from utils import CITIES
from models import (
    CityModel, DayWeatherConditionsModel,
    CombinedWeatherConditionsModel, FinalOutputModel
)


def forecast_weather() -> list[CityModel]:
    """
    Анализ погодных условий по городам
    """
    forecating = []
    for city in CITIES.keys():
        city_model = DataFetchingTask().get_data(city_name=city)
        forecating.append(city_model)

    return forecating


def calculatinfg_value(data: list[CityModel]) -> list[dict]:
    result = []
    calculating_class = DataCalculationTask()
    for city in data:
        calculating_data = calculating_class.calculating_data(city)
        calculating = calculating_class.calc_general_indicators(calculating_data)
        result.append(calculating)

    total = calculating_class.adding_rating(result)
    return total


if __name__ == "__main__":
    tmp = calculatinfg_value(forecast_weather())
    saving_process = DataAggregationTask().save_results(tmp)
    result = DataAnalyzingTask().get_result(tmp)
    print(result)
