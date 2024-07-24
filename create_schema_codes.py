# Import system modules
import os
import sys
import arcpy

# Set workspace
arcpy.env.workspace = r"D:\my new task\project_ro"

# Set local variables
out_folder_path = r"D:\my new task\project_ro"
out_name = "windfarmfgdb.gdb"

# Execute CreateFileGDB
# old: arcpy.CreateFileGDB_management(out_folder_path, out_name)
arcpy.management.CreateFileGDB(out_folder_path, "windfarmfgdb.gdb", "CURRENT")   # out_version(Optional)

# Create Feature Dataset
arcpy.management.CreateFeatureDataset(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Electric", 'PROJCS["WGS_1984_UTM_Zone_35N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",27.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision')

# Create Feature Classes
arcpy.management.CreateFeatureclass(r"D:\my new task\project_ro\windfarmfgdb.gdb\Electric", "Station", "POINT", None, "DISABLED", "DISABLED", 'PROJCS["WGS_1984_UTM_Zone_35N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",27.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision', '', 0, 0, 0, "Statie Post")
arcpy.management.CreateFeatureclass(r"D:\my new task\project_ro\windfarmfgdb.gdb\Electric", "Conductor", "POLYLINE", None, "DISABLED", "DISABLED", 'PROJCS["WGS_1984_UTM_Zone_35N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",27.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision', '', 0, 0, 0, "Tronson tehnologic")


# Add Feature Fields
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "CODE_LOWER_STRING", "Long", None, None, "", "COD_SIRUTA_INFERIOARA", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "LOCATION", "Text", None, None, "15", "AMPLASARE", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "POST NAME", "Text", None, None, "30", "DENUMIRE_POST", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "VOLTAGE_KV", "Short", None, None, "", "TENSIUNE_KV", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "NR_TOTAL_UNITS", "Short", None, None, "", "NR_TOTAL_UNITATI", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "TOTAL_INSTALLED_POWER_MVA", "Short", None, None, "", "PUTERE_INSTALATA_TOTALA_MVA", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "CUI_OPERATOR", "Text", None, None, "20", "CUI_OPERATOR", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "NR_INVENTAR", "Text", None, None, "20", "NR_INVENTAR", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "ACCOUNT_VALUE_LEI", "Double", None, None, "", "VALOARE_CONTABILA_LEI", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "NR_PVRTL", "Text", None, None, "20", "NR_PVRTL", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "DATA_PVRTL", "Date", None, None, "", "DATA_PVRTL", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "STATION_TYPE", "Text", None, None, "15", "TIP_STATIE", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "STATION NAME", "Text", None, None, "30", "DENUMIRE_STATIE", "NULLABLE", "NON_REQUIRED", None)


arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "CODE_LOWER_STRING", "Long", None, None, "", "COD_SIRUTA_INFERIOARA", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "LOCATION", "Text", None, None, "15", "AMPLASARE", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "STATION NAME", "Text", None, None, "30", "DENUMIRE_STATIE", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "LINE_NAME", "Text", None, None, "30", "LINE_NAME", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "VOLTAGE_KV", "Short", None, None, "", "TENSIUNE_KV", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "LENGTH_KM", "Double", None, None, "", "LUNGIME_KM", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "CUI_OPERATOR", "Text", None, None, "20", "CUI_OPERATOR", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "NR_INVENTAR", "Text", None, None, "20", "NR_INVENTAR", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "ACCOUNT_VALUE_LEI", "Double", None, None, "", "VALOARE_CONTABILA_LEI", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "NR_PVRTL", "Text", None, None, "20", "NR_PVRTL", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "DATA_PVRTL", "Date", None, None, "", "DATA_PVRTL", "NULLABLE", "NON_REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "TYPE_LINE_VOLTAGE", "Text", None, None, "15", "TIP_TENSIUNE_LINIE", "NULLABLE", "NON_REQUIRED", None)



# Add Global IDs (Data Management)
#arcpy.management.AddGlobalIDs(in_datasets)
#arcpy.management.AddGlobalIDs("'Statie Post';'Tronson tehnologic'")
#arcpy.management.AddGlobalIDs("'D:\my new task\project_ro\windfarmfgdb.gdb\Conductor';'D:\my new task\project_ro\windfarmfgdb.gdb\Station'")
#arcpy.management.AddGlobalIDs("D:\my new task\project_ro\windfarmfgdb.gdb\Conductor")
#arcpy.management.AddGlobalIDs("D:\my new task\project_ro\windfarmfgdb.gdb\Station")
arcpy.management.AddGlobalIDs("D:\my new task\project_ro\windfarmfgdb.gdb\Electric")

# Create Domain
arcpy.management.CreateDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Location Type", "Power line location: overhead or underground", "TEXT", "CODED", "DUPLICATE", "DEFAULT")
arcpy.management.CreateDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Station Type", "Power line location: overhead or underground", "TEXT", "CODED", "DUPLICATE", "DEFAULT")
arcpy.management.CreateDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Type", "Power line location: overhead or underground", "TEXT", "CODED", "DUPLICATE", "DEFAULT")
arcpy.management.CreateDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Value", "Voltage in kV at the power station: 0 kV; 0,23 kV; 0,4 kV; 20 kV; 110 kV", "LONG", "CODED", "DUPLICATE", "DEFAULT")

# Add Coded Value To Domain
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Location Type",1, "overhead")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Location Type",2, "underground")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Location Type",3, "ground")

arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Station Type",1, "connection")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Station Type",2, "transformation")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Station Type",3, "connection_transformation")

arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Type",1, "low")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Type",2, "medium")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Type",3, "high")

arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Value",0, "0 kV")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Value",230, "0,23 kV")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Value",400, "0,4 kV")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Value",20000, "20 kV")
arcpy.management.AddCodedValueToDomain(r"D:\my new task\project_ro\windfarmfgdb.gdb", "Voltage Value",110000, "110 kV")

# Assign Domain to a Field
arcpy.management.AssignDomainToField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "VOLTAGE_KV", "Voltage Value", None)
arcpy.management.AssignDomainToField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "VOLTAGE_KV", "Voltage Value", None)
arcpy.management.AssignDomainToField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "LOCATION", "Location Type", None)
arcpy.management.AssignDomainToField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "LOCATION", "Location Type", None)
arcpy.management.AssignDomainToField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "STATION_TYPE", "Station Type", None)
arcpy.management.AssignDomainToField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "TYPE_LINE_VOLTAGE", "Voltage Type", None)

# Add SUBTYPE_CD field
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "SUBTYPE_CD", "Short", None, None, "", "SUBTYPE_CD", "NULLABLE", "REQUIRED", None)
arcpy.management.AddField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "SUBTYPE_CD", "Short", None, None, "", "SUBTYPE_CD", "NULLABLE", "REQUIRED", None)

# Set Subtype Field
arcpy.management.SetSubtypeField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", "SUBTYPE_CD", "DO_NOT_CLEAR")
arcpy.management.SetSubtypeField("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", "SUBTYPE_CD", "DO_NOT_CLEAR")

# Add Subtype
arcpy.management.AddSubtype("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", 0, "Substation")
arcpy.management.AddSubtype("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Station", 1, "Transformer station")

arcpy.management.AddSubtype("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", 0, "Underground Conductor")
arcpy.management.AddSubtype("D:\my new task\project_ro\windfarmfgdb.gdb\Electric\Conductor", 1, "Overhead Conductor")

# Generate Schema Report
arcpy.management.GenerateSchemaReport("D:\my new task", "schema_report", ["JSON", "PDF", "HTML", "XLSX"])

print("Update was successful")