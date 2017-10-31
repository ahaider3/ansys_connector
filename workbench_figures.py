'''
A simple script for generating ansys structures
'''

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateSphere(
	[
		"NAME:SphereParameters",
		"XCenter:="		, "0.8mm",
		"YCenter:="		, "0.9mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "0.608276253029822mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Sphere1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.CreateSphere(
	[
		"NAME:SphereParameters",
		"XCenter:="		, "1.2mm",
		"YCenter:="		, "2.4mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "0.282842712474619mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Sphere2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.CreateCone(
	[
		"NAME:ConeParameters",
		"XCenter:="		, "2.8mm",
		"YCenter:="		, "0.5mm",
		"ZCenter:="		, "0mm",
		"WhichAxis:="		, "Z",
		"Height:="		, "0.2mm",
		"BottomRadius:="	, "0.316227766016838mm",
		"TopRadius:="		, "0.632455532033676mm"
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
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "2.6mm",
		"YPosition:="		, "3.8mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "0.4mm",
		"YSize:="		, "1mm",
		"ZSize:="		, "0.8mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "3.8mm",
		"YPosition:="		, "2mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "0.6mm",
		"YSize:="		, "1.4mm",
		"ZSize:="		, "1mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.CreateTorus(
	[
		"NAME:TorusParameters",
		"XCenter:="		, "3.8mm",
		"YCenter:="		, "0.2mm",
		"ZCenter:="		, "0mm",
		"MajorRadius:="		, "0.723606797749979mm",
		"MinorRadius:="		, "0.276393202250021mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Torus1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Torus1"
	])
oEditor.CreateTorus(
	[
		"NAME:TorusParameters",
		"XCenter:="		, "5.4mm",
		"YCenter:="		, "0.2mm",
		"ZCenter:="		, "0mm",
		"MajorRadius:="		, "0.647213595499958mm",
		"MinorRadius:="		, "0.247213595499958mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Torus1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
