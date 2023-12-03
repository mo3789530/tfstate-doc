from logging import getLogger
import re
from typing import Optional
from src.libs.html import md_to_html, save
from src.libs.md import is_exist_md, write_md
from src.service.common.parser import CommonParser

from src.libs.pretty import pretty_markdown
from src.libs.xlsx import ExcelWriter
from src.template.format import Format
from src.template.markdown import MarkdownTemplateCommon


logger = getLogger("src").getChild(__name__)

class CommonBridge():

    def __init__(self) -> None:
        pass

    def service_bridge(self, dic: list, format: Format, filename: str) -> str:
        res = []
        pretty = False
        if format == format.MD or format == Format.HTML:
            pretty = True
        for d in dic:
            data = CommonParser().parser(json_data=d.get("attributes", {}), type_str=d.get("type", ""), pretty=pretty)
            if type(data) != dict:
                raise Exception("Error parsed data type")
            res.append(data)
        logger.debug(format)
        if format == Format.HTML:
            pass
        elif format == Format.XLSX:
            self.__create_xlsx(data=res, name=filename)
        else:
            self.__create_markdown(data=res, name=filename)

    
    def __create_markdown(self, data: list, name: str) -> str:
        dst = ""
        for d in data:
            dst += pretty_markdown(MarkdownTemplateCommon().create_markdown_facade(data=d, common_type=d['type']))
            dst += "\n"
        
        self.output(file_name=name, output=None, format="md", data=dst)


    def output(self, file_name: str, output: Optional[str], format: Optional[str], data: str):
        # file check
        if output == None:
            if format == "html":
                output = re.sub(".json", ".html", file_name)
            elif format == "md":
                output = re.sub(".json", ".md", file_name)
                is_exist_md(output)
        else:
            output = output

        if format == "html":
            save(output=output, html=md_to_html(data))
        else:
            write_md(output=output, dst=data)

    def __create_xlsx(self, data: list, name: str) -> str:
        xlsx = ExcelWriter()
        xlsx.write_sheet(dic=data, name=name)
        xlsx.save_workbook("aaa")
        return "aaa.xlsx"