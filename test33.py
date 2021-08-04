"""Func"""

def func():
    """Func"""
    def length(dist):
        """Find each distance"""
        convert = int(dist.replace("k", "000").replace(" ", "").replace("m", ""))
        print(dist)
        print("= %.3f kueb" %float((convert * 100)/25))
        print("= %.3f sok" %float((convert * 100)/50))
        print("= %.3f wa" %float(convert/2))
        print("= %.3f sen" %float(convert/40))
        print("= %.3f yot\n" %float((convert/1000)/16))

    length("200 m")
    length("500 m")
    length("1 km")
    length("2 km")
    length("5 km")
func()
