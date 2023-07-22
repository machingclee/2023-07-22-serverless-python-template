import os
from uuid import uuid4

def main (data_source: dict, 
          target_path: str = os.path.abspath(f"/tmp/excel_files/output_excel_{uuid4()}.xlsx")):    
    return target_path