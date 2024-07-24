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
    match = re.search(r'^(.*?)-', doc_name)   #match = re.search(r'-([А-Яа-я]+)-', doc_name)
    if match:
        return match.group(1)      # CEZ Wind Farm     # "Бръшляница"
    return "No match found for station name."


def subnetwork_name(doc_name):
    match = re.search(r'((?:BL|VD|VR|KN|LO|MO|PK|PL|SF|SO)\d{4})', doc_name)   #match = re.search(r'([A-Za-z]{2}\d+)', doc_name)
    if match:
        return match.group(1)   # "PL1102"
    return "No match found for subnetwork name."


document_name = "CEZ Wind Farm-Бръшляница-PL1102-20 kV_new"
voltage = extract_voltage(document_name)
voltage_group = voltage_group(document_name)
station_name = station_name(document_name)
subnetwork_name = subnetwork_name(document_name)
print(f"Extracted voltage value: {voltage}")
print(f"The voltage group is: {voltage_group}")
print(f"The station name is: {station_name}")
print(f"The code is: {subnetwork_name}")


#################################################################################


# voltage_mapping = {"Unknown": 0,
#                    "0,230 kV": 230,
#                    "0,4 kV": 400,
#                    "0,66 kV": 660,
#                    "0,8 kV": 800,
#                    "0,95 kV": 950,
#                    "1 kV": 1000,
#                    "6 kV": 6000,
#                    "10 kV": 10000,
#                    "20 kV": 20000,
#                    "35 kV": 35000,
#                    "60 kV": 60000,
#                    "110 kV": 110000,
#                    "220 kV": 220000,
#                    "400 kV": 400000}
#
#
# def extract_voltage(doc_name):
#     match = re.search(r'(\d+ kV)', doc_name)
#     if match:
#         voltage_text = match.group(1)  # "20 kV"
#         if voltage_text in voltage_mapping:
#             return voltage_mapping.get(voltage_text)  # Return mapped voltage value or None if not found
#         return None
#
#
# def voltage_group(voltage_value):
#     if voltage_value < 1000:
#         return "LV"
#     elif 1000 <= voltage_value <= 35000:
#         return "MV"
#     elif voltage_value > 35000:
#         return "HV"
#     else:
#         return "Unknown"
#
#
# def determine_voltage_group(document):
#     voltage_value = extract_voltage(document)    # value: 20000
#     if voltage_value is not None:
#         return voltage_group(voltage_value)     # voltage_group: "MV"
#     else:
#         return "Unknown"
#
#
# doc_name = r"C:\Users\nikole\Documents\new task\autocad files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf"
# group = determine_voltage_group(doc_name)
# #print(f"The voltage group is: {group}")