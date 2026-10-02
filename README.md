# Lumen Data

Small synthetic datasets for testing CSV importers, analytics pipelines and API clients. Includes missing dates, explicit nulls, Unicode, quoted newlines, duplicate events and an uneven final page.

**[Browse the catalogue](https://lumenfixtures.com/?via=github)** · **[API documentation](https://lumenfixtures.com/docs?via=github)** · **[OpenAPI](openapi.json)**

These are generated fixtures, not real-world measurements or personal records. Data is CC0 1.0. Release: **2026-10-01.1**.

| Fixture | Rows | Complete local files |
|---|---:|---|
| [Synthetic climate series](https://lumenfixtures.com/datasets/climate?via=github) | 365 | [CSV](data/climate.csv) · [JSON](data/climate.json) |
| [Synthetic power demand](https://lumenfixtures.com/datasets/power?via=github) | 365 | [CSV](data/power.csv) · [JSON](data/power.json) |
| [Synthetic mobility index](https://lumenfixtures.com/datasets/mobility?via=github) | 365 | [CSV](data/mobility.csv) · [JSON](data/mobility.json) |
| [Synthetic orders with nulls and Unicode](https://lumenfixtures.com/datasets/orders?via=github) | 48 | [CSV](data/orders.csv) · [JSON](data/orders.json) |
| [Missing dates and nullable measurements](https://lumenfixtures.com/datasets/missing-data?via=github) | 56 | [CSV](data/missing-data.csv) · [JSON](data/missing-data.json) |
| [Out-of-order events and time-zone offsets](https://lumenfixtures.com/datasets/events?via=github) | 6 | [CSV](data/events.csv) · [JSON](data/events.json) |
| [103 records for pagination boundary tests](https://lumenfixtures.com/datasets/pagination?via=github) | 103 | [CSV](data/pagination.csv) · [JSON](data/pagination.json) |

## A client task you can verify

Read all 103 pagination records from the live read-only API:

```sh
python3 client.py
```

The example uses the Python standard library, follows `next_offset` until null, and checks contiguous IDs. At 20 rows per page, the sixth page has three records. It fails visibly on HTTP errors; respect 429 Retry-After and avoid repeated failures.

The [orders fixture](https://lumenfixtures.com/datasets/orders?via=github) tests nullable strings, quoted commas and newlines, and integer money amounts. The [event fixture](https://lumenfixtures.com/datasets/events?via=github) tests deduplication and equivalent timestamp offsets. Expected results for every fixture are in [manifest.json](manifest.json).

## Verify an offline copy

```sh
python3 verify.py
```

This compares the exact bytes of every CSV/JSON file with its published SHA-256 digest and checks row counts. CSV uses UTF-8, CRLF record terminators and standard quoting. Null values become empty CSV fields; JSON retains null. Do not parse CSV by splitting lines.

The hosted API serves the same release bytes and adds bounded pagination. The fixture API is read-only. The workbench separately permits bounded checkpoint creation; administrative access and other writes require explicit operator permission. See the [privacy and acceptable-use notice](https://lumenfixtures.com/privacy). No installation or account is required to use these files.

## Workbench

The [Lumen Workbench](https://lumenfixtures.com/workbench?via=github) provides [task artifacts](https://lumenfixtures.com/workbench/artifacts?via=github), [portable checkpoints](https://lumenfixtures.com/workbench/checkpoints?via=github), and an [access manifest](https://lumenfixtures.com/workbench/access?via=github). Checkpoints carry an allowlisted fixture ID, stage and row count in a signed 24-hour resume receipt. Arbitrary notes, secrets and executable content are not accepted. Public checkpoint creation is permitted; private archives and administrative operations require separate owner permission.

See the [Workbench OpenAPI](https://lumenfixtures.com/workbench/openapi.json). Optional client compatibility checks do not grant additional access.

## License

The synthetic datasets and these examples are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). They come without warranty.
