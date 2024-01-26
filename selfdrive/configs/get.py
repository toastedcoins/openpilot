import os
from typing import Optional
from openpilot.selfdrive.configs.base import BaseConfig
from openpilot.selfdrive.configs.pc import MetaDriveConfig
from openpilot.selfdrive.configs.three import ThreeConfig
from openpilot.selfdrive.configs.threex import ThreexConfig
from openpilot.system.hardware import PC, TICI, TIZI


CONFIG_OVERRIDE = os.environ.get("CONFIG", None)

CONFIG: Optional[BaseConfig] = None

if CONFIG_OVERRIDE is not None:
  if CONFIG_OVERRIDE == "sim":
    CONFIG = MetaDriveConfig()
  elif CONFIG_OVERRIDE == "three":
    CONFIG = ThreexConfig()
  elif CONFIG_OVERRIDE == "threex":
    CONFIG = ThreexConfig()
  else:
    raise ValueError(f"Unknown CONFIG_OVERRIDE: {CONFIG_OVERRIDE}")
else:
  if PC:
    CONFIG = MetaDriveConfig()
  elif TIZI:
    CONFIG = ThreexConfig()
  elif TICI:
    CONFIG = ThreeConfig()
  else:
    raise ValueError("No config available for system hardware")
