
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_watermark.Config'

LEONARDO_OPTGROUP = 'Watermark'
LEONARDO_APPS = ['leonardo_watermark', 'watermark']

class Config(AppConfig):
    name = 'leonardo_watermark'
    verbose_name = _("Watermark")
