class Element(object):
	"""Element class"""
	def __init__(self, elementName, molarMass):
		self.elementName = elementName
		self.molarMass = molarMass

		
hydrogen = Element("Hydrogen", 1.01)
helium = Element("Helium", 4.00)
lithium = Element("Lithium", 6.94)
#This would continue until every element is listed in this format

avagadro = 6.022 * 10**23

def gramsToMoles(grams, elementName):
	moles = grams/elementName.molarMass
	print moles

def molesToGrams(moles, elementName):
	grams = moles*elementName.molarMass
	print grams

def gramsToMolecules(grams, elementName):
	molecules = (grams/elementName.molarMass) * avagadro
	print molecules

def moleculesToGrams(molecules, elementName):
	grams = (molecules/avagadro) * elementName.molarMass
	print grams

def molesToMolecules(moles):
	molecules = moles*avagadro
	print molecules

def moleculesToMoles(molecules):
	moles = molecules/avagadro
	print moles0

gramsToMoles(10, hydrogen)
#This line tests the function
