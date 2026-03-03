from .converter import convert_text
from .registry import get_language_layout


def miskey(text: str, language: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(language, str):
        raise TypeError("language must be a string")
    if not language:
        raise ValueError("language must not be empty")

    layout = get_language_layout(language.lower())
    return convert_text(text, layout)
