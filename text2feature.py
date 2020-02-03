import sitepackages
import	arcpy, os

try:
	# create workspace
	workspace = arcpy.GetParameterAsText(0)
	txtfile = arcpy.GetParameterAsText(1)
	fc = arcpy.GetParameterAsText(2)
	# open the text file
	open (txtfile, "r")
	# read the text file
	liststadiums = f.readlines()
	# create cursor for iterating through the text file
	cursor = arcpy.InsertCursor(fc)
	for stadiums in liststadiums:
		if "latitude" in stadiums:
			continue
		vals = stadiums.split("   ")
		latitude = float(vals[2])
		longitude = float(vals[1])
		location = str(vals[0])

		pnt = arcpy.Point(longitude,latitude)
		feat = cursor.newRow()
		feat.shape = pnt
		feat.setValue("LOCATION",location)
		cursor.insertRow(feat)


except:

	print arcpy.GetMessages()

finally:
	del cursor
	f.close

