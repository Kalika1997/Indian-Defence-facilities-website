from django.apps import AppConfig
from sms.signals import create_profile,save_profile

class SmsConfig(AppConfig):
    name = 'sms'


