from typing import Any

import pytest

from miskey import miskey


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("rjywthn", "концерт"),
        ("ghbdtn", "привет"),
        ("Vjcrdf", "Москва"),
    ],
)
def test_convert_en_to_ru_words(source: str, expected: str) -> None:
    assert miskey(source, "en-ru") == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("концерт", "rjywthn"),
        ("привет", "ghbdtn"),
        ("Москва", "Vjcrdf"),
    ],
)
def test_convert_ru_to_en_words(source: str, expected: str) -> None:
    assert miskey(source, "ru-en") == expected


def test_mixed_text_keeps_unmapped_characters() -> None:
    source = "ghbdtn! vbh 123"
    assert miskey(source, "en-ru") == "привет! мир 123"


def test_full_english_alphabet_to_russian() -> None:
    source = "abcdefghijklmnopqrstuvwxyz"
    expected = "фисвуапршолдьтщзйкыегмцчня"
    assert miskey(source, "en-ru") == expected


def test_full_russian_alphabet_to_english() -> None:
    source = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    expected = "f,dult`;pbqrkvyjghcnea[wxio]sm'.z"
    assert miskey(source, "ru-en") == expected


def test_full_english_alphabet_uppercase_to_russian() -> None:
    source = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    expected = "ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ"
    assert miskey(source, "en-ru") == expected


def test_full_russian_alphabet_uppercase_to_english() -> None:
    source = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    expected = 'F<DULT~:PBQRKVYJGHCNEA{WXIO}SM">Z'
    assert miskey(source, "ru-en") == expected


def test_unsupported_language_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Unsupported language"):
        miskey("hello", "de-en")


def test_empty_language_raises_value_error() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        miskey("hello", "")


def test_non_string_arguments_raise_type_error() -> None:
    invalid_text: Any = 1
    invalid_language: Any = 1

    with pytest.raises(TypeError, match="text must be a string"):
        miskey(invalid_text, "en-ru")

    with pytest.raises(TypeError, match="language must be a string"):
        miskey("test", invalid_language)
