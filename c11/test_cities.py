from city_functions import city_country

def test_city_country():
    formatted_city = city_country("bristol", "Connecticut")
    assert formatted_city == "Bristol, Connecticut"

def test_city_country_population():
    formatted_city = city_country("San Francisco", "California", 808988)
    assert formatted_city == "San Francisco, California - Population 808988"

