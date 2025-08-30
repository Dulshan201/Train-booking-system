# Major cities around the world for train booking system
WORLD_CITIES = [
    # North America
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
    "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus",
    "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston",
    "El Paso", "Nashville", "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis",
    "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento",
    "Kansas City", "Mesa", "Atlanta", "Colorado Springs", "Omaha", "Raleigh", "Miami", "Oakland",
    "Minneapolis", "Tulsa", "Cleveland", "Wichita", "Arlington", "Tampa", "New Orleans",
    "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi",
    "Lexington", "Pittsburgh", "Anchorage", "Stockton", "Cincinnati", "Saint Paul", "Toledo",
    "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Jersey City",
    "Chula Vista", "Fort Wayne", "Orlando", "St. Petersburg", "Chandler", "Laredo", "Norfolk",
    "Durham", "Madison", "Lubbock", "Irvine", "Winston-Salem", "Glendale", "Garland",
    "Hialeah", "Reno", "Chesapeake", "Gilbert", "Baton Rouge", "Irving", "Scottsdale",
    "North Las Vegas", "Fremont", "Boise", "Richmond", "San Bernardino", "Birmingham",
    
    # Canada
    "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg",
    "Quebec City", "Hamilton", "Kitchener", "London", "Victoria", "Halifax", "Oshawa",
    "Windsor", "Saskatoon", "Regina", "Sherbrooke", "St. John's", "Barrie", "Kelowna",
    "Abbotsford", "Greater Sudbury", "Kingston", "Saguenay", "Trois-Rivières", "Guelph",
    "Cambridge", "Whitby", "Coquitlam", "Saanich", "Milton", "Thunder Bay", "Burlington",
    "Moncton", "Saint John", "Richmond Hill", "Oakville", "Vaughan", "Burnaby", "Richmond",
    
    # Europe
    "London", "Berlin", "Madrid", "Rome", "Paris", "Bucharest", "Vienna", "Hamburg",
    "Warsaw", "Budapest", "Barcelona", "Munich", "Milan", "Prague", "Sofia", "Brussels",
    "Birmingham", "Cologne", "Naples", "Turin", "Palermo", "Marseille", "Stockholm",
    "Amsterdam", "Valencia", "Kraków", "Seville", "Łódź", "Zaragoza", "Athens", "Frankfurt",
    "Wrocław", "Helsinki", "Rotterdam", "Düsseldorf", "Essen", "Gothenburg", "Málaga",
    "Stuttgart", "The Hague", "Dortmund", "Genoa", "Leipzig", "Vilnius", "Bologna",
    "Oslo", "Poznań", "Gdańsk", "Lisbon", "Bremen", "Dresden", "Copenhagen", "Hannover",
    "Duisburg", "Bochum", "Nuremberg", "Wuppertal", "Bielefeld", "Bonn", "Münster",
    "Mannheim", "Augsburg", "Chemnitz", "Braunschweig", "Aachen", "Kiel", "Magdeburg",
    "Freiburg", "Lübeck", "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen",
    "Saarbrücken", "Hamm", "Mülheim", "Potsdam", "Ludwigshafen", "Oldenburg", "Leverkusen",
    "Osnabrück", "Solingen", "Heidelberg", "Herne", "Neuss", "Darmstadt", "Paderborn",
    "Regensburg", "Ingolstadt", "Würzburg", "Fürth", "Wolfsburg", "Offenbach", "Ulm",
    
    # Asia
    "Tokyo", "Delhi", "Shanghai", "Dhaka", "São Paulo", "Cairo", "Mexico City", "Beijing",
    "Mumbai", "Osaka", "Karachi", "Chongqing", "Istanbul", "Buenos Aires", "Kolkata",
    "Manila", "Lagos", "Rio de Janeiro", "Tianjin", "Kinshasa", "Guangzhou", "Los Angeles",
    "Moscow", "Shenzhen", "Lahore", "Bangalore", "Paris", "Bogotá", "Jakarta", "Chennai",
    "Lima", "Bangkok", "Seoul", "Nagoya", "Hyderabad", "London", "Tehran", "Chicago",
    "Chengdu", "Nanjing", "Wuhan", "Ho Chi Minh City", "Luanda", "Ahmedabad", "Kuala Lumpur",
    "Pune", "Surat", "Jeddah", "Harbin", "Surabaya", "Riyadh", "Baghdad", "Singapore",
    "Khartoum", "Aleppo", "Qingdao", "Dalian", "Zhengzhou", "Ji'nan", "Salvador",
    "Fortaleza", "Dar es Salaam", "Barcelona", "St. Petersburg", "Medellín", "Brasília",
    "Faisalabad", "Belo Horizonte", "Rawalpindi", "Sapporo", "Kyoto", "Fukuoka", "Kawasaki",
    "Yokohama", "Kobe", "Kitakyushu", "Hiroshima", "Sendai", "Chiba", "Sakai", "Niigata",
    "Hamamatsu", "Okayama", "Sagamihara", "Shizuoka", "Kumamoto", "Kagoshima", "Utsunomiya",
    
    # Australia & Oceania
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle",
    "Canberra", "Sunshine Coast", "Wollongong", "Hobart", "Geelong", "Townsville",
    "Cairns", "Darwin", "Toowoomba", "Ballarat", "Bendigo", "Albury", "Launceston",
    "Mackay", "Rockhampton", "Bunbury", "Bundaberg", "Coffs Harbour", "Wagga Wagga",
    "Hervey Bay", "Mildura", "Shepparton", "Port Macquarie", "Gladstone", "Tamworth",
    "Traralgon", "Orange", "Dubbo", "Geraldton", "Nowra", "Warrnambool", "Kalgoorlie",
    "Albany", "Blue Mountains", "Lismore", "Goulburn", "Broken Hill", "Bathurst",
    "Auckland", "Wellington", "Christchurch", "Hamilton", "Tauranga", "Napier-Hastings",
    "Dunedin", "Palmerston North", "Nelson", "Rotorua", "New Plymouth", "Whangarei",
    "Invercargill", "Whanganui", "Gisborne", "Timaru", "Pukekohe", "Papakura",
    
    # Africa
    "Lagos", "Cairo", "Kinshasa", "Luanda", "Nairobi", "Casablanca", "Alexandria",
    "Abidjan", "Kano", "Cape Town", "Ibadan", "Dar es Salaam", "Addis Ababa", "Johannesburg",
    "Khartoum", "Algiers", "Accra", "Sanaa", "Mogadishu", "Lusaka", "Harare", "Antananarivo",
    "Kampala", "Rabat", "Dakar", "Bamako", "Conakry", "Freetown", "Monrovia", "Lomé",
    "Ouagadougou", "Niamey", "N'Djamena", "Libreville", "Malabo", "Bangui", "Brazzaville",
    "Kinshasa", "Bujumbura", "Kigali", "Dodoma", "Moroni", "Port Louis", "Victoria",
    "Windhoek", "Gaborone", "Maseru", "Mbabane", "Maputo", "Pretoria", "Bloemfontein",
    
    # South America
    "São Paulo", "Rio de Janeiro", "Buenos Aires", "Lima", "Bogotá", "Santiago",
    "Caracas", "Salvador", "Brasília", "Fortaleza", "Belo Horizonte", "Medellín",
    "Guayaquil", "Quito", "La Paz", "Santa Cruz", "Montevideo", "Asunción", "Georgetown",
    "Paramaribo", "Cayenne", "Recife", "Porto Alegre", "Manaus", "Curitiba", "Belém",
    "Goiânia", "Guarulhos", "Campinas", "São Luís", "São Gonçalo", "Maceió", "Duque de Caxias",
    "Natal", "Teresina", "Campo Grande", "Nova Iguaçu", "São Bernardo do Campo", "João Pessoa",
    "Santo André", "Osasco", "Jaboatão dos Guararapes", "São José dos Campos", "Ribeirão Preto",
    "Uberlândia", "Sorocaba", "Contagem", "Aracaju", "Feira de Santana", "Cuiabá",
    "Joinville", "Juiz de Fora", "Londrina", "Aparecida de Goiânia", "Niterói", "Ananindeua",
    "Cali", "Barranquilla", "Cartagena", "Cúcuta", "Soledad", "Ibagué", "Bucaramanga",
    "Soacha", "Santa Marta", "Villavicencio", "Valledupar", "Pereira", "Montería",
    "Bello", "Pasto", "Armenia", "Manizales", "Neiva", "Palmira", "Popayán", "Buenaventura",
    "Tuluá", "Envigado", "Cartago", "Girardot", "Ubaté", "Sogamoso", "Facatativá"
]

# Group cities by regions for better organization
CITY_REGIONS = {
    "North America": [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
        "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus",
        "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston",
        "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg",
        "Quebec City", "Hamilton", "Kitchener", "London", "Victoria", "Halifax"
    ],
    "Europe": [
        "London", "Berlin", "Madrid", "Rome", "Paris", "Bucharest", "Vienna", "Hamburg",
        "Warsaw", "Budapest", "Barcelona", "Munich", "Milan", "Prague", "Sofia", "Brussels",
        "Birmingham", "Cologne", "Naples", "Turin", "Amsterdam", "Stockholm", "Helsinki",
        "Oslo", "Copenhagen", "Lisbon", "Athens", "Dublin", "Edinburgh", "Glasgow"
    ],
    "Asia": [
        "Tokyo", "Delhi", "Shanghai", "Beijing", "Mumbai", "Osaka", "Seoul", "Bangkok",
        "Singapore", "Kuala Lumpur", "Manila", "Jakarta", "Bangalore", "Chennai", "Hyderabad",
        "Pune", "Kolkata", "Ahmedabad", "Surat", "Nagoya", "Yokohama", "Kobe", "Kyoto",
        "Fukuoka", "Kawasaki", "Sapporo", "Hiroshima", "Sendai", "Chiba"
    ],
    "Australia & Oceania": [
        "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle",
        "Canberra", "Auckland", "Wellington", "Christchurch", "Hamilton", "Tauranga"
    ],
    "Africa": [
        "Cairo", "Lagos", "Nairobi", "Cape Town", "Johannesburg", "Casablanca", "Alexandria",
        "Addis Ababa", "Accra", "Algiers", "Tunis", "Rabat", "Dar es Salaam", "Lusaka"
    ],
    "South America": [
        "São Paulo", "Rio de Janeiro", "Buenos Aires", "Lima", "Bogotá", "Santiago",
        "Caracas", "Salvador", "Brasília", "Fortaleza", "Belo Horizonte", "Medellín",
        "Guayaquil", "Quito", "La Paz", "Montevideo", "Asunción"
    ]
}
