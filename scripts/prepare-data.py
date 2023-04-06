#!/usr/bin/env python
# coding: utf-8
#
# Usage:
#
#     poetry run scripts/prepare-data.py
#
from os import makedirs
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.dataset as ds
import numpy as np

from dw.data import human_readable_size
from dw.sample_data import get_data_dir
from shutil import rmtree

sample_size = 1_000_000
data_dir = get_data_dir()

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sapien tellus,
aliquet eu semper ut, faucibus in augue. Donec mollis nisi vitae nulla tristique, ut
iaculis tortor ultricies. Nullam finibus tortor eros, et elementum dolor lacinia et.
In hac habitasse platea dictumst. Ut a tempus tellus. Nam hendrerit luctus nisi, at
condimentum nibh. Morbi sed eleifend dui. Donec pellentesque efficitur nunc ut consequat.
In id varius magna, sed accumsan elit. Maecenas lobortis lectus nec fermentum lacinia.
Suspendisse placerat euismod sem eu pretium. Sed efficitur, dolor sed aliquet molestie,
mauris enim tristique nulla, in elementum erat velit quis diam. Ut non nisi quis tellus
iaculis lacinia vel non sapien. Fusce eget dui ullamcorper, semper ipsum non, convallis
mauris. Donec rutrum diam nisi, id tempus sapien pharetra eu. Nunc tempus varius erat,
ultricies congue est aliquam sed."""


def main():
    clear_data_dir()
    create_data()
    report_data_stats()
    print("...Done!")


def clear_data_dir():
    print_heading(f"Preparing data directory at: {get_data_dir}")
    rmtree(get_data_dir, ignore_errors=True)
    makedirs(get_data_dir)


def create_data():
    print_heading(f"Creating data files under: {get_data_dir}")
    for n in range(10):
        print(f"Saving parquet file part {n}")
        t = pa.table({
            "id": list(range(n * sample_size, (n + 1) * sample_size)),
            "text": [text * 3] * sample_size,
            "to_be_ignored": np.random.randint(30, size=sample_size)
        })
        pq.write_table(t, f"{get_data_dir}/part-{n}.parquet")


def report_data_stats():
    print_heading("Data stats")
    rows = ds.dataset(get_data_dir, format="parquet").count_rows()
    print(f"Number of rows: {rows}")

    dir_size = sum(f.stat().st_size for f in Path(get_data_dir).glob('**/*') if f.is_file())
    print(f"Data size: {human_readable_size(dir_size)}")


def print_heading(message): print(f"\n>>> {message}")


if __name__ == "__main__":
    main()
