def city_country(city, country, population=''):
    """Formats city and country."""
    if population:
        formatted = f"{city}, {country} - population {population}"
    else:
        formatted = f"{city}, {country}"
    return formatted.title()
