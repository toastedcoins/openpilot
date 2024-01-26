

import abc
from typing import Dict, Set

from openpilot.selfdrive.manager.process import ManagerProcess

from openpilot.selfdrive.manager.process_config import ATHENA, CALIBRATIOND, LOGCAT, PROCLOG, MODELD, NAVMODELD, LOCATIOND, TORQUED, CONTROLSD, \
                                                       DELETER, NAVD, PARAMSD, PLANNERD, RADARD, TOMBSTONED, UPDATED, UPLOADERD, THERMALD, \
                                                       STATSD, LOGGERD, LOGMESSAGED, ENCODERD, DMONITORINGMODELD, DMONITORINGD, UI, SOUNDD, MICD


Processes = Set[ManagerProcess]

# services that run on all hardware
COMMON_SERVICES: Processes = {
  ATHENA,

  LOGCAT,
  PROCLOG,

  MODELD,
  NAVMODELD,

  LOCATIOND,
  CALIBRATIOND,
  TORQUED,
  CONTROLSD,
  DELETER,
  NAVD,
  PARAMSD,
  PLANNERD,
  RADARD,
  TOMBSTONED,
  UPDATED,
  UPLOADERD,
  STATSD,
  THERMALD,
}

LOGGING_SERVICES: Processes = {
  LOGGERD,
  LOGMESSAGED,
  ENCODERD,
}

DMONITORING_SERVICES: Processes = {
  DMONITORINGMODELD,
  DMONITORINGD,
}

UI_SERVICES: Processes = {
  UI,
  SOUNDD,
  MICD,
}


class BaseConfig(abc.ABC):
  @abc.abstractmethod
  def get_services(self) -> Set[ManagerProcess]:
    pass

  @abc.abstractmethod
  def get_env(self) -> Dict[str, str]:
    pass
