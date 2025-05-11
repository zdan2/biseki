import requests
import pandas as pd
import datetime

class WeatherAnalyzer:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.lat = None
        self.lon = None

    def get_location(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric&lang=ja"
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            self.lat = data['coord']['lat']
            self.lon = data['coord']['lon']
            return data
        except requests.RequestException as e:
            print(f"位置取得エラー: {e}")
            return None

    def fetch_past_weather(self, days=5):
        if self.lat is None or self.lon is None:
            print("まずは位置情報を取得してください。")
            return []

        records = []
        for i in range(1, days + 1):
            dt = int((datetime.datetime.now() - datetime.timedelta(days=i)).timestamp())
            url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
            params = {
                'lat': self.lat,
                'lon': self.lon,
                'dt': dt,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'ja'
            }
            try:
                res = requests.get(url, params=params)
                res.raise_for_status()
                data = res.json()
                records.append({
                    'date': datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d'),
                    'hourly': data.get('hourly', [])
                })
            except requests.RequestException as e:
                print(f"履歴データ取得エラー（{i}日前）: {e}")
        return records

    def analyze(self):
        current = self.get_location()
        if current:
            print(f"現在の{self.city}の気温: {current['main']['temp']}℃")
            print(f"天気: {current['weather'][0]['description']}")

        records = self.fetch_past_weather()
        dates, temps_avg = [], []

        for day in records:
            date = day['date']
            hourly_data = day.get('hourly', [])
            temps = [hour['temp'] for hour in hourly_data if 'temp' in hour]
            avg_temp = sum(temps) / len(temps) if temps else None
            dates.append(date)
            temps_avg.append(avg_temp)

        df = pd.DataFrame({
            "Date": dates,
            "Avg_Temp": temps_avg
        }).set_index("Date")

        print("\n=== 過去5日間の平均気温 ===")
        print(df)

# 使い方
wa = WeatherAnalyzer("Machida", "APIキー")
wa.analyze()
