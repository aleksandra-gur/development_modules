def normalize_name(name: str) -> str:
    """к нормальному виду."""
    return " ".join(name.split()).title()

def _squash_spaces(text: str) -> str:
    return " ".join(text.split())