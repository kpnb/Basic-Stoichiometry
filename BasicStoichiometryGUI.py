from Tkinter import *
import ttk

class Element(object):
    """Element class"""
    def __init__(self, elementName, molarMass):
        self.elementName = elementName
        self.molarMass = molarMass
 
    def __str__(self):
        return self.elementName
 
    def __repr__(self):
        return str(self) + ' (' + str(self.molarMass) + ')'

 
data = '''1		1.01	Hydrogen	H	-259	-253	0.09	0.14	1776	1	1s1	13.5984
2		4.00	Helium	He	-272	-269	0.18		1895	18	1s2	24.5874
3		6.94	Lithium	Li	180	1347	0.53		1817	1	[He] 2s1	5.3917
4		9.01	Beryllium	Be	1278	2970	1.85		1797	2	[He] 2s2	9.3227
5		10.81	Boron	B	2300	2550	2.34		1808	13	[He] 2s2 2p1	8.298
6		12.01	Carbon	C	3500	4827	2.26	0.094	ancient	14	[He] 2s2 2p2	11.2603
7		14.01	Nitrogen	N	-210	-196	1.25		1772	15	[He] 2s2 2p3	14.5341
8		16.00	Oxygen	O	-218	-183	1.43	46.71	1774	16	[He] 2s2 2p4	13.6181
9		19.00	Fluorine	F	-220	-188	1.7	0.029	1886	17	[He] 2s2 2p5	17.4228
10		20.18	Neon	Ne	-249	-246	0.9		1898	18	[He] 2s2 2p6	21.5645
11		22.99	Sodium	Na	98	883	0.97	2.75	1807	1	[Ne] 3s1	5.1391
12		24.31	Magnesium	Mg	639	1090	1.74	2.08	1755	2	[Ne] 3s2	7.6462
13		26.98	Aluminum	Al	660	2467	2.7	8.07	1825	13	[Ne] 3s2 3p1	5.9858
14		28.09	Silicon	Si	1410	2355	2.33	27.69	1824	14	[Ne] 3s2 3p2	8.1517
15		30.97	Phosphorus	P	44	280	1.82	0.13	1669	15	[Ne] 3s2 3p3	10.4867
16		32.07	Sulfur	S	113	445	2.07	0.052	ancient	16	[Ne] 3s2 3p4	10.36
17		35.45	Chlorine	Cl	-101	-35	3.21	0.045	1774	17	[Ne] 3s2 3p5	12.9676
18		39.95	Argon	Ar	-189	-186	1.78		1894	18	[Ne] 3s2 3p6	15.7596
19		39.10	Potassium	K	64	774	0.86	2.58	1807	1	[Ar] 4s1	4.3407
20		40.08	Calcium	Ca	839	1484	1.55	3.65	1808	2	[Ar] 4s2	6.1132
21		44.96	Scandium	Sc	1539	2832	2.99		1879	3	[Ar] 3d1 4s2	6.5615
22		47.87	Titanium	Ti	1660	3287	4.54	0.62	1791	4	[Ar] 3d2 4s2	6.8281
23		50.94	Vanadium	V	1890	3380	6.11		1830	5	[Ar] 3d3 4s2	6.7462
24		52.00	Chromium	Cr	1857	2672	7.19	0.035	1797	6	[Ar] 3d5 4s1	6.7665
25		54.94	Manganese	Mn	1245	1962	7.43	0.09	1774	7	[Ar] 3d5 4s2	7.434
26		55.85	Iron	Fe	1535	2750	7.87	5.05	ancient	8	[Ar] 3d6 4s2	7.9024
27		58.93	Cobalt	Co	1495	2870	8.9		1735	9	[Ar] 3d7 4s2	7.881
28		58.69	Nickel	Ni	1453	2732	8.9	0.019	1751	10	[Ar] 3d8 4s2	7.6398
29		63.55	Copper	Cu	1083	2567	8.96		ancient	11	[Ar] 3d10 4s1	7.7264
30		65.39	Zinc	Zn	420	907	7.13		ancient	12	[Ar] 3d10 4s2	9.3942
31		69.72	Gallium	Ga	30	2403	5.91		1875	13	[Ar] 3d10 4s2 4p1	5.9993
32		72.64	Germanium	Ge	937	2830	5.32		1886	14	[Ar] 3d10 4s2 4p2	7.8994
33		74.92	Arsenic	As	81	613	5.72		ancient	15	[Ar] 3d10 4s2 4p3	9.7886
34		78.96	Selenium	Se	217	685	4.79		1817	16	[Ar] 3d10 4s2 4p4	9.7524
35		79.90	Bromine	Br	-7	59	3.12		1826	17	[Ar] 3d10 4s2 4p5	11.8138
36		83.80	Krypton	Kr	-157	-153	3.75		1898	18	[Ar] 3d10 4s2 4p6	13.9996
37		85.47	Rubidium	Rb	39	688	1.63		1861	1	[Kr] 5s1	4.1771
38		87.62	Strontium	Sr	769	1384	2.54		1790	2	[Kr] 5s2	5.6949
39		88.91   Yttrium	Y	1523	3337	4.47		1794	3	[Kr] 4d1 5s2	6.2173
40		91.22	Zirconium	Zr	1852	4377	6.51	0.025	1789	4	[Kr] 4d2 5s2	6.6339
41		92.91	Niobium	Nb	2468	4927	8.57		1801	5	[Kr] 4d4 5s1	6.7589
42		95.94	Molybdenum	Mo	2617	4612	10.22		1781	6	[Kr] 4d5 5s1	7.0924
43	*	98.00	Technetium	Tc	2200	4877	11.5		1937	7	[Kr] 4d5 5s2	7.28
44		101.07	Ruthenium	Ru	2250	3900	12.37		1844	8	[Kr] 4d7 5s1	7.3605
45		102.91	Rhodium	Rh	1966	3727	12.41		1803	9	[Kr] 4d8 5s1	7.4589
46		106.42	Palladium	Pd	1552	2927	12.02		1803	10	[Kr] 4d10	8.3369
47		107.87	Silver	Ag	962	2212	10.5		ancient	11	[Kr] 4d10 5s1	7.5762
48		112.41	Cadmium	Cd	321	765	8.65		1817	12	[Kr] 4d10 5s2	8.9938
49		114.82	Indium	In	157	2000	7.31		1863	13	[Kr] 4d10 5s2 5p1	5.7864
50		118.71	Tin	Sn	232	2270	7.31		ancient	14	[Kr] 4d10 5s2 5p2	7.3439
51		121.76	Antimony	Sb	630	1750	6.68		ancient	15	[Kr] 4d10 5s2 5p3	8.6084
52		127.60	Tellurium	Te	449	990	6.24		1783	16	[Kr] 4d10 5s2 5p4	9.0096
53		126.91	Iodine	I	114	184	4.93		1811	17	[Kr] 4d10 5s2 5p5	10.4513
54		131.29	Xenon	Xe	-112	-108	5.9		1898	18	[Kr] 4d10 5s2 5p6	12.1298
55		132.91	Cesium	Cs	29	678	1.87		1860	1	[Xe] 6s1	3.8939
56		137.33	Barium	Ba	725	1140	3.59	0.05	1808	2	[Xe] 6s2	5.2117
57		138.91	Lanthanum	La	920	3469	6.15		1839	3	[Xe] 5d1 6s2	5.5769
58		140.12	Cerium	Ce	795	3257	6.77		1803	101	[Xe] 4f1 5d1 6s2	5.5387
59		140.91	Praseodymium	Pr	935	3127	6.77		1885	101	[Xe] 4f3 6s2	5.473
60		144.24	Neodymium	Nd	1010	3127	7.01		1885	101	[Xe] 4f4 6s2	5.525
61	*	145	Promethium	Pm	1100	3000	7.3		1945	101	[Xe] 4f5 6s2	5.582
62		150.36	Samarium	Sm	1072	1900	7.52		1879	101	[Xe] 4f6 6s2	5.6437
63		151.96	Europium	Eu	822	1597	5.24		1901	101	[Xe] 4f7 6s2	5.6704
64		157.25	Gadolinium	Gd	1311	3233	7.9		1880	101	[Xe] 4f7 5d1 6s2	6.1501
65		158.93	Terbium	Tb	1360	3041	8.23		1843	101	[Xe] 4f9 6s2	5.8638
66		162.50	Dysprosium	Dy	1412	2562	8.55		1886	101	[Xe] 4f10 6s2	5.9389
67		164.93	Holmium	Ho	1470	2720	8.8		1867	101	[Xe] 4f11 6s2	6.0215
68		167.26	Erbium	Er	1522	2510	9.07		1842	101	[Xe] 4f12 6s2	6.1077
69		168.93	Thulium	Tm	1545	1727	9.32		1879	101	[Xe] 4f13 6s2	6.1843
70		173.04	Ytterbium	Yb	824	1466	6.9		1878	101	[Xe] 4f14 6s2	6.2542
71		174.97	Lutetium	Lu	1656	3315	9.84		1907	101	[Xe] 4f14 5d1 6s2	5.4259
72		178.49	Hafnium	Hf	2150	5400	13.31		1923	4	[Xe] 4f14 5d2 6s2	6.8251
73		180.95	Tantalum	Ta	2996	5425	16.65		1802	5	[Xe] 4f14 5d3 6s2	7.5496
74		183.84	Tungsten	W	3410	5660	19.35		1783	6	[Xe] 4f14 5d4 6s2	7.864
75		186.21	Rhenium	Re	3180	5627	21.04		1925	7	[Xe] 4f14 5d5 6s2	7.8335
76		190.23	Osmium	Os	3045	5027	22.6		1803	8	[Xe] 4f14 5d6 6s2	8.4382
77		192.22	Iridium	Ir	2410	4527	22.4		1803	9	[Xe] 4f14 5d7 6s2	8.967
78		195.08	Platinum	Pt	1772	3827	21.45		1735	10	[Xe] 4f14 5d9 6s1	8.9587
79		196.97	Gold	Au	1064	2807	19.32		ancient	11	[Xe] 4f14 5d10 6s1	9.2255
80		200.59	Mercury	Hg	-39	357	13.55		ancient	12	[Xe] 4f14 5d10 6s2	10.4375
81		204.38	Thallium	Tl	303	1457	11.85		1861	13	[Xe] 4f14 5d10 6s2 6p1	6.1082
82		207.20	Lead	Pb	327	1740	11.35		ancient	14	[Xe] 4f14 5d10 6s2 6p2	7.4167
83		208.98	Bismuth	Bi	271	1560	9.75		ancient	15	[Xe] 4f14 5d10 6s2 6p3	7.2856
84	*	209	Polonium	Po	254	962	9.3		1898	16	[Xe] 4f14 5d10 6s2 6p4	8.417
85	*	210	Astatine	At	302	337			1940	17	[Xe] 4f14 5d10 6s2 6p5	9.3
86	*	222	Radon	Rn	-71	-62	9.73		1900	18	[Xe] 4f14 5d10 6s2 6p6	10.7485
87	*	223	Francium	Fr	27	677			1939	1	[Rn] 7s1	4.0727
88	*	226	Radium	Ra	700	1737	5.5		1898	2	[Rn] 7s2	5.2784
89	*	227	Actinium	Ac	1050	3200	10.07		1899	3	[Rn] 6d1 7s2	5.17
90		232.04	Thorium	Th	1750	4790	11.72		1829	102	[Rn] 6d2 7s2	6.3067
91		231.04	Protactinium	Pa	1568		15.4		1913	102	[Rn] 5f2 6d1 7s2	5.89
92		238.03	Uranium	U	1132	3818	18.95		1789	102	[Rn] 5f3 6d1 7s2	6.1941
93	*	237	Neptunium	Np	640	3902	20.2		1940	102	[Rn] 5f4 6d1 7s2	6.2657
94	*	244	Plutonium	Pu	640	3235	19.84		1940	102	[Rn] 5f6 7s2	6.0262
95	*	243	Americium	Am	994	2607	13.67		1944	102	[Rn] 5f7 7s2	5.9738
96	*	247	Curium	Cm	1340		13.5		1944	102		5.9915
97	*	247	Berkelium	Bk	986		14.78		1949	102		6.1979
98	*	251	Californium	Cf	900		15.1		1950	102		6.2817
99	*	252	Einsteinium	Es	860				1952	102		6.42
100	*	257	Fermium	Fm	1527				1952	102		6.5
101	*	258	Mendelevium	Md					1955	102		6.58
102	*	259	Nobelium	No	827				1958	102		6.65
103	*	262	Lawrencium	Lr	1627				1961	102		4.9
104	*	261	Rutherfordium	Rf					1964	4
105	*	262	Dubnium	Db					1967	5
106	*	266	Seaborgium	Sg					1974	6
107	*	264	Bohrium	Bh					1981	7
108	*	277	Hassium	Hs					1984	8
109	*	268	Meitnerium	Mt					1982	9		'''
 
i = 1
x = 1
 
elements = dict()
for line in data.split('\n'):
    line = line.split()
 
    if line[1] == '*':
        line.remove(line[1])

    elements[i] = Element(line[2], float(line[1])) #Creates a class for every element and stores each class in the elements dict?? Maybe??
    i += 1

elementlist = []

for element in elements:
	elementlist.append(elements[x].elementName)
	x += 1

avagadro = 6.022 * 10**23

def gramsToMoles(grams, elementName):
	moles = float(grams)/elements[elementName].molarMass
	return moles

def molesToGrams(moles, elementName):
	grams = moles*elements[elementName].molarMass
	return grams

def gramsToMolecules(grams, elementName):
	molecules = (grams/elements[elementName].molarMass) * avagadro
	return molecules

def moleculesToGrams(molecules, elementName):
	grams = (molecules/avagadro) * elements[elementName].molarMass
	return grams

def molesToMolecules(moles):
	molecules = moles*avagadro
	return molecules

def moleculesToMoles(molecules):
	moles = molecules/avagadro
	return moles

def getGrams(entry_type_grams):
	entry_type_grams = grams

def getMoles(entry_type_moles):
	entry_type_grams = grams

def getAtoms(entry_type_atoms):
	entry_type_atoms = atoms

def calculate():
	pass

root = Tk()
root.title("Stoichiometry Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

grams = StringVar()
moles = StringVar()
atoms = StringVar()
elementName = StringVar()
elementSelector = StringVar()

spaceholder = Label(mainframe, text="This is a label").grid(row=0, column=0)

amounttext = Label(mainframe, text="Enter the amount of your substance").grid(row=0, column=1)
amounttext2 = Label(mainframe, text="and select your units").grid(row=1, column=1)

entry = ttk.Entry(mainframe, width=7).grid(column=1, row=2)

entry_type_grams = ttk.Radiobutton(mainframe, text="grams", variable=grams, value=entry, command=getGrams).grid(row=0, column=2)

entry_type_moles = ttk.Radiobutton(mainframe, text="moles", variable=moles, value=entry, command=getMoles).grid(row=1, column=2)

entry_type_atoms = ttk.Radiobutton(mainframe, text="atoms", variable=atoms, value=entry, command=getAtoms).grid(row=2, column=2)

elementSelectorLabel = Label(mainframe, text="Select your atom:").grid(column=3, row=0)

elementSelector = ttk.Combobox(mainframe, textvariable=elementName, values=elementlist).grid(column=3, row=2)

equivalentLabel = Label(mainframe, text="is equivalent to").grid(column=0, row=4)

resultLabel = Label(mainframe, text="result'll be here").grid(column=1, row=4)

result_type_grams = ttk.Radiobutton(mainframe, text="grams", variable=grams, value=entry, command=getGrams).grid(row=3, column=2)

result_type_moles = ttk.Radiobutton(mainframe, text="moles", variable=moles, value=entry, command=getMoles).grid(row=4, column=2)

result_type_atoms = ttk.Radiobutton(mainframe, text="atoms", variable=atoms, value=entry, command=getAtoms).grid(row=5, column=2)

calculate = ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=7)
#print elements[1].elementName
#print elements
#print elementlist

root.mainloop()