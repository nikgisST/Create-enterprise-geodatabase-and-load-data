import arcpy

arcpy.management.CreateDataLoadingWorkspace(
    source_target_mapping=r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Подстанция_СрН' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Station;"
                          r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Възлова_станция_ВС' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Station;"
                          r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Разпределителна_станция_ТП' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Station;"
                          r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Проводник_СрН_въздушна_изолирана_линия' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Conductor;"
                          r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Проводник_СрН_въздушна_линия' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Conductor;"
                          r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Проводник_СрН_подземна_линия' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Conductor;"
                          r"'C:\Users\nikole\Documents\new_task\autocad_files\CEZ Wind Farm-Бръшляница-PL1102-20 kV_new.dxf\Проводник_СрН_други' "
                          r"D:\gis\gdb\cezwindfarm.gdb\Electric\Conductor",
    out_folder=r"C:\Users\nikole\Documents\new_task",
    match_options=None,
    mapping_table="Create_Data_Loading_Workspace_Mapping_Table",
    calc_stats="NO_STATS",
    match_subtypes="NO_MATCH_SUBTYPES"
)