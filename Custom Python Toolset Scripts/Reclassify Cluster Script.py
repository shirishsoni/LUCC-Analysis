# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Reclassify Cluster Script.py
# Usage: Reclassify Cluster Script <combined_2002_Clip_IsoCluste01> <combined_2017_Clip_IsoCluste01> <Project_Geodatabase_gdb> 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Set overwrite property true
arcpy.env.overwriteOutput = True

# Script arguments
combined_2002_Clip_IsoCluste01 = arcpy.GetParameterAsText(0)
if combined_2002_Clip_IsoCluste01 == '#' or not combined_2002_Clip_IsoCluste01:
    combined_2002_Clip_IsoCluste01 = "combined_2002_Clip_IsoCluste01" # provide a default value if unspecified

combined_2017_Clip_IsoCluste01 = arcpy.GetParameterAsText(1)
if combined_2017_Clip_IsoCluste01 == '#' or not combined_2017_Clip_IsoCluste01:
    combined_2017_Clip_IsoCluste01 = "combined_2017_Clip_IsoCluste01" # provide a default value if unspecified

Project_Geodatabase_gdb = arcpy.GetParameterAsText(2)
if Project_Geodatabase_gdb == '#' or not Project_Geodatabase_gdb:
    Project_Geodatabase_gdb = "R:\\GIS Project\\Project Geodatabase.gdb" # provide a default value if unspecified

# Local variables:
Reclass_comb1 = Project_Geodatabase_gdb + "\\Reclass_comb1"
Reclass_comb2 = Project_Geodatabase_gdb + "\\Reclass_comb2"
Project_Geodatabase_gdb__2_ = Project_Geodatabase_gdb
Input_reclass_images = Reclass_comb1 + ";" + Reclass_comb2

# Process: Reclassify
arcpy.gp.Reclassify_sa(combined_2002_Clip_IsoCluste01, "Value", "1 1;2 1;3 2;4 4;5 3;6 5;7 2;8 1;9 4;10 5;11 3;12 3;13 3;14 5;15 2;16 4;17 4;18 3;19 4;20 5;21 3;22 5;23 4", Reclass_comb1, "DATA")

# Process: Reclassify (3)
arcpy.gp.Reclassify_sa(combined_2017_Clip_IsoCluste01, "Value", "1 1;2 1;3 3;4 4;5 5;6 2;7 3;8 4;9 5;10 3;11 2;12 3;13 2;14 4;15 1;16 3;17 5;18 3;19 3;20 3;21 5;22 4;23 3;24 5", Reclass_comb2, "DATA")

# Process: Raster To Other Format (multiple)
arcpy.RasterToOtherFormat_conversion(Input_reclass_images, Project_Geodatabase_gdb, "TIFF")
