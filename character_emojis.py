"""
Character Emoji Mapping
Maps character names to their custom emojis
"""

# Character emoji mappings
CHARACTER_EMOJIS = {
    # Killers
    "Slasher": "<:firejason:1468043640139022632>",
    "John Doe": "<:jondo:1468078899672911872>",
    "C00lkidd": "<:coolkid:1468088658363154482>",
    "Nosferatu": "<:nosferatu:1468089157657296938>",
    "1x1x1x1": "<:1x1x1x1:1468089431620845762>",
    "Noli": "<a:noli:1468090156241125586>",  # Animated emoji
    "Guest 666": "<:guest666:1468090686489231655>",
    
    # Survivors
    "Noob": "<:noob:1468090717288005725>",
    "007n7": "<:007n7:1468093770372350064>",
    "Builderman": "<:builderman:1468093749140914360>",
    "Chance": "<:chance:1468093728085508127>",
    "Dusekkar": "<:dusekkar:1468093703846498364>",
    "Elliot": "<:elliot:1468093685576110224>",
    "Guest 1337": "<:guest1337:1468093662926864525>",
    "Shedletsky": "<:shedletsky:1468093609256685679>",
    "Taph": "<:taph:1468093588159205431>",
    "Two Time": "<:twotime:1468093557394116742>",
    "Veeronica": "<:veeronica:1468093535269158983>",
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
