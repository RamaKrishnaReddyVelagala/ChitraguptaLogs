import logging.config

logger = logging.getLogger("myapp")
# Here try to get name of the ml model we have.
import os
print(os.path.basename(os.getcwd()))
