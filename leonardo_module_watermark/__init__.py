
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_module_watermark.Config'

LEONARDO_OPTGROUP = 'Watermark'
LEONARDO_APPS = ['leonardo_module_watermark', 'watermark']

class Config(AppConfig):
    name = 'leonardo_module_watermark'
    verbose_name = _("Watermark")
