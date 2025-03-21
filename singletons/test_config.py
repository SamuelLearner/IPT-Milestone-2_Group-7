import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from singletons.config_manager import ConfigManager
from singletons.logger_singleton import LoggerSingleton  

config1 = ConfigManager()
config2 = ConfigManager()
logger1 = LoggerSingleton().get_logger()
logger2 = LoggerSingleton().get_logger()

assert config1 is config2
assert logger1 is logger2   
config1.set_setting("DEFAULT_PAGE_SIZE", 50)
assert config2.get_setting("DEFAULT_PAGE_SIZE") == 50
logger1.info("This is a test log message.")
logger2.warning("This is a warning log message.")

print("Singleton test passed!")
print("Logger Singleton test passed!")
