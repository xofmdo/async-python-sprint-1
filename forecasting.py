import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from tasks import (
    DataFetchingTask,
    DataCalculationTask,
    DataAggregationTask,
    DataAnalyzingTask,
)
from utils import CITIES, logger


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

    lock = threading.RLock()
    table_aggr = DataAggregationTask(lock)

    table_aggr.save_results_as_json(result_data)
    table_aggr.prepare_table_xlsx(result_data)

    with ThreadPoolExecutor() as pool:
        list_to_insert = pool.map(
            table_aggr.preparing_data_for_insertion,
            result_data
        )
    current_result = list(list_to_insert)

    for i in range(len(current_result)):
        process = threading.Thread(target=table_aggr.filling_in_table,
                                   args=(current_result[i],))
        process.start()
        process.join()

    table_aggr.adding_boarder()
    results_analysis = class_for_analysis.get_result(result_data)

    return results_analysis


if __name__ == "__main__":
    print(forecast_weather())
