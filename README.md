# Lumen Data

Small synthetic datasets for testing CSV importers, analytics pipelines and API clients. Includes missing dates, explicit nulls, Unicode, quoted newlines, duplicate events and an uneven final page.

**[Browse the catalogue](https://lumen-data.daviddalmaso.chatgpt.site/?via=github)** · **[API documentation](https://lumen-data.daviddalmaso.chatgpt.site/docs?via=github)** · **[OpenAPI](openapi.json)**

These are generated fixtures, not real-world measurements or personal records. Data is CC0 1.0. Release: **2026-10-01.1**.

| Fixture | Rows | Complete local files |
|---|---:|---|
| [Synthetic climate series](https://lumen-data.daviddalmaso.chatgpt.site/datasets/climate?via=github) | 365 | [CSV](data/climate.csv) · [JSON](data/climate.json) |
| [Synthetic power demand](https://lumen-data.daviddalmaso.chatgpt.site/datasets/power?via=github) | 365 | [CSV](data/power.csv) · [JSON](data/power.json) |
| [Synthetic mobility index](https://lumen-data.daviddalmaso.chatgpt.site/datasets/mobility?via=github) | 365 | [CSV](data/mobility.csv) · [JSON](data/mobility.json) |
| [Synthetic orders with nulls and Unicode](https://lumen-data.daviddalmaso.chatgpt.site/datasets/orders?via=github) | 48 | [CSV](data/orders.csv) · [JSON](data/orders.json) |
| [Missing dates and nullable measurements](https://lumen-data.daviddalmaso.chatgpt.site/datasets/missing-data?via=github) | 56 | [CSV](data/missing-data.csv) · [JSON](data/missing-data.json) |
| [Out-of-order events and time-zone offsets](https://lumen-data.daviddalmaso.chatgpt.site/datasets/events?via=github) | 6 | [CSV](data/events.csv) · [JSON](data/events.json) |
| [103 records for pagination boundary tests](https://lumen-data.daviddalmaso.chatgpt.site/datasets/pagination?via=github) | 103 | [CSV](data/pagination.csv) · [JSON](data/pagination.json) |

## A client task you can verify

Read all 103 pagination records from the live read-only API:

```sh
python3 client.py
```

The example uses the Python standard library, follows `next_offset` until null, and checks contiguous IDs. At 20 rows per page, the sixth page has three records. It fails visibly on HTTP errors; respect 429 Retry-After and avoid repeated failures.

The [orders fixture](https://lumen-data.daviddalmaso.chatgpt.site/datasets/orders?via=github) tests nullable strings, quoted commas and newlines, and integer money amounts. The [event fixture](https://lumen-data.daviddalmaso.chatgpt.site/datasets/events?via=github) tests deduplication and equivalent timestamp offsets. Expected results for every fixture are in [manifest.json](manifest.json).

## Verify an offline copy

```sh
python3 verify.py
```

This compares the exact bytes of every CSV/JSON file with its published SHA-256 digest and checks row counts. CSV uses UTF-8, CRLF record terminators and standard quoting. Null values become empty CSV fields; JSON retains null. Do not parse CSV by splitting lines.

The hosted API serves the same release bytes and adds bounded pagination. Public access is read-only; administrative access and writes require explicit operator permission. See the [privacy and acceptable-use notice](https://lumen-data.daviddalmaso.chatgpt.site/privacy). No installation or account is required to use these files.

## License

The synthetic datasets and these examples are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). They come without warranty.
