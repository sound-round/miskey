from .layouts import LayoutMap


def convert_text(text: str, layout: LayoutMap) -> str:
    return "".join(layout.get(char, char) for char in text)
