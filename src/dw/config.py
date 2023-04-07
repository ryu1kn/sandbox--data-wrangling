from enum import StrEnum

from dw.sample_data import get_data_dir


class DataDir(StrEnum):
    SOURCE = get_data_dir("source")
    OUT_1 = get_data_dir("out-1")
