def truncate_text(text, max_length=1000):
    """
    Truncate a given text to a maximum specified length.
    
    Args:
        text (str): The input text to truncate.
        max_length (int): The maximum allowed length.
        
    Returns:
        str: Truncated text.
    """
    return text[:max_length].strip() if text else ""