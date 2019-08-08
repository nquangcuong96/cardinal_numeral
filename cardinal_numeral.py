import cardinal_numerals_eng
import cardinal_numerals_vie


def integer_to_vietnamese_numeral(number, strings='north', boolean=False):
    """ This function will cover a number to string of vietnamese name base on region we choose.
        And will speak this string if we set
            Args:
                number: the integer number which greater than 0 and smaller than 999999999999
                strings: a string which be set default is 'north', and only accept value 'north' or 'south'
                boolean: a boolean, which is True of False. And the default is False
            Return:
                A string of vietnamese name of a number base on region we choose
                Speak this string if boolean is True
            Raise:
                TypeError: if number is not a integer or boolean is not a boolean
                ValueError: if number is smaller than 0 or greater than 999999999999.
                            Or value of strings is not 'north' or 'south'
        """
    if not isinstance(number, int) or not isinstance(strings, str) or not isinstance(boolean, bool):
        raise TypeError
    if strings != 'north' and strings != 'south':
        raise ValueError
    if number < 0 or number > 999999999999:
        raise ValueError
    return cardinal_numerals_vie.integer_to_vietnamese(number, strings, boolean)


def integer_to_english_numeral(number, boolean=False):
    """ This function will cover a number to string of english name. And will speak this string if we set
        Args:
            number: the integer number which greater than 0 and smaller than 999999999999
            boolean: a boolean, which is True of False. And the default is False
        Return:
            A string of english name of a number
            Speak this string if boolean is True
        Raise:
            TypeError: if number is not a integer or boolean is not a boolean
            ValueError: if number is smaller than 0 or greater than 999999999999
    """
    if not isinstance(number, int) or not isinstance(boolean, bool):
        raise TypeError
    if number < 0 or number > 999999999999:
        raise ValueError
    return cardinal_numerals_eng.integer_to_english(number, boolean)
