# -*- encoding: utf-8 -*-
# Author: Roger·J
# Date: 2022/9/9 16:38
# File: logger.py

import logging.config
from config.log_config import LOGGING_DIC

logging.config.dictConfig(LOGGING_DIC)
log = logging.getLogger(__name__)
