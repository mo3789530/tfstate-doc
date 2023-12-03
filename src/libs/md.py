import os
from logging import getLogger

logger = getLogger("src").getChild(__name__)  # type: ignore


def is_exist_md(file_name: str):
    if os.path.isfile(file_name) == True:
        logger.warn(f"Deleting exist file: {file_name} ")
        os.remove(file_name)


def write_md(output: str, dst: str):
    with open(output, mode='a') as f:
        f.write(dst)
        f.write("\n")