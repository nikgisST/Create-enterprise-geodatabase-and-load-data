import re

voltage_mapping = {"Unknown": 0,
                   "0,230 kV": 230,
                   "0,4 kV": 400,
                   "0,66 kV": 660,
                   "0,8 kV": 800,
                   "0,95 kV": 950,
                   "1 kV": 1000,
                   "6 kV": 6000,
                   "10 kV": 10000,
                   "20 kV": 20000,
                   "35 kV": 35000,
                   "60 kV": 60000,
                   "110 kV": 110000,
                   "220 kV": 220000,
                   "400 kV": 400000}


def extract_voltage(doc_name):
    match = re.search(r'(\d+ kV)', doc_name)
    if match:
        voltage_text = match.group(1)  # "20 kV"
        if voltage_text in voltage_mapping:
            return voltage_mapping[voltage_text]  # value: 20000
        else:
            return None
    return "No match found for voltage value."


def voltage_group(doc_name):
    voltage_value = extract_voltage(doc_name)    # value: 20000
    if voltage_value is not None:
        if voltage_value < 1000:
            return "LV"
        elif 1000 <= voltage_value <= 35000:
            return "MV"                         # voltage_group: "MV"
        elif voltage_value > 35000:
            return "HV"
    return "Unknown"


def station_name(doc_name):
    match = re.search(r'^(.*?)-', doc_name)
    if match:
        return match.group(1)   # "CEZ Wind Farm"
    return "No match found for station name."


def subnetwork_name(doc_name):
    match = re.search(r'((?:BL|VD|VR|KN|LO|MO|PK|PL|SF|SO)\d{4})', doc_name)
    if match:
        return match.group(1)   # "PL1102"
    return "No match found for subnetwork name."