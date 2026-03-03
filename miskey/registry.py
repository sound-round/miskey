from typing import Final

from .layouts import (
    EN_TO_RU_BASE,
    EN_TO_RU_SHIFTED,
    RU_TO_EN_BASE,
    RU_TO_EN_SHIFTED,
    LayoutMap,
    build_layout,
)

EN_TO_RU_LAYOUT: Final[LayoutMap] = build_layout(EN_TO_RU_BASE, EN_TO_RU_SHIFTED)
RU_TO_EN_LAYOUT: Final[LayoutMap] = build_layout(RU_TO_EN_BASE, RU_TO_EN_SHIFTED)

LANGUAGE_LAYOUTS: Final[dict[str, LayoutMap]] = {
    "en-ru": EN_TO_RU_LAYOUT,
    "ru-en": RU_TO_EN_LAYOUT,
}


def get_language_layout(language: str) -> LayoutMap:
    try:
        return LANGUAGE_LAYOUTS[language]
    except KeyError as error:
        supported_languages = ", ".join(sorted(LANGUAGE_LAYOUTS))
        message = (
            f"Unsupported language pair '{language}'. "
            f"Supported language pairs: {supported_languages}"
        )
        raise ValueError(
            message,
        ) from error
