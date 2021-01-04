import json
import os

class ConfigURL:
    @classmethod
    def generate_config_object(self):
        site_mapping_dir = "site_mapping"
        file_list = os.listdir(site_mapping_dir)
        configURL = dict()
        for file in file_list:
            file_path = os.path.join(site_mapping_dir, file)
            with open(file_path) as json_file:
                data = json.load(json_file)
            configURL[data["domain"]] = data["config"]
        return configURL
