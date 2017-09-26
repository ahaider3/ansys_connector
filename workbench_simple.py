# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2016.1.0
# 12:34:02  Sep 26, 2017
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCone(
	[
		"NAME:ConeParameters",
		"XCenter:="		, "1.2mm",
		"YCenter:="		, "2mm",
		"ZCenter:="		, "0mm",
		"WhichAxis:="		, "Z",
		"Height:="		, "1.4mm",
		"BottomRadius:="	, "1.2369316876853mm",
		"TopRadius:="		, "2.61725046566048mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cone1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
