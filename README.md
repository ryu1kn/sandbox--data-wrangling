
# Sandbox: Data Wrangling

Playing with

* PyArrow
* DuckDB
* Polars

## Usage

```sh
poetry install
poetry run scripts/prepare-data.py
```

Then go play with notebooks under [notebooks](./notebooks) directory :)

## Troubleshooting

While installing dependencies with poetry, if `debugpy` installation fails, you may
temporarily disable `modern-installation`. See https://github.com/microsoft/debugpy/issues/1246

```sh
poetry config installer.modern-installation false
```

## References

* [Polars](https://pola-rs.github.io/polars-book/user-guide/introduction.html)
* [DuckDB](https://duckdb.org/)
