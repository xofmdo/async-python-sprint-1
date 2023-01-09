from api_client import YandexWeatherAPI
from models import (
    CityModel, DayWeatherConditionsModel,
    CombinedWeatherConditionsModel
)


class DataFetchingTask:
    """
    Получение данных через API
    """
    ywAPI: YandexWeatherAPI = YandexWeatherAPI()

    def get_data(self, city_name: str) -> CityModel:
        city_data = self.ywAPI.get_forecasting(city_name)
        return CityModel(
            city=city_name,
            forecasts=city_data
        )


class DataCalculationTask:
    """
    Вычисление погодных параметров
    """
    START_TIME = 9
    END_TIME = 19
    CONDITIONS = ('clear', 'partly-cloudy', 'cloudy', 'overcast')

    @staticmethod
    def additional_calculating(temp_data: list) -> float:
        if temp_data:
            return round(sum(temp_data) / len(temp_data), 2)
        else:
            return 0

    def calculating_data(self,
                         city_data: CityModel) -> CombinedWeatherConditionsModel:
        """
            Вычисление средних показателей
        """
        weather_data = []
        for day in data.forecasts.forecasts:
            result_temp_for_day = []
            count_clear_cond = 0

            for hour in day.hours:
                if self.START_TIME <= hour.hour <= self.END_TIME:
                    result_temp_for_day.append(hour.temp)
                    count_clear_cond += 1

            weather_data.append(
                DayWeatherConditionsModel(
                    date=day.date,
                    daily_avg_temp=self.additional_calculating(
                        result_temp_for_day),
                    clear_weather_cond=count_clear_cond
                ))

        return CombinedWeatherConditionsModel(
            city=city_data.city,
            data=weather_data
        )


class DataAggregationTask:
    """
    Объединение вычисленных данных
    """
    pass


class DataAnalyzingTask:
    """
     Финальный анализ и получение результата
    """
    pass


tmp = DataFetchingTask()
tmp_2 = DataCalculationTask()

data: CityModel = tmp.get_data('MOSCOW')

print(tmp_2.calculating_data(data))