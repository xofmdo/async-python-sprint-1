import json

from api_client import YandexWeatherAPI
from models import (
    CityModel, DayWeatherConditionsModel,
    CombinedWeatherConditionsModel, FinalOutputModel
)
from utils import RESULT_FILE_NAME, START_TIME, END_TIME, CONDITIONS


class DataFetchingTask:
    """
    Получение данных через API
    """
    ywAPI: YandexWeatherAPI = YandexWeatherAPI()

    def get_data(self, city_name: str) -> CityModel:
        """Получение данных по API"""
        city_data = self.ywAPI.get_forecasting(city_name)
        return CityModel(
            city=city_name,
            forecasts=city_data
        )


class DataCalculationTask:
    """
    Вычисление погодных параметров
    """

    @staticmethod
    def __additional_calculating(temp_data: list) -> float:
        """ Вычисление средних показателей с округлением."""

        if temp_data:
            return round(sum(temp_data) / len(temp_data), 2)
        else:
            return 0

    def __calculating_data(self,
                           city_data: CityModel) -> CombinedWeatherConditionsModel:
        """ Вычисление средних показателей"""

        weather_data = []
        for day in city_data.forecasts.forecasts:
            result_temp_for_day = []
            count_clear_cond = 0

            for hour in day.hours:
                if START_TIME < hour.hour < END_TIME:
                    result_temp_for_day.append(hour.temp)
                    count_clear_cond += \
                        1 if hour.condition in CONDITIONS else 0

            weather_data.append(
                DayWeatherConditionsModel(
                    date=day.date,
                    daily_avg_temp=self.__additional_calculating(
                        result_temp_for_day),
                    clear_weather_cond=count_clear_cond
                ))

        return CombinedWeatherConditionsModel(
            city=city_data.city,
            data=weather_data,
        )

    def __calc_general_indicators_for_day(self,
                                          data:
                                          CombinedWeatherConditionsModel) -> \
            FinalOutputModel:
        """Добавление финальных показателей"""

        list_avg_temp = []
        total_avg_clear_weather_cond = 0
        for element in data.data:
            if element.daily_avg_temp != 0.0:
                list_avg_temp.append(element.daily_avg_temp)
                total_avg_clear_weather_cond += element.clear_weather_cond

        total_avg_temperature = self.__additional_calculating(list_avg_temp)
        return FinalOutputModel(
            city=data.city,
            data=data.data,
            total_avg_temp=total_avg_temperature,
            total_clear_weather_cond=total_avg_clear_weather_cond,
            rating=0
        )

    def general_calculation(self,
                            city_data: CityModel) -> FinalOutputModel:
        """Вычисление результатов для обработки вне класса"""

        calculating = self.__calculating_data(city_data)
        result = self.__calc_general_indicators_for_day(calculating)
        return result

    @staticmethod
    def adding_rating(data: list[FinalOutputModel]) -> list[dict]:
        """Добавление рейтинга города"""

        total_rating = [
            (one_model.city,
             one_model.total_avg_temp,
             one_model.total_clear_weather_cond) for one_model in data
        ]
        sorted_rating = sorted(total_rating, key=lambda x: (-x[1], -x[2]))
        dict_rating = {
            a[0]: i + 1 for i, a in enumerate(sorted_rating)}
        for element in data:
            element.rating = dict_rating[element.city]
        result = [
            element.dict() for element in data
        ]
        return result


class DataAggregationTask:
    """
    Объединение вычисленных данных
    """

    @staticmethod
    def save_results(to_save: list[dict]) -> None:
        """Сохранение аналитических данных"""

        with open(RESULT_FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(to_save, file, indent=2)


class DataAnalyzingTask:
    """
     Финальный анализ и получение результата
    """

    @staticmethod
    def get_result(data: list[dict]) -> str:
        """Получение результата"""

        result = []
        max_temp = -9999
        sunniest_weather = 0
        for city_data in data:
            if city_data['rating'] == 1:
                max_temp = city_data['total_avg_temp']
                sunniest_weather = city_data['total_clear_weather_cond']
                break

        for city_data in data:
            if city_data['total_avg_temp'] == max_temp or \
                    city_data['total_clear_weather_cond'] == sunniest_weather:
                result.append(
                    {
                        'city':
                            city_data['city'],
                        'total_avg_temp':
                            city_data['total_avg_temp'],
                        'total_clear_weather_cond':
                            city_data['total_clear_weather_cond']
                    }
                )
        answer = 'Самые лучшие погодные условия получились в городе'
        result_str = ''
        for city in result:
            result_str += f' {city["city"]}, средняя температура: ' \
                          f'{city["total_avg_temp"]}, а количество ' \
                          f'времени без осадков {city["total_clear_weather_cond"]} ' \
                          f'часов.\n'

        return answer + result_str
