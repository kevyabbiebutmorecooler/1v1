"""
Character Emoji Mapping
Maps character names to their custom emojis
"""

# Character emoji mappings
CHARACTER_EMOJIS = {
    "Slasher": "<:firejason:1468043640139022632>",
    # Add more character emojis here as needed
}


def format_character_name(character_name: str) -> str:
    """
    Format character name with emoji if available
    
    Args:
        character_name: The character name (e.g., "Slasher")
    
    Returns:
        Formatted string with emoji (e.g., "Slasher <:firejason:1468043640139022632>")
    """
    if character_name in CHARACTER_EMOJIS:
        return f"{character_name} {CHARACTER_EMOJIS[character_name]}"
    return character_name


def get_character_emoji(character_name: str) -> str:
    """
    Get just the emoji for a character
    
    Args:
        character_name: The character name
    
    Returns:
        The emoji string or empty string if no emoji exists
    """
    return CHARACTER_EMOJIS.get(character_name, "")
