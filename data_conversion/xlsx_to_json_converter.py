import os
import openpyxl as excel
import json

class XlsxToJsonConverter:
    def __init__(self, excel_path):
        self.excel_path = excel_path

    def to_object(self):
        book = excel.load_workbook(self.excel_path)
        sheet = book.active

        data_list = []
        for col in sheet.iter_rows(min_col=2, min_row=2):
            values = [cell.value for cell in col]
            data_list.append(values)

        excel_obj = []
        for i in range(1, len(data_list)):
            data_dict = {}
            for j in range(len(data_list[0])):
                data_dict[data_list[0][j]] = data_list[i][j]
            excel_obj.append(data_dict)
        return excel_obj


    def dump_json(self, dump_dst, dump_file_name):
        excel_obj = self.to_object()
        with open(os.path.join(dump_dst, dump_file_name), "w") as f:
            json.dump(excel_obj, f, indent=2)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, "sample_data")
    excel_path = os.path.join(data_dir, "sample.xlsx")

    xlsx_converter = XlsxToJsonConverter(excel_path)
    
    dump_dst = data_dir
    dump_file_name = "excel.json"
    xlsx_converter.dump_json(dump_dst, dump_file_name)