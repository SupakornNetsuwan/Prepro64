"""Func prepro"""

def func():
    """max it"""
    inp1 = float(input())
    inp2 = float(input())
    inp3 = float(input())
    inp4 = float(input())
    inp5 = float(input())
    inp6 = float(input())
    inp7 = float(input())
    inp8 = float(input())
    tot = sum((inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8))
    find = min(tot-inp1, tot-inp2, tot-inp3, tot-inp4, tot-inp5, tot-inp6, tot-inp7, tot-inp8)
    print("%.2f" %(tot - find))
func()
