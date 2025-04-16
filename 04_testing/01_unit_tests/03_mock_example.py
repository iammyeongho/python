"""
unittest.mock을 사용한 모킹 테스트 예제
이 파일은 Python의 unittest.mock을 사용하여 외부 의존성을 모킹하는 방법을 보여줍니다.
"""

from unittest import TestCase, mock
from datetime import datetime
from typing import List, Optional
import requests

class WeatherService:
    """날씨 정보를 제공하는 서비스 클래스"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.weather.com"

    def get_temperature(self, city: str) -> float:
        """도시의 현재 온도를 조회합니다."""
        url = f"{self.base_url}/temperature"
        params = {
            "city": city,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data["temperature"]

    def get_forecast(self, city: str, days: int) -> List[float]:
        """도시의 예상 온도를 조회합니다."""
        url = f"{self.base_url}/forecast"
        params = {
            "city": city,
            "days": days,
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data["temperatures"]

class WeatherApp:
    """날씨 정보를 표시하는 애플리케이션 클래스"""
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service
        self.last_update = None

    def display_temperature(self, city: str) -> str:
        """도시의 현재 온도를 표시합니다."""
        temperature = self.weather_service.get_temperature(city)
        self.last_update = datetime.now()
        return f"현재 {city}의 온도는 {temperature}°C입니다."

    def display_forecast(self, city: str, days: int) -> str:
        """도시의 예상 온도를 표시합니다."""
        temperatures = self.weather_service.get_forecast(city, days)
        self.last_update = datetime.now()
        forecast = ", ".join([f"{temp}°C" for temp in temperatures])
        return f"{city}의 {days}일간 예상 온도: {forecast}"

class TestWeatherApp(TestCase):
    """WeatherApp 클래스에 대한 테스트 케이스"""

    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        self.mock_service = mock.Mock(spec=WeatherService)
        self.weather_app = WeatherApp(self.mock_service)

    def test_display_temperature(self):
        """현재 온도 표시 테스트"""
        # 모킹된 서비스의 반환값 설정
        self.mock_service.get_temperature.return_value = 25.5

        # 테스트 실행
        result = self.weather_app.display_temperature("서울")

        # 결과 검증
        self.assertEqual(result, "현재 서울의 온도는 25.5°C입니다.")
        self.mock_service.get_temperature.assert_called_once_with("서울")
        self.assertIsInstance(self.weather_app.last_update, datetime)

    def test_display_forecast(self):
        """예상 온도 표시 테스트"""
        # 모킹된 서비스의 반환값 설정
        self.mock_service.get_forecast.return_value = [20.0, 22.0, 24.0]

        # 테스트 실행
        result = self.weather_app.display_forecast("부산", 3)

        # 결과 검증
        self.assertEqual(result, "부산의 3일간 예상 온도: 20.0°C, 22.0°C, 24.0°C")
        self.mock_service.get_forecast.assert_called_once_with("부산", 3)
        self.assertIsInstance(self.weather_app.last_update, datetime)

    def test_api_error_handling(self):
        """API 오류 처리 테스트"""
        # 모킹된 서비스에서 예외 발생 설정
        self.mock_service.get_temperature.side_effect = requests.RequestException("API 오류")

        # 테스트 실행 및 예외 검증
        with self.assertRaises(requests.RequestException):
            self.weather_app.display_temperature("서울")

class TestWeatherService(TestCase):
    """WeatherService 클래스에 대한 테스트 케이스"""

    @mock.patch('requests.get')
    def test_get_temperature(self, mock_get):
        """온도 조회 테스트"""
        # 모킹된 응답 설정
        mock_response = mock.Mock()
        mock_response.json.return_value = {"temperature": 25.5}
        mock_get.return_value = mock_response

        # 테스트 실행
        service = WeatherService("test_api_key")
        temperature = service.get_temperature("서울")

        # 결과 검증
        self.assertEqual(temperature, 25.5)
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs["params"]["city"], "서울")
        self.assertEqual(kwargs["params"]["api_key"], "test_api_key")

    @mock.patch('requests.get')
    def test_get_forecast(self, mock_get):
        """예상 온도 조회 테스트"""
        # 모킹된 응답 설정
        mock_response = mock.Mock()
        mock_response.json.return_value = {"temperatures": [20.0, 22.0, 24.0]}
        mock_get.return_value = mock_response

        # 테스트 실행
        service = WeatherService("test_api_key")
        temperatures = service.get_forecast("부산", 3)

        # 결과 검증
        self.assertEqual(temperatures, [20.0, 22.0, 24.0])
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs["params"]["city"], "부산")
        self.assertEqual(kwargs["params"]["days"], 3)
        self.assertEqual(kwargs["params"]["api_key"], "test_api_key")

if __name__ == '__main__':
    unittest.main() 