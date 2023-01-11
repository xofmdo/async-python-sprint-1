# import logging

import concurrent
from concurrent.futures import ThreadPoolExecutor

from models import CityModel
from tasks import (
    DataFetchingTask,
    DataCalculationTask,
    DataAggregationTask,
    DataAnalyzingTask,
)
from utils import CITIES


# можно было реализовать вычисление результатов по городам через Queue, но
# преимуществ у данного способа перед ProcessPoolExecutor() не увидел

def forecast_weather(forecasts: list[CityModel]) -> list[dict]:
    class_for_calculations = DataCalculationTask()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        data = executor.map(
            class_for_calculations.general_calculation,
            forecasts
        )

    result_data = class_for_calculations.adding_rating(list(data))

    return result_data


if __name__ == "__main__":
    class_for_analysis = DataAnalyzingTask()

    with ThreadPoolExecutor() as pool:
        results = pool.map(
            DataFetchingTask().get_data,
            CITIES.keys()
        )

    forecast_responses = list(results)
    result = forecast_weather(forecast_responses)

    DataAggregationTask().save_results(result)

    results_analysis = class_for_analysis.get_result(result)
    print(results_analysis)
