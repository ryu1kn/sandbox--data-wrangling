from pathlib import Path


def get_data_dir(): return str(Path(__file__, "../../../tmp").resolve())
