import arcpy
import re

# Set workspace
arcpy.env.workspace = r"C:\Users\nikole\Documents\new task\autocad files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf"   #r"D:\my new task\autocad files corrected\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf"     #print(matching_word.group(1))                                             #return matching_word.group(1) if matching_word else None

# Set local variables
#out_folder_path = r"C:\Users\nikole\Documents\new task\file_gdb_wind_farm\wind_farm_gdb.gdb"
#out_name = "wind_farm_gdb.gdb"
# Create Data Loading Workspace
#arcpy.management.CreateDataLoadingWorkspace(source_target_mapping, out_folder, {match_options}, {mapping_table}, {calc_stats}, {match_subtypes})

def extract_voltage(dxf_filename):
    matching_word = re.search(r'(\d+ kV)', dxf_filename)   #(r'(\d+)\s*kV', doc_name)
    if matching_word:
        return int(matching_word.group(1))
    else:
        return None
# def extract_voltage(doc_name):
#     if '20 kV' in doc_name:
#         return "20 kv"
#     return None


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
    else:
        pass


if __name__ == '__main__':
    extract_voltage(arcpy.env.workspace)
