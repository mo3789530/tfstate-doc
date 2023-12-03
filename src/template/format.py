from enum import Enum

class Format(Enum):
    MD=1
    HTML=2
    CSV=3
    XLSX=4
    
    def to_format(s: str): 
        if s == "html" or s == "HTML":
            return Format.HTML
        elif s == "csv" or s == "CSV":
            return Format.CSV
        elif s == "xlsx" or s == "XLSX":
            return Format.XLSX
        # return default value
        return Format.MD
        
        