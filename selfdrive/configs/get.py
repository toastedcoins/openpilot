import os
from openpilot.selfdrive.configs.base import BaseConfig
from openpilot.selfdrive.configs.pc import MetaDriveConfig, PCConfig
from openpilot.selfdrive.configs.three import ThreeConfig
from openpilot.selfdrive.configs.threex import ThreexConfig
from openpilot.system.hardware import PC, SIM, TICI, TIZI


def get_config():
  CONFIG_OVERRIDE = os.environ.get("CONFIG", None)

  if CONFIG_OVERRIDE is not None:
    if CONFIG_OVERRIDE == "sim":
      return MetaDriveConfig()
    elif CONFIG_OVERRIDE == "three":
      return ThreexConfig()
    elif CONFIG_OVERRIDE == "threex":
      return ThreexConfig()
    else:
      raise ValueError(f"Unknown CONFIG_OVERRIDE: {CONFIG_OVERRIDE}")
  else:
    if PC and SIM:
      return MetaDriveConfig()
    elif PC:
      return PCConfig()
    elif TIZI:
      return ThreexConfig()
    elif TICI:
      return ThreeConfig()
    else:
      raise ValueError("No config available for system hardware")


CONFIG: BaseConfig = get_config()
