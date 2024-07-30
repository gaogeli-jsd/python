# このファイルを次のようにして読み込みます。

import yaml
from logging import config, getLogger

config.dictConfig(yaml.safe_load(open("config.yaml").read()))
logger = getLogger("exampleLogger")
logger.error("This is ERROR message.")

