"""Func"""

def findmore3(evidence1, evidence2):
    """Find more3"""
    if evidence1 == "Ghost Writing" and evidence2 == "Ghost Writing":
        print("I think Yurei and Revenant, so one of them is the answer!!!.")
    elif evidence1 == "Spirit box" and evidence2 == "Spirit box":
        print("I think Wraith and Hantu, so one of them is the answer!!!.")
    elif evidence1 == "Fingerprints" and evidence2 == "Fingerprints":
        print("I think Revenant and Hantu, so one of them is the answer!!!.")
    elif evidence1 == "Freezing Temperature" and evidence2 == "Freezing Temperature":
        print("I think Wraith and Banshee, so one of them is the answer!!!.")
    elif evidence1 == "EMF Level 5" and evidence2 == "EMF Level 5":
        print("I think Phantom and Banshee, so one of them is the answer!!!.")
    elif evidence1 == "Ghost orb" and evidence2 == "Ghost orb":
        print("I think Phantom and Yurei, so one of them is the answer!!!.")
    else:
        print("I think Wraith, Phantom, Yurei, Banshee, \
Revenant and Hantu, so one of them is the answer!!!.")

def findmore2(evidence1, evidence2):
    """Find more2"""
    if (evidence1 == "Ghost Writing" or evidence2 == "Ghost Writing") and\
        (evidence1 == "No Evidence" or evidence2 == "No Evidence"):
        print("I think Yurei and Revenant, so one of them is the answer!!!.")
    elif (evidence1 == "Spirit box" or evidence2 == "Spirit box") and \
        (evidence1 == "No Evidence" or evidence2 == "No Evidence"):
        print("I think Wraith and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Fingerprints" or evidence2 == "Fingerprints") and \
        (evidence1 == "No Evidence" or evidence2 == "No Evidence"):
        print("I think Revenant and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Freezing Temperature" or evidence2 == "Freezing Temperature") and \
        (evidence1 == "No Evidence" or evidence2 == "No Evidence"):
        print("I think Wraith and Banshee, so one of them is the answer!!!.")
    elif (evidence1 == "EMF Level 5" or evidence2 == "EMF Level 5") and \
        (evidence1 == "No Evidence" or evidence2 == "No Evidence"):
        print("I think Phantom and Banshee, so one of them is the answer!!!.")
    elif (evidence1 == "Ghost orb" or evidence2 == "Ghost orb") and \
        (evidence1 == "No Evidence" or evidence2 == "No Evidence"):
        print("I think Phantom and Yurei, so one of them is the answer!!!.")
    else:
        findmore3(evidence1, evidence2)

def findmore(evidence1, evidence2):
    """Find more"""
    if (evidence1 == "Ghost Writing" or evidence2 == "Ghost Writing") and \
        (evidence1 == "Spirit box" or evidence2 == "Spirit box"):
        print("I think Wraith, Yurei, Revenant and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Ghost Writing" or evidence2 == "Ghost Writing") and \
        (evidence1 == "Freezing Temperature" or evidence2 == "Freezing Temperature"):
        print("I think Wraith, Yurei, Banshee and Revenant, so one of them is the answer!!!.")
    elif (evidence1 == "Ghost Writing" or evidence2 == "Ghost Writing") and \
        (evidence1 == "EMF Level 5" or evidence2 == "EMF Level 5"):
        print("I think Phantom, Yurei, Banshee and Revenant, so one of them is the answer!!!.")
    elif (evidence1 == "Spirit box" or evidence2 == "Spirit box") and \
        (evidence1 == "EMF Level 5" or evidence2 == "EMF Level 5"):
        print("I think Wraith, Phantom, Banshee and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Spirit box" or evidence2 == "Spirit box") and \
        (evidence1 == "Ghost orb" or evidence2 == "Ghost orb"):
        print("I think Wraith, Phantom, Yurei and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Fingerprints" or evidence2 == "Fingerprints") and \
        (evidence1 == "Freezing Temperature" or evidence2 == "Freezing Temperature"):
        print("I think Wraith, Banshee, Revenant and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Fingerprints" or evidence2 == "Fingerprints") and \
        (evidence1 == "EMF Level 5" or evidence2 == "EMF Level 5"):
        print("I think Phantom, Banshee, Revenant and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Fingerprints" or evidence2 == "Fingerprints") and \
        (evidence1 == "Ghost orb" or evidence2 == "Ghost orb"):
        print("I think Phantom, Yurei, Revenant and Hantu, so one of them is the answer!!!.")
    elif (evidence1 == "Freezing Temperature" or evidence2 == "Freezing Temperature") and \
        (evidence1 == "Ghost orb" or evidence2 == "Ghost orb"):
        print("I think Wraith, Phantom, Yurei and Banshee, so one of them is the answer!!!.")
    else:
        findmore2(evidence1, evidence2)

def func():
    """Phasmophobian"""
    evidence1 = input()
    evidence2 = input()
    if (evidence1 == "Ghost Writing" or evidence2 == "Ghost Writing") and \
        (evidence1 == "Ghost orb" or evidence2 == "Ghost orb"):
        print("I think Yurei is the answer!!!.")
    elif (evidence1 == "Ghost Writing" or evidence2 == "Ghost Writing") and \
        (evidence1 == "Fingerprints" or evidence2 == "Fingerprints"):
        print("I think Revenant is the answer!!!.")
    elif (evidence1 == "Spirit box" or evidence2 == "Spirit box") and \
        (evidence1 == "Freezing Temperature" or evidence2 == "Freezing Temperature"):
        print("I think Wraith is the answer!!!.")
    elif (evidence1 == "Spirit box" or evidence2 == "Spirit box") and \
        (evidence1 == "Fingerprints" or evidence2 == "Fingerprints"):
        print("I think Hantu is the answer!!!.")
    elif (evidence1 == "Freezing Temperature" or evidence2 == "Freezing Temperature") and \
        (evidence1 == "EMF Level 5" or evidence2 == "EMF Level 5"):
        print("I think Banshee is the answer!!!.")
    elif (evidence1 == "EMF Level 5" or evidence2 == "EMF Level 5") and \
        (evidence1 == "Ghost orb" or evidence2 == "Ghost orb"):
        print("I think Phantom is the answer!!!.")
    else:
        findmore(evidence1, evidence2)
func()
