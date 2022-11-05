#!/usr/bin/env python3

import os
import pibooth
from pibooth.utils import LOGGER
import cec

__version__ = "1.0.0"

SECTION='HDMI_CEC'

@pibooth.hookimpl
def pibooth_startup(cfg, app):
    cec.init()
    app.tv = cec.Device(cec.CECDEVICE_TV)
    app.tv.power_on()


# @pibooth.hookimpl
# def pibooth_cleanup(app):
#     app.tv.standby()