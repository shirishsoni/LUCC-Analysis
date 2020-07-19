# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Generate Clusters.py
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Set overwrite property true
arcpy.env.overwriteOutput = True

# Script arguments
# Obtain the Workspace
Workspace = arcpy.GetParameterAsText(0)
if Workspace == '#' or not Workspace:
	Workspace = "R:\\GIS Project"

# Band Images for the First Image
First_LandSat_Image_Red_Band__B3_ = arcpy.GetParameterAsText(1)
if First_LandSat_Image_Red_Band__B3_ == '#' or not First_LandSat_Image_Red_Band__B3_:
    First_LandSat_Image_Red_Band__B3_ = Workspace + "\\LT05_L1TP_035025_19870426_20170213_01_T1_B3.TIF" # provide a default value if unspecified

First_LandSat_Image_Green_Band__B2_ = arcpy.GetParameterAsText(2)
if First_LandSat_Image_Green_Band__B2_ == '#' or not First_LandSat_Image_Green_Band__B2_:
    First_LandSat_Image_Green_Band__B2_ = Workspace + "\\LandSat07_1987\\LT05_L1TP_035025_19870426_20170213_01_T1_B2.TIF" # provide a default value if unspecified

First_LandSat_Image_Blue_Band__B1_ = arcpy.GetParameterAsText(3)
if First_LandSat_Image_Blue_Band__B1_ == '#' or not First_LandSat_Image_Blue_Band__B1_:
    First_LandSat_Image_Blue_Band__B1_ = Workspace + "\\LandSat07_1987\\LT05_L1TP_035025_19870426_20170213_01_T1_B1.TIF" # provide a default value if unspecified

# Band Images for the Second Image
Second_LandSat_Image_Red_Band__B3_ = arcpy.GetParameterAsText(4)
if Second_LandSat_Image_Red_Band__B3_ == '#' or not Second_LandSat_Image_Red_Band__B3_:
    Second_LandSat_Image_Red_Band__B3_ = "R:\\GIS Project\\LandSat07_2002\\LE07_L1TP_036025_20020520_20170130_01_T1_B3.TIF" # provide a default value if unspecified

Second_LandSat_Image_Green_Band__B2_ = arcpy.GetParameterAsText(5)
if Second_LandSat_Image_Green_Band__B2_ == '#' or not Second_LandSat_Image_Green_Band__B2_:
    Second_LandSat_Image_Green_Band__B2_ = "R:\\GIS Project\\LandSat07_2002\\LE07_L1TP_036025_20020520_20170130_01_T1_B2.TIF" # provide a default value if unspecified

Second_LandSat_Image_Blue_Band__B1_ = arcpy.GetParameterAsText(6)
if Second_LandSat_Image_Blue_Band__B1_ == '#' or not Second_LandSat_Image_Blue_Band__B1_:
    Second_LandSat_Image_Blue_Band__B1_ = "R:\\GIS Project\\LandSat07_2002\\LE07_L1TP_036025_20020520_20170130_01_T1_B1.TIF" # provide a default value if unspecified

# Band Images for the Third Image
Third_LandSat_Image_Red_Band__B3_ = arcpy.GetParameterAsText(7)
if Third_LandSat_Image_Red_Band__B3_ == '#' or not Third_LandSat_Image_Red_Band__B3_:
    Third_LandSat_Image_Red_Band__B3_ = "R:\\GIS Project\\LandSat07_2017\\LC08_L1TP_035025_20171005_20171014_01_T1_B3.TIF" # provide a default value if unspecified

Third_LandSat_Image_Green_Band__B2_ = arcpy.GetParameterAsText(8)
if Third_LandSat_Image_Green_Band__B2_ == '#' or not Third_LandSat_Image_Green_Band__B2_:
    Third_LandSat_Image_Green_Band__B2_ = "R:\\GIS Project\\LandSat07_2017\\LC08_L1TP_035025_20171005_20171014_01_T1_B2.TIF" # provide a default value if unspecified

Third_LandSat_Image_Blue_Band__B1_ = arcpy.GetParameterAsText(9)
if Third_LandSat_Image_Blue_Band__B1_ == '#' or not Third_LandSat_Image_Blue_Band__B1_:
    Third_LandSat_Image_Blue_Band__B1_ = "R:\\GIS Project\\LandSat07_2017\\LC08_L1TP_035025_20171005_20171014_01_T1_B1.TIF" # provide a default value if unspecified

# Clipping Feature value
Clipping_feature_class = arcpy.GetParameterAsText(10)
if Clipping_feature_class == '#' or not Clipping_feature_class:
    Clipping_feature_class = "city_limits" # provide a default value if unspecified

# Output Result File Names
IsoCluster_first_image = arcpy.GetParameterAsText(11)
if IsoCluster_first_image == '#' or not IsoCluster_first_image:
    IsoCluster_first_image = Workspace + "\\combined_1987_Clip_IsoCluste" # provide a default value if unspecified

IsoCluster_second_image = arcpy.GetParameterAsText(12)
if IsoCluster_second_image == '#' or not IsoCluster_second_image:
    IsoCluster_second_image = Workspace + "\\Project Geodatabase.gdb\\combined_2002_Clip_IsoCluste" # provide a default value if unspecified

IsoCluster_third_image = arcpy.GetParameterAsText(13)
if IsoCluster_third_image == '#' or not IsoCluster_third_image:
    IsoCluster_third_image = Workspace + "\\Project Geodatabase.gdb\\combined_2017_Clip_IsoCluste" # provide a default value if unspecified

# IsoCluster Classes variable
IsoCluster_Classes = arcpy.GetParameterAsText(14)
if IsoCluster_Classes == '#' or not IsoCluster_Classes:
	IsoCluster_Classes = 25


# Local variables:
combined_1987 = Workspace + "\\Project Geodatabase.gdb\\combined_1987"
combined_1987_Clip = Workspace + "\\Project Geodatabase.gdb\\combined_1987_Clip"
Output_signature_file = ""
combined_2002 = Workspace + "\\Project Geodatabase.gdb\\combined_2002"
combined_2002_Clip = Workspace + "\\Project Geodatabase.gdb\\combined_2002_Clip"
Output_signature_file__2_ = ""
combined_2017 = Workspace + "\\Project Geodatabase.gdb\\combined_2017"
combined_2017_Clip = Workspace + "\\Project Geodatabase.gdb\\combined_2017_Clip"
Output_signature_file__3_ = ""

# Band List Variables
rasterList01 = [First_LandSat_Image_Red_Band__B3_, First_LandSat_Image_Green_Band__B2_, First_LandSat_Image_Blue_Band__B1_]
rasterList02 = [Second_LandSat_Image_Red_Band__B3_, Second_LandSat_Image_Green_Band__B2_, Second_LandSat_Image_Blue_Band__B1_]
rasterList03 = [Third_LandSat_Image_Red_Band__B3_, Third_LandSat_Image_Green_Band__B2_, Third_LandSat_Image_Blue_Band__B1_]

# Calculate Clipping Extent
Description = arcpy.Describe(Clipping_feature_class)
MinX = Description.extent.XMin
MaxX = Description.extent.XMax
MinY = Description.extent.YMin
MaxY = Description.extent.YMax

Extent = str(MinX) + " " + str(MinY) + " " + str(MaxX) + " " + str(MaxY)

# Process: Composite Bands for First Image
#arcpy.CompositeBands_management("'R:\\GIS Project\\LandSat07_1987\\LT05_L1TP_035025_19870426_20170213_01_T1_B3.TIF';'R:\\GIS Project\\LandSat07_1987\\LT05_L1TP_035025_19870426_20170213_01_T1_B2.TIF';'R:\\GIS Project\\LandSat07_1987\\LT05_L1TP_035025_19870426_20170213_01_T1_B1.TIF'", combined_1987)
arcpy.CompositeBands_management(rasterList01, combined_1987)

# Process: Clip First Image
arcpy.Clip_management(combined_1987, Extent, combined_1987_Clip, Clipping_feature_class, "256", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Iso Cluster Unsupervised Classification Firsta Image
arcpy.gp.IsoClusterUnsupervisedClassification_sa(combined_1987_Clip, IsoCluster_Classes, IsoCluster_first_image, "20", "10", Output_signature_file)

# Process: Composite Bands for Second Image
arcpy.CompositeBands_management(rasterList02, combined_2002)

# Process: Clip Second Image
arcpy.Clip_management(combined_2002, Extent, combined_2002_Clip, Clipping_feature_class, "256", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Iso Cluster Unsupervised Classification Second Image
arcpy.gp.IsoClusterUnsupervisedClassification_sa(combined_2002_Clip, IsoCluster_Classes, IsoCluster_second_image, "20", "10", Output_signature_file__2_)

# Process: Composite Bands for Third Image
arcpy.CompositeBands_management(rasterList03, combined_2017)

# Process: Clip Third Image
arcpy.Clip_management(combined_2017, Extent, combined_2017_Clip, Clipping_feature_class, "65535", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Iso Cluster Unsupervised Classification Third Image
arcpy.gp.IsoClusterUnsupervisedClassification_sa(combined_2017_Clip, IsoCluster_Classes, IsoCluster_third_image, "20", "10", Output_signature_file__3_)

