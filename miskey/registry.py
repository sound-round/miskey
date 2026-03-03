from typing import Final

from .layouts import (
    EN_TO_RU_BASE,
    EN_TO_RU_SHIFTED,
    RU_TO_EN_BASE,
    RU_TO_EN_SHIFTED,
    build_layout,
)

TranslationTable = dict[int, str]

EN_TO_RU_TABLE: Final[TranslationTable] = str.maketrans(
    build_layout(EN_TO_RU_BASE, EN_TO_RU_SHIFTED)
)
RU_TO_EN_TABLE: Final[TranslationTable] = str.maketrans(
    build_layout(RU_TO_EN_BASE, RU_TO_EN_SHIFTED)
)

LANGUAGE_TABLES: Final[dict[str, TranslationTable]] = {
    "en-ru": EN_TO_RU_TABLE,
    "ru-en": RU_TO_EN_TABLE,
}


def get_language_table(language: str) -> TranslationTable:
    try:
        return LANGUAGE_TABLES[language]
    except KeyError as error:
        supported_languages = ", ".join(sorted(LANGUAGE_TABLES))
        message = (
            f"Unsupported language pair '{language}'. "
            f"Supported language pairs: {supported_languages}"
        )
        raise ValueError(
            message,
        ) from error
