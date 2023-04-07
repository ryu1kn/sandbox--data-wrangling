from pathlib import Path


def get_data_dir(id: str):
    repo_root = "../../.."
    return str(Path(__file__, repo_root, "data", id).resolve())
