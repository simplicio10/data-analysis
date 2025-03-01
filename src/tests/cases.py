
def address_tests():
    test_case = [
        'ON N RIDGEWAY AVE FROM W SCHOOL ST (3300 N) TO W BELMONT AVE (3200 N)',
        'N MILWAUKEE AVE & N WASHTENAW AVE',
        '1110 N STATE ST; 1030 N STATE ST',
        '5300-5330 S PRAIRIE AVE',
        'ON W 70TH ST FROM S GREEN ST (830 W) TO S PEORIA ST (900 W)',
        '434-442 E 46TH PL',  # unable to find address in address API
        'S DORCHESTER AVE & E MADISON PARK  & S WOODLAWN AVE & E 50TH ST',
        'ON N LEAVITT ST FROM W DIVISION ST (1200 N) TO W NORTH AVE (1600 N)',
        'N WOOD AVE & W AUGUSTA ST & W CORTEZ ST & N HERMITAGE AVE',
        'ON W 52ND PL FROM 322 W TO S PRINCETON AVE (300 W)',  #
        '3221 W ARMITAGE AVE',
        'N CAMPBELL AVE & W LE MOYNE ST & W HIRSCH ST & N MAPLEWOOD AVE',
        'ON N KOLMAR AVE FROM W CORNELIA AVE (3500 N) TO W ADDISON ST (3600 N)',
        '200-250 E 40TH ST',  # unable to find addresss
        'N WHIPPLE ST & W BLOOMINGDALE AVE & N HUMBOLDT BLVD W & W CORTLAND ST',
        '1400 N CAMPBELL AVE; N CAMPBELL AVE & W LE MOYNE ST & W HIRSCH ST & N MAPLEWOOD AVE',
        '6754 S EUCLID AVE; ON W 68TH ST FROM S BENNETT AVE  (1900 E) TO S EUCLID AVE  (1930 E)',
        '1110 N STATE ST; 1030 N STATE ST',
        # 'ON W EVERGREEN AVE FROM N MILWAUKEE AVE  (1800 W) TO W SCHILLER ST  (1900 W)' # on transportation reported as cross with "Wicher Park AVE",
        # null cases
        'N MILWAUKEE AVE & N HONORE ST',
        'W DIVISION ST & N PAULINA ST',
        'ON N HONORE ST FROM N WICKER PARK AVE (1500 N) TO N MILWAUKEE AVE (1520 N)',
        'ON W DELAWARE PL FROM N DEARBORN ST (40 W) TO N CLARK ST (100 W)',
        'S DR MARTIN LUTHER KING JR DR & E 42ND ST',
        "ON W BARRY AVE FROM N BROADWAY ST (599 W) TO N CLARK ST (800 W)",
        "ON W BRIAR PL FROM N BROADWAY ST (599 W) TO N HALSTED ST (800 W)",
        "ON W OAKDALE AVE FROM N CLARK ST (700 W) TO N PINE GROVE AVE (500 W)",
        "ON W SURF ST FROM N PINE GROVE AVE (510 W) TO N CLARK ST (700 W)",
        "ON W SURF ST FROM N PINE GROVE AVE (510 W) TO N SHERIDAN RD (400 W)",
        "ON W WELLINGTON AVE FROM N BROADWAY ST (599 W) TO N CLARK ST (730 W)",
        "ON W WELLINGTON ST FROM N BROADWAY ST (599 W) TO N CLARK ST (730 W)",
        "ON W 125TH PL FROM 50  W TO S STATE ST  (0 E)",
        "ON S MANISTEE AVE FROM 10300 S TO E 104TH ST  (10400 S)",
        'W 43RD ST &  S HALSTED ST; S LOCK ST &  S LYMAN ST',
        # intentional wrong locations
        '1400 N WRONG AVE',
        'jkdfhgjkoahfiea',
        'N NOPE AVE & W HGFYHREAS ST & W OFFLIMIT ST & N GHTUEIFGHUS AVE',
    ]

    return test_case