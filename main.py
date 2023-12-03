import argparse
import json
import re
from logging import config, getLogger
from typing import Optional
# from src.libs.s3 import get_list_buckets_with_prefix
from src.service.common.bridge import CommonBridge
from src.service.terraform.state import State

from src.template.format import Format


logger = getLogger(__name__)


def json_open(file_path: str) -> dict:
    json_data = open(file=file_path, mode="r")
    return json.load(json_data)

def main(args):
    logger.info(f"start tf-doc file: {args.file}")
    data = None

    try:
        data = json_open(args.file)
    except Exception as e:
        logger.error(e)
        exit(-1)

    data = State().parse(data).get("resources", [])

    # sorted by type
    data = sorted(data, key=lambda x: x["type"])

    aws = CommonBridge()
    result = ""
    aws.service_bridge(data, Format.XLSX, filename=args.output)

    logger.info(f"end tf-doc file: {args.file}")


# def test_main():
#     res = get_list_buckets_with_prefix("test")
#     print(res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    parser.add_argument("--output")
    args = parser.parse_args()
    with open("./log_config.json", "r") as f:
        log_conf = json.load(f)
    config.dictConfig(log_conf)
    main(args=args)