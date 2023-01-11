from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from tasks import (
    DataFetchingTask,
    DataCalculationTask,
    DataAggregationTask,
    DataAnalyzingTask,
)
from utils import CITIES, logger


# можно было реализовать вычисление результатов по городам через Queue, но
# преимуществ у данного способа перед ProcessPoolExecutor() не увидел

def forecast_weather() -> str:
    class_for_analysis = DataAnalyzingTask()

    logger.debug("Running ThreadPoolExecutor() for make_request")
    with ThreadPoolExecutor() as pool:
        forecasts = pool.map(
            DataFetchingTask().make_request,
            CITIES.keys()
        )
    class_for_calculations = DataCalculationTask()

    logger.debug("Running ProcessPoolExecutor() for %s cities models")
    with ProcessPoolExecutor() as executor:
        data = executor.map(
            class_for_calculations.general_calculation,
            list(forecasts)
        )
    result_data = class_for_calculations.adding_rating(list(data))

    DataAggregationTask().save_results(result_data)
    results_analysis = class_for_analysis.get_result(result_data)

    return results_analysis


if __name__ == "__main__":
    print(forecast_weather())
