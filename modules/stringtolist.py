# String to list attempts to make string manipulation more advanced by converting
# Raw text into a list/array of chars as C++ does by default.

# created by Shotaro Ikeda
# Date Janurary 29, 2015
# version 1.0

# Usage instructions in test()

class StringList(object):
    """Class to convert a string into a list or vice versa."""

    def convert(self, words):
        """
        Either takes a list, and returns a string or takes a string and returns
        a list
        """
        if type(words) == str:
            a_list = []
            for char in words:
                a_list.append(char)

            return a_list
        elif type(words) == list:
            returnstring = None
            for char in words:
                if returnstring == None:
                    returnstring = char
                else:
                    returnstring += char

            return returnstring

def test():

    a = 'Hi, my name is Shotaro'
    b = ['A', 'y', 'y', 'y', 'Y', ' ', 'l', 'M', 'a', 'o']
    makelist = StringList()

    # Coverts 'Hi name is Shotaro', then removes the 's' in 'is'
    mssg_list = makelist.convert(a)
    mssg_list.remove('s')
    # Reconverts it to a string
    print makelist.convert(mssg_list)

    # Takes the list b and converts it to a string. Then changes it to lower case
    # and returns it once more as a list
    aylmao = makelist.convert(b)
    print makelist.convert(aylmao.lower())


if __name__ == '__main__':
    test()
