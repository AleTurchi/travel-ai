ANYWHERE_TEST = [
]

AIRPORT_GROUPS = {
    # Italia
    "ROMA": ["FCO", "CIA"],
    "ROME": ["FCO", "CIA"],

    "MILANO": ["MXP", "LIN", "BGY"],
    "MILAN": ["MXP", "LIN", "BGY"],

    "VENEZIA": ["VCE", "TSF"],
    "VENICE": ["VCE", "TSF"],

    "NAPOLI": ["NAP"],
    "NAPLES": ["NAP"],

    "BARI": ["BRI"],
    "CATANIA": ["CTA"],
    "PALERMO": ["PMO"],
    "BOLOGNA": ["BLQ"],
    "PISA": ["PSA"],

    # Francia
    "PARIGI": ["CDG", "ORY", "BVA"],
    "PARIS": ["CDG", "ORY", "BVA"],

    "NIZZA": ["NCE"],
    "NICE": ["NCE"],

    "MARSIGLIA": ["MRS"],
    "MARSEILLE": ["MRS"],

    "LIONE": ["LYS"],
    "LYON": ["LYS"],

    "BORDEAUX": ["BOD"],

    "TOLOSA": ["TLS"],
    "TOULOUSE": ["TLS"],

    # Regno Unito / Irlanda
    "LONDRA": ["LHR", "LGW", "STN", "LTN", "LCY"],
    "LONDON": ["LHR", "LGW", "STN", "LTN", "LCY"],

    "MANCHESTER": ["MAN"],

    "EDIMBURGO": ["EDI"],
    "EDINBURGH": ["EDI"],

    "GLASGOW": ["GLA", "PIK"],

    "BELFAST": ["BFS", "BHD"],

    "DUBLINO": ["DUB"],
    "DUBLIN": ["DUB"],

    # Germania
    "BERLINO": ["BER"],
    "BERLIN": ["BER"],

    "FRANCOFORTE": ["FRA", "HHN"],
    "FRANKFURT": ["FRA", "HHN"],

    "MONACO": ["MUC", "FMM"],
    "MUNICH": ["MUC", "FMM"],

    "DUSSELDORF": ["DUS", "NRN"],
    "DÜSSELDORF": ["DUS", "NRN"],

    "AMBURGO": ["HAM"],
    "HAMBURG": ["HAM"],

    "COLONIA": ["CGN"],
    "COLOGNE": ["CGN"],

    "NORIMBERGA": ["NUE"],
    "NUREMBERG": ["NUE"],

    # Polonia
    "VARSAVIA": ["WAW", "WMI", "RDO"],
    "WARSAW": ["WAW", "WMI", "RDO"],

    "CRACOVIA": ["KRK", "KTW"],
    "KRAKOW": ["KRK", "KTW"],

    "DANZICA": ["GDN"],
    "GDANSK": ["GDN"],

    "WROCLAW": ["WRO"],
    "BRESLAVIA": ["WRO"],

    "POZNAN": ["POZ"],
    "KATOWICE": ["KTW"],

    # Spagna
    "MADRID": ["MAD"],

    "BARCELLONA": ["BCN", "GRO", "REU"],
    "BARCELONA": ["BCN", "GRO", "REU"],

    "MALAGA": ["AGP"],
    "VALENCIA": ["VLC"],
    "ALICANTE": ["ALC"],
    "IBIZA": ["IBZ"],

    "PALMA": ["PMI"],
    "MALLORCA": ["PMI"],
    "PALMA DE MALLORCA": ["PMI"],

    # Grecia
    "ATENE": ["ATH"],
    "ATHENS": ["ATH"],

    "SALONICCO": ["SKG"],
    "THESSALONIKI": ["SKG"],

    "RODI": ["RHO"],
    "RHODES": ["RHO"],

    "CORFU": ["CFU"],
    "CORFÙ": ["CFU"],

    "SANTORINI": ["JTR"],
    "SKIATHOS": ["JSI"],

    # Portogallo
    "LISBONA": ["LIS"],
    "LISBON": ["LIS"],

    "PORTO": ["OPO"],
    "FARO": ["FAO"],

    # Paesi Bassi / Belgio
    "AMSTERDAM": ["AMS", "EIN", "RTM"],
    "ROTTERDAM": ["RTM", "AMS", "EIN"],
    "EINDHOVEN": ["EIN", "AMS", "RTM"],

    "BRUXELLES": ["BRU", "CRL"],
    "BRUSSELS": ["BRU", "CRL"],

    "CHARLEROI": ["CRL"],

    # Nord Europa
    "STOCCOLMA": ["ARN", "BMA", "NYO", "VST"],
    "STOCKHOLM": ["ARN", "BMA", "NYO", "VST"],

    "OSLO": ["OSL", "TRF"],

    "COPENAGHEN": ["CPH", "MMX"],
    "COPENHAGEN": ["CPH", "MMX"],

    # Altri
    "VIENNA": ["VIE", "BTS"],

    "ISTANBUL": ["IST", "SAW"],

    "BASILEA": ["BSL", "MLH", "EAP"],
    "BASEL": ["BSL", "MLH", "EAP"],

    "MALTA": ["MLA"],
    "LA VALLETTA": ["MLA"],
    "VALLETTA": ["MLA"],

    "DUBROVNIK": ["DBV"],

    "ZAGABRIA": ["ZAG"],
    "ZAGREB": ["ZAG"],

    # Balcani / Europa Est
    "SARAJEVO": ["SJJ"],
    "BANJA LUKA": ["BNX"],
    "TUZLA": ["TZL"],
    "MOSTAR": ["OMO"],

    "BELGRADO": ["BEG"],
    "BELGRADE": ["BEG"],
    "NIS": ["INI"],
    "NIŠ": ["INI"],

    "PODGORICA": ["TGD"],
    "TIVAT": ["TIV"],

    "BRATISLAVA": ["BTS", "VIE"],
    "KOSICE": ["KSC"],
    "KOŠICE": ["KSC"],

    "PRAGA": ["PRG"],
    "PRAGUE": ["PRG"],
    "BRNO": ["BRQ"],
    "OSTRAVA": ["OSR"],

    "BUCAREST": ["OTP", "BBU"],
    "BUCHAREST": ["OTP", "BBU"],
    "CLUJ": ["CLJ"],
    "TIMISOARA": ["TSR"],
    "TIMIȘOARA": ["TSR"],
    "IASI": ["IAS"],
    "IAȘI": ["IAS"],
    "CONSTANTA": ["CND"],
    "CONSTANȚA": ["CND"],

    "SOFIA": ["SOF"],
    "VARNA": ["VAR"],
    "BURGAS": ["BOJ"],
    "PLOVDIV": ["PDV"],

    # Nord Europa extra
    "HELSINKI": ["HEL"],
    "TAMPERE": ["TMP"],
    "TURKU": ["TKU"],
    "OULU": ["OUL"],

    "GOTEBORG": ["GOT"],
    "GÖTEBORG": ["GOT"],
    "GOTHENBURG": ["GOT"],
    "MALMO": ["MMX"],
    "MALMÖ": ["MMX"],
    "UMEÅ": ["UME"],
    "UMEA": ["UME"],
    "KIRUNA": ["KRN"],

    "BERGEN": ["BGO"],
    "TRONDHEIM": ["TRD"],
    "STAVANGER": ["SVG"],
    "TROMSO": ["TOS"],
    "TROMSØ": ["TOS"],

    "REYKJAVIK": ["KEF", "RKV"],
    "REYKJAVÍK": ["KEF", "RKV"],
    "AKUREYRI": ["AEY"],
    
    # Albania
    "TIRANA": ["TIA"],

    # Cipro
    "LARNACA": ["LCA"],
    "PAPHOS": ["PFO"],

    "NICOSIA": ["LCA", "ECN"],

    # Estonia
    "TALLINN": ["TLL"],
    "TALLIN": ["TLL"],
    "TARTU": ["TAY"],

    # Lettonia
    "RIGA": ["RIX"],

    # Lituania
    "VILNIUS": ["VNO"],
    "KAUNAS": ["KUN"],
    "PALANGA": ["PLQ"],

    "BUDAPEST": ["BUD"],
    "DEBRECEN": ["DEB"],

    "LJUBLJANA": ["LJU"],
    "MARIBOR": ["MBX"],

    "ZURIGO": ["ZRH"],
    "ZURICH": ["ZRH"],

    "GINEVRA": ["GVA"],
    "GENEVA": ["GVA"],

    "BERNA": ["BRN"],
    "BERN": ["BRN"],
}

COUNTRY_GROUPS = {
    "ITALIA": [
        "ROMA",
        "MILANO",
        "VENEZIA",
        "NAPOLI",
        "BARI",
        "CATANIA",
        "PALERMO",
        "BOLOGNA",
        "PISA",
    ],
    "ITALY": [
        "ROMA",
        "MILANO",
        "VENEZIA",
        "NAPOLI",
        "BARI",
        "CATANIA",
        "PALERMO",
        "BOLOGNA",
        "PISA",
    ],

    "FRANCIA": [
        "PARIGI",
        "NIZZA",
        "MARSIGLIA",
        "LIONE",
        "BORDEAUX",
        "TOLOSA",
    ],
    "FRANCE": [
        "PARIGI",
        "NIZZA",
        "MARSIGLIA",
        "LIONE",
        "BORDEAUX",
        "TOLOSA",
    ],

    "GERMANIA": [
        "BERLINO",
        "FRANCOFORTE",
        "MONACO",
        "DUSSELDORF",
        "AMBURGO",
        "COLONIA",
        "NORIMBERGA",
    ],
    "GERMANY": [
        "BERLINO",
        "FRANCOFORTE",
        "MONACO",
        "DUSSELDORF",
        "AMBURGO",
        "COLONIA",
        "NORIMBERGA",
    ],

    "POLONIA": [
        "VARSAVIA",
        "CRACOVIA",
        "DANZICA",
        "WROCLAW",
        "POZNAN",
        "KATOWICE",
    ],
    "POLAND": [
        "VARSAVIA",
        "CRACOVIA",
        "DANZICA",
        "WROCLAW",
        "POZNAN",
        "KATOWICE",
    ],

    "SPAGNA": [
        "MADRID",
        "BARCELLONA",
        "MALAGA",
        "VALENCIA",
        "ALICANTE",
        "PALMA DE MALLORCA",
        "IBIZA",
    ],
    "SPAIN": [
        "MADRID",
        "BARCELLONA",
        "MALAGA",
        "VALENCIA",
        "ALICANTE",
        "PALMA DE MALLORCA",
        "IBIZA",
    ],

    "GRECIA": [
        "ATENE",
        "SALONICCO",
        "RODI",
        "CORFU",
        "SANTORINI",
        "SKIATHOS",
    ],
    "GREECE": [
        "ATENE",
        "SALONICCO",
        "RODI",
        "CORFU",
        "SANTORINI",
        "SKIATHOS",
    ],

    "PORTOGALLO": [
        "LISBONA",
        "PORTO",
        "FARO",
    ],
    "PORTUGAL": [
        "LISBONA",
        "PORTO",
        "FARO",
    ],

    "PAESI BASSI": [
        "AMSTERDAM",
        "ROTTERDAM",
        "EINDHOVEN",
    ],
    "NETHERLANDS": [
        "AMSTERDAM",
        "ROTTERDAM",
        "EINDHOVEN",
    ],

    "BELGIO": [
        "BRUXELLES",
        "CHARLEROI",
    ],
    "BELGIUM": [
        "BRUXELLES",
        "CHARLEROI",
    ],

    "REGNO UNITO": [
        "LONDRA",
        "MANCHESTER",
        "EDIMBURGO",
        "GLASGOW",
        "BELFAST",
    ],
    "UNITED KINGDOM": [
        "LONDRA",
        "MANCHESTER",
        "EDIMBURGO",
        "GLASGOW",
        "BELFAST",
    ],

    "AUSTRIA": [
        "VIENNA",
    ],

    "TURCHIA": [
        "ISTANBUL",
    ],
    "TURKEY": [
        "ISTANBUL",
    ],

    "CROAZIA": [
        "ZAGABRIA",
        "DUBROVNIK",
    ],
    "CROATIA": [
        "ZAGABRIA",
        "DUBROVNIK",
    ],
    "ALBANIA": [
        "TIRANA",
    ],

    "CIPRO": [
        "LARNACA",
        "PAPHOS",
    ],
    "CYPRUS": [
        "LARNACA",
        "PAPHOS",
    ],

    "ESTONIA": [
        "TALLINN",
        "TARTU",
    ],

    "LETTONIA": [
        "RIGA",
    ],
    "LATVIA": [
        "RIGA",
    ],

    "LITUANIA": [
        "VILNIUS",
        "KAUNAS",
        "PALANGA",
    ],
    "LITHUANIA": [
        "VILNIUS",
        "KAUNAS",
        "PALANGA",
    ],

    "DANIMARCA": [
        "COPENAGHEN",
    ],
    "DENMARK": [
        "COPENAGHEN",
    ],
    
    "SVIZZERA": [
        "ZURIGO",
        "GINEVRA",
        "BASILEA",
    ],
    "SWITZERLAND": [
        "ZURIGO",
        "GINEVRA",
        "BASILEA",
    ],

    "SLOVENIA": [
        "LJUBLJANA",
        "MARIBOR",
    ],

    "UNGHERIA": [
    "BUDAPEST",
    "DEBRECEN",
    ],

    "HUNGARY": [
        "BUDAPEST",
        "DEBRECEN",
    ],

    "BOSNIA": ["SARAJEVO", "BANJA LUKA", "TUZLA", "MOSTAR"],
    "BOSNIA ED ERZEGOVINA": ["SARAJEVO", "BANJA LUKA", "TUZLA", "MOSTAR"],

    "SERBIA": ["BELGRADO", "NIS"],

    "MONTENEGRO": ["PODGORICA", "TIVAT"],

    "SLOVACCHIA": ["BRATISLAVA", "KOSICE"],
    "SLOVAKIA": ["BRATISLAVA", "KOSICE"],

    "REPUBBLICA CECA": ["PRAGA", "BRNO", "OSTRAVA"],
    "CZECHIA": ["PRAGA", "BRNO", "OSTRAVA"],
    "CZECH REPUBLIC": ["PRAGA", "BRNO", "OSTRAVA"],

    "ROMANIA": ["BUCAREST", "CLUJ", "TIMISOARA", "IASI", "CONSTANTA"],

    "BULGARIA": ["SOFIA", "VARNA", "BURGAS", "PLOVDIV"],

    "FINLANDIA": ["HELSINKI", "TAMPERE", "TURKU", "OULU"],
    "FINLAND": ["HELSINKI", "TAMPERE", "TURKU", "OULU"],

    "SVEZIA": ["STOCCOLMA", "GOTEBORG", "MALMO", "UMEÅ", "KIRUNA"],
    "SWEDEN": ["STOCCOLMA", "GOTEBORG", "MALMO", "UMEÅ", "KIRUNA"],

    "NORVEGIA": ["OSLO", "BERGEN", "TRONDHEIM", "STAVANGER", "TROMSO"],
    "NORWAY": ["OSLO", "BERGEN", "TRONDHEIM", "STAVANGER", "TROMSO"],

    "ISLANDA": ["REYKJAVIK", "AKUREYRI"],
    "ICELAND": ["REYKJAVIK", "AKUREYRI"],
}