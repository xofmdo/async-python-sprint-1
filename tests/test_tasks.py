from pathlib import Path

import pytest

from models import CityModel, FinalOutputModel, DayWeatherConditionsModel, \
    CombinedWeatherConditionsModel
from tasks import DataAggregationTask, DataAnalyzingTask, DataCalculationTask, \
    DataFetchingTask
from utils import RESULT_FILE_NAME


@pytest.mark.parametrize('city', ['PARIS'])
def test_fetch_forecast(city):
    formatted_data = DataFetchingTask().make_request(city_name=city)
    assert isinstance(formatted_data, CityModel) == True
    assert formatted_data.city == city


def test_calculating_data(city_data: CityModel):
    result = DataCalculationTask()._calculating_data(city_data=city_data)
    assert type(result) == CombinedWeatherConditionsModel
    assert type(result.data[0]) == DayWeatherConditionsModel
    assert result.data[0].date == "2022-05-26"
    assert result.data[0].clear_weather_cond == 9
    assert result.data[0].daily_avg_temp == 17.64


def test_calc_general_indicators_for_day(
        data_for_general: CombinedWeatherConditionsModel):

    result = DataCalculationTask()._calc_general_indicators_for_day(
        data=data_for_general)

    assert type(result) == FinalOutputModel
    assert type(result.data) == list
    assert type(result.data[0]) == DayWeatherConditionsModel
    assert result.city == 'PARIS'
    assert result.total_avg_temp == 17.33
    assert result.total_clear_weather_cond == 31


def test_calculate_general(city_data: CityModel):
    result = DataCalculationTask().general_calculation(
        city_data=city_data)
    assert type(result) == FinalOutputModel
    assert type(result.data) == list
    assert type(result.data[0]) == DayWeatherConditionsModel
    assert city_data.city == result.city
    assert result.total_avg_temp == 17.33
    assert result.total_clear_weather_cond == 31
    assert result.rating == 0


def test_data_aggregation(final_data):
    DataAggregationTask.save_results(final_data)
    assert Path(RESULT_FILE_NAME).exists()


def test_data_analyzing_get_result(data_for_result):
    data = 'Самые лучшие погодные условия получились в городе ABUDHABI, ' \
           'средняя температура: 34.27, а количество времени без осадков 35 ' \
           'часов.\n'
    result = DataAnalyzingTask().get_result(data_for_result)
    assert data == result
