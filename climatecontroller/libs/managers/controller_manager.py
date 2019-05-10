from django.utils import timezone
from datetime import datetime, timedelta

from climatecontroller.libs.managers import (humidity_manager, 
											 temperature_manager, 
											 carbondioxide_manager,
                                             request_manager)
from climatecontroller.libs.parsers import request_parser
from climatecontroller.libs.helpers import params_helper


def control_climate(data):
    if params_helper.temperature in data:
        manage_climate_state(float(data[params_helper.temperature]), 
                             temperature_manager.get_controller())
    
    if params_helper.humidity in data:
        manage_climate_state(float(data[params_helper.humidity]), 
                             humidity_manager.get_controller())

    if params_helper.carbondioxide in data:
        manage_carbondioxide(float(data[params_helper.carbondioxide]))
    
def manage_climate_state(current_value, controller):
    if controller.control_mode:
        state = request_manager.get_controller_state(controller.controller_ip, 
                                                     controller.controller_gpio)

        if controller.preffered_value - current_value > controller.delta and state == 0:
            request_manager.change_controller_state(controller.controller_ip, 
                                                    controller.controller_gpio,
                                                    1)

        elif current_value - controller.preffered_value > controller.delta and state == 1:
            request_manager.change_controller_state(controller.controller_ip, 
                                                    controller.controller_gpio,
                                                    0)

def manage_carbondioxide(current_value):
    controller = carbondioxide_manager.get_controller()

    if controller.control_mode:
        state = request_manager.get_controller_state(controller.controller_ip, 
                                                     controller.controller_gpio)

        if current_value > controller.max_value and state == 0:
            request_manager.change_controller_state(controller.controller_ip, 
                                                    controller.controller_gpio,
                                                    1)

        elif current_value < controller.min_value and state == 1:
            request_manager.change_controller_state(controller.controller_ip, 
                                                    controller.controller_gpio,
                                                    0)

def get_carbondioxide_controller_state():
    controller = carbondioxide_manager.get_controller()
    return  request_manager.get_controller_state(controller.controller_ip, 
                                                 controller.controller_gpio)

def get_humidity_controller_state():
    controller = humidity_manager.get_controller()
    return  request_manager.get_controller_state(controller.controller_ip, 
                                                 controller.controller_gpio)

def get_temperature_controller_state():
    controller = temperature_manager.get_controller()
    return  request_manager.get_controller_state(controller.controller_ip, 
                                                 controller.controller_gpio)                                        