# miskey

`miskey` is a lightweight Python library for converting text typed with the wrong keyboard layout.

Supported directions:
- `en-ru` - from English layout to Russian
- `ru-en` - from Russian layout to English

## Installation

### From PyPI

```bash
pip install miskey
```

## Quick Start

```python
from miskey import miskey

print(miskey("ghbdtn", "en-ru"))   # привет
print(miskey("Vjcrdf", "en-ru"))   # Москва
print(miskey("руддщ", "ru-en"))   # hello
```

Characters that are not present in the mapping are kept as-is:

```python
from miskey import miskey

print(miskey("ghbdtn! vbh 123", "en-ru"))  # привет! мир 123
```

## API

### `miskey(text: str, language: str) -> str`

- `text` - input string
- `language` - conversion direction (for example, `en-ru`)

Raises:
- `TypeError` if `text` or `language` is not a string
- `ValueError` if `language` is empty or unsupported

## Requirements

- Python `>=3.13`

## License

MIT
