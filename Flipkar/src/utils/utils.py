from pathlib import Path

def get_inventory_path() -> Path:

    root_path = get_app_src_path().joinpath()
    return root_path

def get_app_src_path() -> Path:

    src_path = Path(__file__).parent.parent
    return src_path