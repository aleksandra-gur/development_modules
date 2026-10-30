def format_title(text: str) -> str:
    """заголовок красивый."""
    return text.strip().title()

def format_kopeks(amount: int) -> str:
    """копейки в рубли."""
    return f"{amount / 100:.2f} руб."