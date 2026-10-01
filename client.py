"""Fetch and verify the public pagination fixture. Python 3 standard library only."""
import json
from urllib.request import Request, urlopen

ORIGIN = 'https://lumen-data.daviddalmaso.chatgpt.site'
def main():
    items, offset, pages = [], 0, 0
    while offset is not None:
        request = Request(f"{ORIGIN}/api/fixtures/pagination?offset={offset}&limit=20&via=example-client")
        with urlopen(request, timeout=15) as response:
            page = json.load(response)
        items.extend(page['items'])
        offset = page['next_offset']
        pages += 1
        if pages > 10: raise RuntimeError('Unexpected pagination loop')
    assert [row['id'] for row in items] == list(range(1, 104))
    print(f'Verified {len(items)} records across {pages} pages.')
if __name__ == '__main__': main()
