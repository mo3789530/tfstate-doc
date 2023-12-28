import json
from logging import getLogger
from multiprocessing.spawn import prepare

from src.libs.pretty import pretty_json, pretty_array

logger = getLogger("src").getChild(__name__)


class CommonParser:
    def __init__(self) -> None:
        pass

    def parser(self, json_data: dict, type_str: str, pretty: bool):
        data = {}
        for k in json_data.keys():
            if pretty:
                v = self.format(k, json_data[k])
                data[k] = v if v != "" else "None"
            else:
                data[k] = json_data[k]
        data["type"] = type_str
        # print(data)
        return data

    def format(self, key: str, data: any):
        v = data
        if type(data) is dict:
            v = pretty_json(json.dumps(data))
        elif type(data) is list:
            v = pretty_array(json.dumps(data))
        elif data == "null" or data == None:
            v = "None"

        if key == "json" or "policy" in key:
            try:
                v = pretty_json(data)
            except:
                logger.debug(f"error: key: {key}, data: {data}")
                pass

        return v
