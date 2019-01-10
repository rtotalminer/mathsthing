import math
import os

def menu():
	os.system("cls")
	print("\n[1] Calculate for F")
	print("\n[2] Similarities Between the Sequence of Squared Numbers")
	print("\n[3] Similarities Between the Sequence of Cubed Numbers")
	print("\n[4] Similarities Between the Sequence of Tesseratic Numbers")
	print("\n[5] N'th Term Calculator")
	i = input("\n>>> ")
	if i == "1":
		os.system("cls")
		calculateF()
	if i == "2":
		os.system("cls")
		squarednumbers()
	if i == "3":
		os.system("cls")
		cubednumbers()
	if i == "4":
		os.system("cls")
		tesseraticnumbers()
	if i == "5":
		os.system("cls")
		ncalculator()
	else:
		os.system("cls")
		menu()

def calculateF():	
	mEarth = 6e+24 
	mSun = 2e+30
	rEarth = 6400000
	G = 6.67e-11
	dEarthSun = 150000000000
	print("\nMass of the Earth = '6e+24' ")
	print("Mass of the Sun = '2e+30' ")
	print("Distance from the Earth to the Sun = '150000000000' ")
	m1 = float(input("\nMass of first object: "))
	m2 = float(input("Mass of second object: "))
	m3 = m1*m2 
	r = int(input("Distance between bodies: "))
	r2 = r*r
	FG = m3 / r2
	F = G * FG
	print(str(format(F, "f")) + " N")
	input()

def to_infinity():
    index=0
    while 1:
        yield index
        index += 1

def squarednumbers():
	print("Similarities Between the Sequence of Squared Numbers")
	for i in range(1,101):
		sqN = i ** 2
		swN = (i-1) ** 2
		sq = sqN - swN 
		q = sqN / sq
		b = math.sqrt(sq)  
		print("\n\n[n]", i, "Squared = ", sqN, "\n[b] Differnece From Last Number = ", sq, "\n[n/b] Squared Number Divided By Difference ", q, "\n[sqrt(b)] ", b)
	input()

def cubednumbers():
	print("Similarities Between the Sequence of Cubed Numbers")
	for i in range(1,101):
		sqN = i ** 3
		swN = (i-1) ** 3
		sq = sqN - swN 
		q = sqN / sq
		b = math.sqrt(sq)  
		print("\n\n[n]", i, "Cubed = ", sqN, "\n[b] Differnece From Last Number = ", sq, "\n[n/b] Squared Number Divided By Difference ", q, "\n[sqrt(b)] ", b)
	input()

def tesseraticnumbers():
	print("Similarities Between the Sequence of Tesseratic Numbers")
	for i in range(1,101):
		sqN = i ** 4
		swN = (i-1) ** 4
		sq = sqN - swN 
		q = sqN / sq
		b = math.sqrt(sq)  
		print("\n\n[n]", i, "Tesseratic = ", sqN, "\n[b] Differnece From Last Number = ", sq, "\n[n/b] Squared Number Divided By Difference ", q, "\n[sqrt(b)] ", b)
	input()
"""
def ncalculator():
	nlist = []
	for n in range(4):
		nlist.append(input("Enter Number " + str(n+1) + ": "))
	os.system("cls")
	print(nlist, "Are you content with this list? [y] [n]")
	ui = input(">>>")
	if ui.lower() == "n":
		os.system("cls")
		ncalculator()
	else:
		pass
	
	for i in nlist:
		 
		

		# i == ['i','i','i','i']

	
	

	
	


	input()
"""
while True:
	menu()
