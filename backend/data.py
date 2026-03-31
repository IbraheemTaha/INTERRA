"""
Sample data for the six data-lake tables used in the INTERRA walkthrough.
Each function returns a list of dicts (rows) ready for JSON serialisation.
"""


def bus_ridership_2022() -> list[dict]:
    """T1 – Monthly bus ridership counts per route and borough."""
    return [
        {"month": "2022-01", "route": "B46",  "borough": "Brooklyn",  "ridership": 824500},
        {"month": "2022-01", "route": "M15",  "borough": "Manhattan", "ridership": 1102300},
        {"month": "2022-01", "route": "Bx12", "borough": "Bronx",     "ridership": 673200},
        {"month": "2022-02", "route": "B46",  "borough": "Brooklyn",  "ridership": 791800},
        {"month": "2022-02", "route": "M15",  "borough": "Manhattan", "ridership": 1058700},
        {"month": "2022-02", "route": "Bx12", "borough": "Bronx",     "ridership": 648900},
        {"month": "2022-03", "route": "B46",  "borough": "Brooklyn",  "ridership": 856200},
        {"month": "2022-03", "route": "M15",  "borough": "Manhattan", "ridership": 1134500},
        {"month": "2022-03", "route": "Bx12", "borough": "Bronx",     "ridership": 701100},
        {"month": "2022-04", "route": "B46",  "borough": "Brooklyn",  "ridership": 879400},
        {"month": "2022-04", "route": "M15",  "borough": "Manhattan", "ridership": 1167800},
        {"month": "2022-04", "route": "Bx12", "borough": "Bronx",     "ridership": 719300},
        {"month": "2022-05", "route": "B46",  "borough": "Brooklyn",  "ridership": 903100},
        {"month": "2022-05", "route": "M15",  "borough": "Manhattan", "ridership": 1198200},
        {"month": "2022-05", "route": "Bx12", "borough": "Bronx",     "ridership": 735600},
    ]


def subway_hourly_flows() -> list[dict]:
    """T2 – Hourly passenger flows at each subway station."""
    return [
        {"station": "Times Sq-42 St",     "hour": "07:00", "day_type": "weekday", "passengers": 18420},
        {"station": "Times Sq-42 St",     "hour": "08:00", "day_type": "weekday", "passengers": 34560},
        {"station": "Times Sq-42 St",     "hour": "09:00", "day_type": "weekday", "passengers": 28730},
        {"station": "Grand Central-42 St","hour": "07:00", "day_type": "weekday", "passengers": 16890},
        {"station": "Grand Central-42 St","hour": "08:00", "day_type": "weekday", "passengers": 31200},
        {"station": "Grand Central-42 St","hour": "09:00", "day_type": "weekday", "passengers": 25400},
        {"station": "Fulton St",          "hour": "07:00", "day_type": "weekday", "passengers": 12340},
        {"station": "Fulton St",          "hour": "08:00", "day_type": "weekday", "passengers": 24680},
        {"station": "Fulton St",          "hour": "09:00", "day_type": "weekday", "passengers": 19870},
        {"station": "Atlantic Av-Barclays","hour": "07:00","day_type": "weekday", "passengers": 9870},
        {"station": "Atlantic Av-Barclays","hour": "08:00","day_type": "weekday", "passengers": 21340},
        {"station": "Atlantic Av-Barclays","hour": "09:00","day_type": "weekday", "passengers": 17560},
    ]


def neighbourhood_income_census() -> list[dict]:
    """T3 – Median household income, poverty rate, and employment status per census tract."""
    return [
        {"tract_id": "36061002300", "neighbourhood": "Upper East Side",  "median_income": 112450, "poverty_rate": 0.07, "employment_rate": 0.74},
        {"tract_id": "36047023400", "neighbourhood": "Park Slope",       "median_income": 98200,  "poverty_rate": 0.09, "employment_rate": 0.71},
        {"tract_id": "36005004900", "neighbourhood": "Fordham",          "median_income": 28750,  "poverty_rate": 0.34, "employment_rate": 0.48},
        {"tract_id": "36081040100", "neighbourhood": "Jamaica",          "median_income": 52300,  "poverty_rate": 0.18, "employment_rate": 0.59},
        {"tract_id": "36047034200", "neighbourhood": "East New York",    "median_income": 34100,  "poverty_rate": 0.29, "employment_rate": 0.51},
        {"tract_id": "36061010800", "neighbourhood": "Harlem",           "median_income": 41600,  "poverty_rate": 0.25, "employment_rate": 0.55},
        {"tract_id": "36047055600", "neighbourhood": "Flatbush",         "median_income": 46800,  "poverty_rate": 0.21, "employment_rate": 0.57},
        {"tract_id": "36085012400", "neighbourhood": "St. George",       "median_income": 58900,  "poverty_rate": 0.15, "employment_rate": 0.62},
        {"tract_id": "36061003400", "neighbourhood": "Midtown",          "median_income": 95600,  "poverty_rate": 0.08, "employment_rate": 0.72},
        {"tract_id": "36047060200", "neighbourhood": "Bay Ridge",        "median_income": 62400,  "poverty_rate": 0.12, "employment_rate": 0.65},
    ]


def transit_accessibility_index() -> list[dict]:
    """T4 – Transit-access score per neighborhood, joinable on tract ID."""
    return [
        {"tract_id": "36061002300", "neighbourhood": "Upper East Side",  "access_score": 0.91, "bus_routes": 8,  "subway_lines": 3},
        {"tract_id": "36047023400", "neighbourhood": "Park Slope",       "access_score": 0.84, "bus_routes": 5,  "subway_lines": 4},
        {"tract_id": "36005004900", "neighbourhood": "Fordham",          "access_score": 0.72, "bus_routes": 7,  "subway_lines": 2},
        {"tract_id": "36081040100", "neighbourhood": "Jamaica",          "access_score": 0.65, "bus_routes": 10, "subway_lines": 2},
        {"tract_id": "36047034200", "neighbourhood": "East New York",    "access_score": 0.53, "bus_routes": 4,  "subway_lines": 1},
        {"tract_id": "36061010800", "neighbourhood": "Harlem",           "access_score": 0.79, "bus_routes": 6,  "subway_lines": 3},
        {"tract_id": "36047055600", "neighbourhood": "Flatbush",         "access_score": 0.68, "bus_routes": 5,  "subway_lines": 2},
        {"tract_id": "36085012400", "neighbourhood": "St. George",       "access_score": 0.47, "bus_routes": 3,  "subway_lines": 0},
        {"tract_id": "36061003400", "neighbourhood": "Midtown",          "access_score": 0.97, "bus_routes": 12, "subway_lines": 6},
        {"tract_id": "36047060200", "neighbourhood": "Bay Ridge",        "access_score": 0.58, "bus_routes": 4,  "subway_lines": 1},
    ]


def land_use_zoning() -> list[dict]:
    """T5 – Zoning category and floor-area ratios per parcel."""
    return [
        {"parcel_id": "BK-001", "borough": "Brooklyn",  "zone": "R6",  "floor_area_ratio": 2.43, "land_use": "Residential"},
        {"parcel_id": "MN-014", "borough": "Manhattan", "zone": "C5-3","floor_area_ratio": 10.0, "land_use": "Commercial"},
        {"parcel_id": "BX-007", "borough": "Bronx",     "zone": "R7A", "floor_area_ratio": 4.0,  "land_use": "Residential"},
        {"parcel_id": "QN-022", "borough": "Queens",    "zone": "M1-1","floor_area_ratio": 1.0,  "land_use": "Manufacturing"},
        {"parcel_id": "SI-003", "borough": "Staten Island","zone":"R3-2","floor_area_ratio":0.5,  "land_use": "Residential"},
        {"parcel_id": "MN-031", "borough": "Manhattan", "zone": "C6-4","floor_area_ratio": 10.0, "land_use": "Commercial"},
        {"parcel_id": "BK-042", "borough": "Brooklyn",  "zone": "M1-2","floor_area_ratio": 2.0,  "land_use": "Manufacturing"},
        {"parcel_id": "QN-055", "borough": "Queens",    "zone": "R5",  "floor_area_ratio": 1.25, "land_use": "Residential"},
    ]


def commute_survey_microdata() -> list[dict]:
    """T6 – Individual-level survey: commute mode, duration, income bracket."""
    return [
        {"respondent_id": 1001, "tract_id": "36061002300", "commute_mode": "subway",  "duration_min": 32, "income_bracket": "$100k+"},
        {"respondent_id": 1002, "tract_id": "36047023400", "commute_mode": "bus",     "duration_min": 45, "income_bracket": "$75k-100k"},
        {"respondent_id": 1003, "tract_id": "36005004900", "commute_mode": "bus",     "duration_min": 58, "income_bracket": "$25k-50k"},
        {"respondent_id": 1004, "tract_id": "36081040100", "commute_mode": "car",     "duration_min": 41, "income_bracket": "$50k-75k"},
        {"respondent_id": 1005, "tract_id": "36047034200", "commute_mode": "bus",     "duration_min": 63, "income_bracket": "$25k-50k"},
        {"respondent_id": 1006, "tract_id": "36061010800", "commute_mode": "subway",  "duration_min": 28, "income_bracket": "$50k-75k"},
        {"respondent_id": 1007, "tract_id": "36047055600", "commute_mode": "subway",  "duration_min": 37, "income_bracket": "$50k-75k"},
        {"respondent_id": 1008, "tract_id": "36085012400", "commute_mode": "ferry",   "duration_min": 52, "income_bracket": "$75k-100k"},
        {"respondent_id": 1009, "tract_id": "36061003400", "commute_mode": "walk",    "duration_min": 12, "income_bracket": "$100k+"},
        {"respondent_id": 1010, "tract_id": "36047060200", "commute_mode": "car",     "duration_min": 35, "income_bracket": "$50k-75k"},
        {"respondent_id": 1011, "tract_id": "36061002300", "commute_mode": "bike",    "duration_min": 18, "income_bracket": "$75k-100k"},
        {"respondent_id": 1012, "tract_id": "36005004900", "commute_mode": "bus",     "duration_min": 67, "income_bracket": "<$25k"},
    ]


# Registry: table_key -> (function, display_name)
TABLE_REGISTRY = {
    "T1": (bus_ridership_2022,        "bus_ridership_2022"),
    "T2": (subway_hourly_flows,       "subway_hourly_flows"),
    "T3": (neighbourhood_income_census,"neighbourhood_income_census"),
    "T4": (transit_accessibility_index,"transit_accessibility_index"),
    "T5": (land_use_zoning,           "land_use_zoning"),
    "T6": (commute_survey_microdata,  "commute_survey_microdata"),
}
