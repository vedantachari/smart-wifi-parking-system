from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
import requests

ESP_IP = "192.168.4.1"

class SensorCard(BoxLayout):
    def __init__(self, sensor_id, **kwargs):
        super().__init__(orientation='vertical', padding=10, **kwargs)
        self.sensor_id = sensor_id
        self.label = Label(
            text=f"Sensor {sensor_id}: Checking...",
            font_size=32,
            halign="center",
            valign="middle"
        )
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        with self.canvas.before:
            self.bg_color = Color(0.5, 0.5, 0.5, 1) 
            self.bg_rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[50])

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def update_status(self, status_text):
        if status_text == "occupied":
            self.label.text = f"Parking {self.sensor_id}: OK"
            self.bg_color.rgba = (0, 1, 0, 1)
        elif status_text == "not_connected":
            self.label.text = "Not connected"
            self.bg_color.rgba = (0.5, 0.5, 0.5, 1)
        else:
            self.label.text = f"Parking {self.sensor_id}: OCCUPIED"
            self.bg_color.rgba = (1, 0, 0, 1)

class IRStatusApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', spacing=40, padding=50)

        self.sensor_layout = BoxLayout(orientation='vertical', spacing=25)
        self.sensor_cards = []

        for i in range(1, 5):
            card = SensorCard(i, size_hint_y=0.8)
            self.sensor_layout.add_widget(card)
            self.sensor_cards.append(card)

        root_layout.add_widget(self.sensor_layout)

        Clock.schedule_interval(self.check_status, 2)
        return root_layout

    def check_status(self, dt):
        try:
            r = requests.get(f"http://{ESP_IP}/status", timeout=10)
            if r.status_code == 200:
                data = r.json()
                for i, card in enumerate(self.sensor_cards):
                    card.update_status(data.get(f"sensor_{i+1}", "error"))
            else:
                for card in self.sensor_cards:
                    card.update_status("not_connected")
        except:
            for card in self.sensor_cards:
                card.update_status("not_connected")


if __name__ == '__main__':
    IRStatusApp().run()

