from pathlib import Path
import json

def get_app_resources_path() -> Path:

    resources_path = get_app_src_path().joinpath("resources")
    return resources_path

def get_app_src_path() -> Path:

    src_path = Path(__file__).parent.parent
    return src_path

def get_app_data_path() -> Path:

    data_path = get_app_src_path().parent.joinpath("data")
    return data_path


def get_inventory_details_from_file() -> Path:


    with open(get_app_data_path().joinpath("inventory.json")) as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    get_inventory_details_from_file()