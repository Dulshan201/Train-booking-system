# 🌍 Worldwide Cities Database by Country
# Supporting comprehensive train booking system for the entire world

# Country-based cities database with comprehensive coverage
COUNTRIES_AND_CITIES = {
    # 🇺🇸 United States
    "United States": [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
        "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus",
        "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington DC", "Boston",
        "El Paso", "Nashville", "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis",
        "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento",
        "Kansas City", "Mesa", "Atlanta", "Colorado Springs", "Omaha", "Raleigh", "Miami", "Oakland",
        "Minneapolis", "Tulsa", "Cleveland", "Wichita", "Arlington", "Tampa", "New Orleans",
        "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi",
        "Lexington", "Pittsburgh", "Anchorage", "Stockton", "Cincinnati", "Saint Paul", "Buffalo"
    ],
    
    # 🇨🇦 Canada
    "Canada": [
        "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg",
        "Quebec City", "Hamilton", "Kitchener", "London", "Victoria", "Halifax", "Oshawa",
        "Windsor", "Saskatoon", "Regina", "Sherbrooke", "St. John's", "Barrie", "Kelowna",
        "Abbotsford", "Greater Sudbury", "Kingston", "Saguenay", "Trois-Rivières", "Guelph",
        "Cambridge", "Whitby", "Coquitlam", "Saanich", "Milton", "Thunder Bay", "Burlington"
    ],
    
    # 🇬🇧 United Kingdom
    "United Kingdom": [
        "London", "Birmingham", "Manchester", "Glasgow", "Liverpool", "Leeds", "Sheffield",
        "Edinburgh", "Bristol", "Cardiff", "Leicester", "Coventry", "Belfast", "Nottingham",
        "Kingston upon Hull", "Newcastle upon Tyne", "Stoke-on-Trent", "Southampton", "Derby",
        "Portsmouth", "Brighton", "Plymouth", "Northampton", "Reading", "Luton", "Wolverhampton"
    ],
    
    # 🇩🇪 Germany
    "Germany": [
        "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Düsseldorf", "Leipzig",
        "Dortmund", "Essen", "Bremen", "Dresden", "Hannover", "Nuremberg", "Duisburg", "Bochum",
        "Wuppertal", "Bielefeld", "Bonn", "Münster", "Mannheim", "Augsburg", "Wiesbaden", "Gelsenkirchen",
        "Mönchengladbach", "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Halle", "Magdeburg", "Freiburg"
    ],
    
    # 🇫🇷 France
    "France": [
        "Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier",
        "Bordeaux", "Lille", "Rennes", "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble",
        "Dijon", "Angers", "Villeurbanne", "Saint-Denis", "Le Mans", "Aix-en-Provence", "Clermont-Ferrand",
        "Brest", "Tours", "Limoges", "Amiens", "Annecy", "Perpignan", "Boulogne-Billancourt"
    ],
    
    # 🇪🇸 Spain
    "Spain": [
        "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", "Málaga", "Murcia", "Palma",
        "Las Palmas", "Bilbao", "Alicante", "Córdoba", "Valladolid", "Vigo", "Gijón", "L'Hospitalet",
        "A Coruña", "Granada", "Vitoria-Gasteiz", "Elche", "Santa Cruz de Tenerife", "Oviedo",
        "Badalona", "Cartagena", "Terrassa", "Jerez de la Frontera", "Sabadell", "Móstoles"
    ],
    
    # 🇮🇹 Italy
    "Italy": [
        "Rome", "Milan", "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Bari",
        "Catania", "Venice", "Verona", "Messina", "Padua", "Trieste", "Taranto", "Brescia",
        "Prato", "Reggio Calabria", "Modena", "Reggio Emilia", "Perugia", "Livorno", "Ravenna",
        "Cagliari", "Foggia", "Rimini", "Salerno", "Ferrara", "Sassari", "Latina", "Giugliano"
    ],
    
    # 🇯🇵 Japan
    "Japan": [
        "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kobe", "Kawasaki", "Kyoto",
        "Saitama", "Hiroshima", "Sendai", "Kitakyushu", "Chiba", "Sakai", "Niigata", "Hamamatsu",
        "Okayama", "Sagamihara", "Shizuoka", "Kumamoto", "Kagoshima", "Matsuyama", "Kanazawa",
        "Utsunomiya", "Matsudo", "Kawaguchi", "Takasaki", "Oita", "Nara", "Toyama", "Nagasaki"
    ],
    
    # 🇰🇷 South Korea
    "South Korea": [
        "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Suwon", "Ulsan", "Changwon",
        "Goyang", "Yongin", "Bucheon", "Cheongju", "Ansan", "Jeonju", "Anyang", "Pohang", "Uijeongbu",
        "Siheung", "Cheonan", "Hwaseong", "Gimhae", "Gumi", "Pyeongtaek", "Jinju", "Gunpo", "Osan"
    ],
    
    # 🇨🇳 China
    "China": [
        "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Tianjin", "Wuhan", "Dongguan", "Chengdu",
        "Nanjing", "Chongqing", "Xi'an", "Shenyang", "Hangzhou", "Foshan", "Zhengzhou", "Qingdao",
        "Dalian", "Jinan", "Kunming", "Harbin", "Fuzhou", "Changchun", "Stone Mountain", "Wenzhou",
        "Hefei", "Changsha", "Shijiazhuang", "Taiyuan", "Xuzhou", "Yantai", "Huizhou", "Weifang"
    ],
    
    # 🇮🇳 India
    "India": [
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat",
        "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam",
        "Pimpri-Chinchwad", "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad",
        "Meerut", "Rajkot", "Kalyan-Dombivali", "Vasai-Virar", "Varanasi", "Srinagar", "Dhanbad"
    ],
    
    # 🇦🇺 Australia
    "Australia": [
        "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle",
        "Canberra", "Sunshine Coast", "Wollongong", "Hobart", "Geelong", "Townsville",
        "Cairns", "Darwin", "Toowoomba", "Ballarat", "Bendigo", "Albury", "Launceston",
        "Mackay", "Rockhampton", "Bunbury", "Bundaberg", "Coffs Harbour", "Wagga Wagga"
    ],
    
    # 🇳🇿 New Zealand
    "New Zealand": [
        "Auckland", "Wellington", "Christchurch", "Hamilton", "Tauranga", "Napier-Hastings",
        "Dunedin", "Palmerston North", "Nelson", "Rotorua", "New Plymouth", "Whangarei",
        "Invercargill", "Whanganui", "Gisborne", "Timaru", "Pukekohe", "Papakura"
    ],
    
    # 🇧🇷 Brazil
    "Brazil": [
        "São Paulo", "Rio de Janeiro", "Salvador", "Brasília", "Fortaleza", "Belo Horizonte",
        "Manaus", "Curitiba", "Recife", "Porto Alegre", "Belém", "Goiânia", "Guarulhos",
        "Campinas", "São Luís", "São Gonçalo", "Maceió", "Duque de Caxias", "Natal", "Teresina",
        "Campo Grande", "Nova Iguaçu", "São Bernardo do Campo", "João Pessoa", "Santo André"
    ],
    
    # 🇦🇷 Argentina
    "Argentina": [
        "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "Tucumán", "Mar del Plata",
        "Salta", "Santa Fe", "San Juan", "Resistencia", "Santiago del Estero", "Corrientes",
        "Posadas", "Neuquén", "Bahía Blanca", "Paraná", "Formosa", "San Luis", "La Rioja"
    ],
    
    # 🇲🇽 Mexico
    "Mexico": [
        "Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana", "León", "Juárez",
        "Zapopan", "Nezahualcóyotl", "Chihuahua", "Naucalpan", "Mérida", "Álvaro Obregón",
        "San Luis Potosí", "Aguascalientes", "Hermosillo", "Saltillo", "Mexicali", "Culiacán",
        "Guadalupe", "Acapulco", "Tlalnepantla", "Cancún", "Querétaro", "Chimalhuacán"
    ],
    
    # 🇷🇺 Russia
    "Russia": [
        "Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan",
        "Chelyabinsk", "Omsk", "Samara", "Rostov-on-Don", "Ufa", "Krasnoyarsk", "Perm", "Voronezh",
        "Volgograd", "Krasnodar", "Saratov", "Tyumen", "Tolyatti", "Izhevsk", "Barnaul", "Ulyanovsk"
    ],
    
    # Additional countries with major cities
    # 🇪🇬 Egypt
    "Egypt": ["Cairo", "Alexandria", "Giza", "Shubra El Kheima", "Port Said", "Suez", "Luxor", "Mansoura", "El Mahalla El Kubra", "Tanta"],
    
    # 🇿🇦 South Africa
    "South Africa": ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein", "East London", "Nelspruit", "Kimberley", "Polokwane"],
    
    # 🇳🇬 Nigeria
    "Nigeria": ["Lagos", "Kano", "Ibadan", "Kaduna", "Port Harcourt", "Benin City", "Maiduguri", "Zaria", "Aba", "Jos"],
    
    # 🇰🇪 Kenya
    "Kenya": ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Thika", "Malindi", "Kitale", "Garissa", "Kakamega"],
    
    # 🇹🇭 Thailand
    "Thailand": ["Bangkok", "Nonthaburi", "Pak Kret", "Hat Yai", "Chiang Mai", "Phuket", "Pattaya", "Udon Thani", "Nakhon Ratchasima", "Khon Kaen"],
    
    # 🇮🇩 Indonesia
    "Indonesia": ["Jakarta", "Surabaya", "Bandung", "Bekasi", "Medan", "Depok", "Tangerang", "Palembang", "Semarang", "Makassar"],
    
    # 🇵🇭 Philippines
    "Philippines": ["Manila", "Quezon City", "Caloocan", "Davao", "Cebu City", "Zamboanga", "Antipolo", "Pasig", "Taguig", "Valenzuela"],
    
    # 🇻🇳 Vietnam
    "Vietnam": ["Ho Chi Minh City", "Hanoi", "Haiphong", "Da Nang", "Bien Hoa", "Hue", "Nha Trang", "Can Tho", "Rach Gia", "Qui Nhon"],
    
    # 🇲🇾 Malaysia
    "Malaysia": ["Kuala Lumpur", "George Town", "Ipoh", "Shah Alam", "Petaling Jaya", "Johor Bahru", "Seremban", "Kuantan", "Kota Kinabalu", "Kuching"],
    
    # 🇸🇬 Singapore
    "Singapore": ["Singapore"],
    
    # 🇳🇱 Netherlands
    "Netherlands": ["Amsterdam", "Rotterdam", "The Hague", "Utrecht", "Eindhoven", "Tilburg", "Groningen", "Almere", "Breda", "Nijmegen"],
    
    # 🇧🇪 Belgium
    "Belgium": ["Brussels", "Antwerp", "Ghent", "Charleroi", "Liège", "Bruges", "Namur", "Leuven", "Mons", "Aalst"],
    
    # 🇸🇪 Sweden
    "Sweden": ["Stockholm", "Gothenburg", "Malmö", "Uppsala", "Västerås", "Örebro", "Linköping", "Helsingborg", "Jönköping", "Norrköping"],
    
    # 🇳🇴 Norway
    "Norway": ["Oslo", "Bergen", "Trondheim", "Stavanger", "Bærum", "Kristiansand", "Fredrikstad", "Tromsø", "Sandnes", "Asker"],
    
    # 🇩🇰 Denmark
    "Denmark": ["Copenhagen", "Aarhus", "Odense", "Aalborg", "Esbjerg", "Randers", "Kolding", "Horsens", "Vejle", "Roskilde"],
    
    # 🇫🇮 Finland
    "Finland": ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu", "Turku", "Jyväskylä", "Lahti", "Kuopio", "Pori"],
    
    # 🇵🇱 Poland
    "Poland": ["Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"],
    
    # 🇨🇿 Czech Republic
    "Czech Republic": ["Prague", "Brno", "Ostrava", "Plzen", "Liberec", "Olomouc", "Ústí nad Labem", "České Budějovice", "Hradec Králové", "Pardubice"],
    
    # 🇦🇹 Austria
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg", "Innsbruck", "Klagenfurt", "Villach", "Wels", "Sankt Pölten", "Dornbirn"],
    
    # 🇨🇭 Switzerland
    "Switzerland": ["Zurich", "Geneva", "Basel", "Lausanne", "Bern", "Winterthur", "Lucerne", "St. Gallen", "Lugano", "Biel/Bienne"],
    
    # 🇵🇹 Portugal
    "Portugal": ["Lisbon", "Porto", "Vila Nova de Gaia", "Amadora", "Braga", "Setúbal", "Coimbra", "Queluz", "Funchal", "Almada"]
}

# Create flat list for backward compatibility
WORLD_CITIES = []
for country, cities in COUNTRIES_AND_CITIES.items():
    WORLD_CITIES.extend(cities)


# Regional groupings for better organization
REGIONS = {
    "North America": ["United States", "Canada", "Mexico"],
    "Europe": ["United Kingdom", "Germany", "France", "Spain", "Italy", "Netherlands", "Belgium", 
               "Sweden", "Norway", "Denmark", "Finland", "Poland", "Czech Republic", "Austria", "Switzerland", "Portugal"],
    "Asia": ["Japan", "South Korea", "China", "India", "Thailand", "Indonesia", "Philippines", "Vietnam", "Malaysia", "Singapore"],
    "Oceania": ["Australia", "New Zealand"],
    "South America": ["Brazil", "Argentina"],
    "Africa": ["Egypt", "South Africa", "Nigeria", "Kenya"],
    "Eastern Europe & Russia": ["Russia"]
}

# Get all countries sorted alphabetically
def get_all_countries():
    """Return all countries sorted alphabetically"""
    return sorted(COUNTRIES_AND_CITIES.keys())

# Get cities for a specific country
def get_cities_by_country(country):
    """Return cities for a specific country"""
    return COUNTRIES_AND_CITIES.get(country, [])

# Get countries by region
def get_countries_by_region(region):
    """Return countries in a specific region"""
    return REGIONS.get(region, [])

# Search cities within a country
def search_cities_in_country(country, query, limit=10):
    """Search for cities within a specific country"""
    if country not in COUNTRIES_AND_CITIES:
        return []
    
    cities = COUNTRIES_AND_CITIES[country]
    query_lower = query.lower()
    
    # Exact matches first
    exact_matches = [city for city in cities if city.lower() == query_lower]
    
    # Starts with matches
    starts_with = [city for city in cities if city.lower().startswith(query_lower) and city not in exact_matches]
    
    # Contains matches
    contains = [city for city in cities if query_lower in city.lower() and city not in exact_matches and city not in starts_with]
    
    # Combine and limit results
    results = exact_matches + starts_with + contains
    return results[:limit]

# Search for countries
def search_countries(query, limit=10):
    """Search for countries based on query"""
    query_lower = query.lower()
    countries = get_all_countries()
    
    # Exact matches first
    exact_matches = [country for country in countries if country.lower() == query_lower]
    
    # Starts with matches
    starts_with = [country for country in countries if country.lower().startswith(query_lower) and country not in exact_matches]
    
    # Contains matches
    contains = [country for country in countries if query_lower in country.lower() and country not in exact_matches and country not in starts_with]
    
    # Combine and limit results
    results = exact_matches + starts_with + contains
    return results[:limit]

# Get country for a city (for backward compatibility)
def get_country_for_city(city):
    """Return the country for a given city"""
    for country, cities in COUNTRIES_AND_CITIES.items():
        if city in cities:
            return country
    return None

# Get region for a country
def get_region_for_country(country):
    """Return the region for a given country"""
    for region, countries in REGIONS.items():
        if country in countries:
            return region
    return "Other"
