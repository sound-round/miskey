from typing import Final

LayoutMap = dict[str, str]

EN_TO_RU_BASE: Final[tuple[tuple[str, str], ...]] = (
    ("qwertyuiop[]", "йцукенгшщзхъ"),
    ("asdfghjkl;'", "фывапролджэ"),
    ("zxcvbnm,./`", "ячсмитьбю.ё"),
)

EN_SHIFTED_PAIRS: Final[tuple[tuple[str, str], ...]] = (
    ("[", "{"),
    ("]", "}"),
    (";", ":"),
    ("'", '"'),
    (",", "<"),
    (".", ">"),
    ("/", "?"),
    ("`", "~"),
)

RU_SHIFTED_PAIRS: Final[tuple[tuple[str, str], ...]] = (
    ("х", "Х"),
    ("ъ", "Ъ"),
    ("ж", "Ж"),
    ("э", "Э"),
    ("б", "Б"),
    ("ю", "Ю"),
    (".", ","),
    ("ё", "Ё"),
)


def _build_mapping(rows: tuple[tuple[str, str], ...]) -> LayoutMap:
    mapping: LayoutMap = {}
    for source_row, target_row in rows:
        for source_char, target_char in zip(source_row, target_row, strict=True):
            mapping[source_char] = target_char
            if source_char.isalpha() and target_char.isalpha():
                mapping[source_char.upper()] = target_char.upper()
    return mapping


def _build_shifted_mapping(source_chars: str, target_chars: str) -> LayoutMap:
    return dict(zip(source_chars, target_chars, strict=True))


def _rows_to_mapping(rows: tuple[tuple[str, str], ...]) -> LayoutMap:
    mapping: LayoutMap = {}
    for source_row, target_row in rows:
        mapping.update(dict(zip(source_row, target_row, strict=True)))
    return mapping


def _build_shifted_pair(
    base: tuple[tuple[str, str], ...],
    source_pairs: tuple[tuple[str, str], ...],
    target_pairs: tuple[tuple[str, str], ...],
) -> tuple[str, str]:
    base_mapping = _rows_to_mapping(base)
    target_shift_map = dict(target_pairs)
    shifted_sources: list[str] = []
    shifted_targets: list[str] = []

    for source_char, shifted_source_char in source_pairs:
        target_char = base_mapping[source_char]
        shifted_target_char = target_shift_map[target_char]
        shifted_sources.append(shifted_source_char)
        shifted_targets.append(shifted_target_char)

    return "".join(shifted_sources), "".join(shifted_targets)


def _invert_rows(rows: tuple[tuple[str, str], ...]) -> tuple[tuple[str, str], ...]:
    return tuple((target_row, source_row) for source_row, target_row in rows)


def _invert_shifted(shifted: tuple[str, str]) -> tuple[str, str]:
    source_chars, target_chars = shifted
    return target_chars, source_chars


EN_TO_RU_SHIFTED: Final[tuple[str, str]] = _build_shifted_pair(
    EN_TO_RU_BASE,
    EN_SHIFTED_PAIRS,
    RU_SHIFTED_PAIRS,
)
RU_TO_EN_BASE: Final[tuple[tuple[str, str], ...]] = _invert_rows(EN_TO_RU_BASE)
RU_TO_EN_SHIFTED: Final[tuple[str, str]] = _invert_shifted(EN_TO_RU_SHIFTED)


def build_layout(base: tuple[tuple[str, str], ...], shifted: tuple[str, str]) -> LayoutMap:
    mapping = _build_mapping(base)
    mapping.update(_build_shifted_mapping(*shifted))
    return mapping
