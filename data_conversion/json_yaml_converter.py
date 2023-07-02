import os
import json
import yaml

class JsonYamlConverter:
    def __init__(self, read_file_path):
        self.read_file_path = read_file_path

    def to_object(self, src_file_type):
        with open(self.read_file_path, "r") as f:
            file_str = f.read()
            if src_file_type == "json":
                py_obj = json.loads(file_str)
            elif src_file_type == "yaml":
                py_obj = yaml.safe_load(file_str)
        return py_obj
            
    def yaml_dump(self, dump_dst, dump_file_name):
        py_obj = self.to_object("json")
        with open(os.path.join(dump_dst, dump_file_name), "w") as f:
            yaml.dump(py_obj, f)

    def json_dump(self, dump_dst, dump_file_name):
        py_obj = self.to_object("yaml")
        with open(os.path.join(dump_dst, dump_file_name), "w") as f:
            json.dump(py_obj, f, indent=2)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, "sample_data")

    json_file_name = "sample.json"
    json_file_path = os.path.join(data_dir, json_file_name)
    json_to_yaml_converter = JsonYamlConverter(json_file_path)
    yaml_dst_dir = data_dir
    yaml_file_name = "dump.yml"
    json_to_yaml_converter.yaml_dump(yaml_dst_dir, yaml_file_name)

    yaml_file_name = "sample.yml"
    yaml_file_path = os.path.join(data_dir, yaml_file_name)
    yaml_to_json_converter = JsonYamlConverter(yaml_file_path)
    json_dst_dir = data_dir
    json_file_name = "dump.json"
    yaml_to_json_converter.json_dump(json_dst_dir, json_file_name)