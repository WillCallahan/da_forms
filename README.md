# ReportLab - DA Form 2024

Generates a fillable [DA Form 2404](./docs/DA2404_Sample.pdf) via [ReportLab](https://www.reportlab.com/). Fields
may be easily filled by providing the corresponding fields names to the [Da2404 Class](./da2404/models.py) model.

![DA2404 Sample](./docs/da2404_screenshot.png)

## Installation

Install dependencies using Poetry.

```shell
poetry install
```

## Execution

Generate a form by executing the `generate` script via Poetry.

```shell
poetry run generate
```

## Testing

Execute tests using PyTest.

```shell
poetry run pytest
```

## Dependencies

- Python 3.13
- [Poetry](https://python-poetry.org/)