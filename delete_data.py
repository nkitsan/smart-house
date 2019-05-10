import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'smarthouse.settings'
django.setup()

from climatecontroller.libs.managers import (temperature_manager,
											 humidity_manager,
											 carbondioxide_manager)

def delete_data():
    temperature_manager.delete_obsolete_data()
    humidity_manager.delete_obsolete_data()
    carbondioxide_manager.delete_obsolete_data()


delete_data()
