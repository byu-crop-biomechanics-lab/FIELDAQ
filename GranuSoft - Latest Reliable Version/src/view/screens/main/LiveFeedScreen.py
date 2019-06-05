"""
Shows all data: Temperature, Humidity, Location, Time, and all Sensor data
"""

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from Sensor import Sensor
import datetime

from view.BaseScreen import BaseScreen
from view.elements import *


Builder.load_file('view/screens/main/LiveFeedScreen.kv')

INTERVAL = .004
SECOND_CAP = 1/INTERVAL

class LiveFeedScreen(BaseScreen):
    sensor = Sensor()

    run_count = 0
    transition_to_state = StringProperty("Pause")
    #self.keys = ListProperty()
    #self.values =
    #sensor_keys =  self.sensor.get_sensor_keys()
    #for key in sensor_keys:
    #    self.keys.append(keys)
    #sensor_data =  self.sensor.get_sensor_data()
    #for i in range(0,len(sensor_data)):



    temperature_label = StringProperty("Temperature")
    humidity_label = StringProperty("Humidity")
    location_label = StringProperty("Location")
    time_label = StringProperty("Time")
    x_load_label = StringProperty("X Load")
    y_load_label = StringProperty("Y Load")
    pot_angle_label = StringProperty("Pot Angle")
    imu_angle_label = StringProperty("IMU Angle")
    data_rate_label = StringProperty("Data Rate")

    temperature = StringProperty("0")
    humidity = StringProperty("0")
    location = StringProperty("0.00, 0.00")
    time = StringProperty("00:00:00 AM")
    x_load = StringProperty("0.00")
    y_load = StringProperty("0.00")
    pot_angle = StringProperty("0")
    imu_angle = StringProperty("0")
    data_rate = StringProperty("0")
    old_time = 0

    def on_pre_enter(self):
        self.event = Clock.schedule_interval(self.update_values, INTERVAL)
        self.transition_to_state = "Pause"

    def update_values(self, obj):

        if self.run_count >= SECOND_CAP:
            self.sensor.get_header_data()
            sensor_data = self.sensor.get_sensor_data()
            self.temperature = str(sensor_data["Temperature"])
            self.humidity = str(sensor_data["Humidity"])
            self.location = str(sensor_data["Location"])
            self.time = datetime.datetime.now().strftime("%H:%M:%S %p")
            self.x_load = str(sensor_data["X Load"])
            self.y_load = str(sensor_data["Y Load"])
            self.pot_angle = str(sensor_data["Pot Angle"])
            self.imu_angle = str(sensor_data["IMU Angle"])
            # Calculate Data Acquisition Rate
            now = datetime.datetime.now()
            new_time = (int(now.strftime("%M")) * 60) + int(now.strftime("%S")) + (int(now.strftime("%f"))/1000000)
            time_dif = new_time - self.old_time
            self.data_rate = str(round(SECOND_CAP/time_dif,2))
            self.old_time = new_time
            # Reset run_count
            self.run_count = 0
        else:
            sensor_data = self.sensor.get_sensor_data()
            self.run_count = self.run_count + 1

    def on_leave(self):
        self.event.cancel()

    def transition(self):
        if(self.transition_to_state == "Pause"):
            self.event.cancel()
            self.transition_to_state = "Resume"
        else:
            self.event = Clock.schedule_interval(self.update_values, INTERVAL)
            self.transition_to_state = "Pause"