from .registry import get_language_table


def convert(text: str, language: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(language, str):
        raise TypeError("language must be a string")
    if not language:
        raise ValueError("language must not be empty")

    table = get_language_table(language.lower())
    return text.translate(table)
