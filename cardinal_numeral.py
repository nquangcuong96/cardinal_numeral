import cardinal_numerals_eng
import cardinal_numerals_vie


def integer_to_vietnamese_numeral(n, region='north', activate_tts=False):
    """ This function will cover a number to string of vietnamese name base on region we choose.
        And will speak this string if we set
            Args:
                n: the integer number which greater than 0 and smaller than 999999999999
                region: a string which be set default is 'north', and only accept value 'north' or 'south'
                activate_tts: a boolean, which is True of False. And the default is False
            Return:
                A string of vietnamese name of a number base on region we choose
                Speak this string if activate_tts is True
            Raise:
                TypeError: if n is not a integer or boolean is not a boolean
                ValueError: if n is smaller than 0 or greater than 999999999999.
                            Or value of region is not 'north' or 'south'
        """
    if region is None:
        strings = 'north'
    elif not isinstance(region, str):
        raise TypeError('Argument "region" is not a string')
    if activate_tts is None:
        activate_tts = False
    elif not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if region != 'north' and region != 'south':
        raise ValueError('Argument "region" has not a correct value')
    if n < 0:
        raise ValueError('Not a positive integer')
    if n > 999999999999:
        raise OverflowError('Integer greater than 999,999,999,999')
    return cardinal_numerals_vie.integer_to_vietnamese(n, region, activate_tts)


def integer_to_english_numeral(n, activate_tts=False):
    """ This function will cover a number to string of english name. And will speak this string if we set
        Args:
            n: the integer number which greater than 0 and smaller than 999999999999
            activate_tts: a boolean, which is True of False. And the default is False
        Return:
            A string of english name of a number
            Speak this string if activate_tts is True
        Raise:
            TypeError: if n is not a integer or activate_tts is not a boolean
            ValueError: if n is smaller than 0 or greater than 999999999999
    """
    if activate_tts is None:
        activate_tts = False
    elif not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n < 0:
        raise ValueError('Not a positive integer')
    if n > 999999999999:
        raise OverflowError('Integer greater than 999,999,999,999')
    return cardinal_numerals_eng.integer_to_english(n, activate_tts)
