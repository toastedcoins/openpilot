from typing import Dict
from openpilot.selfdrive.configs.base import COMMON_SERVICES, DMONITORING_SERVICES, LOGGING_SERVICES, UI_SERVICES, BaseConfig, Processes
from openpilot.selfdrive.manager.process_config import BOARDD, CAMERAD, PANDAD, PIGEOND, SENSORD, UBLOXD


class ThreeConfig(BaseConfig):
  GPS_SERVICES: Processes = {UBLOXD, PIGEOND,}

  HARDWARE_SERVICES: Processes = {CAMERAD, SENSORD, BOARDD, PANDAD}

  def get_services(self) -> Processes:
    return COMMON_SERVICES | UI_SERVICES | LOGGING_SERVICES | DMONITORING_SERVICES | self.HARDWARE_SERVICES | self.GPS_SERVICES

  def get_env(self) -> Dict[str, str]:
    return {}
