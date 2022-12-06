###
# Utilidad para gestionar el logger de una aplicación python
# Fork del original de @arnaus@mastodont.cat
# En https://github.com/XaviArnaus/python-bundle
###  

from scr.config import Config
import logging
import sys
import os
import os.path

class Logger:

    def __init__(self, config: Config) -> None:
        log_format    = (config.get("logger.format","[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"))
        log_directory = (config.get("logger.directory", "log"))

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        handlers = []
        if config.get("logger.to_file", False):
            handlers.append(logging.FileHandler(config.get("logger.filename", 'debug.log')))
        if config.get("logger.to_stdout", False):
            handlers.append(logging.StreamHandler(sys.stdout))

        # Define basic configuration
        logging.basicConfig(
            # Define logging level
            level=config.get("logger.loglevel", 20),
            # Define the format of log messages
            format=log_format,
            # Declare handlers
            handlers=handlers
        )
        # Define your own logger name
        self._logger = logging.getLogger(config.get("logger.name", "mastodon_bot"))

    def getLogger(self) -> logging:
        return self._logger