"""Func"""

def main():
    """Sign maker"""
    name1 = input()
    name2 = input()
    name3 = input()

    def sign(name):
        """Print name"""
        print("************\
            \n* Fighting *\
            \n* %8.8s *\
            \n************\
            \n     ||\
            \n     ||\
            \n     ||\
            "%(name))

    sign(name1)
    sign(name2)
    sign(name3)
main()
