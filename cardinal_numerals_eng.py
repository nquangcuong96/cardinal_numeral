import text_speak

number_dictionary = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'
}
replace_dictionary = {
    'onety-one': 'eleven', 'onety-two': 'twelve', 'onety-three': 'thirteen', 'onety-four': 'fourteen',
    'onety-five': 'fifteen', 'onety-six': 'sixteen', 'onety-seven': 'seventeen', 'onety-eight': 'eighteen',
    'onety-nine': 'nineteen', 'onety': 'ten',
    'twoty': 'twenty', 'fourty': 'forty', 'threety': 'thirty', 'fivety': 'fifty', 'eightty': 'eighty'
}
local_part_name = {
    3: ' hundred', 2: 'ty'
}
glo_part_name = {
    4: ' billion', 3: ' million', 2: ' thousand'
}


def integer_to_english(n, tts):
    address = './sounds/eng/'
    ans = ''
    lst = []
    x = 0
    # if number is zero, return zero
    if n == 0:
        # check if we need to speak to text or not
        if tts:
            text_speak.speak_text(number_dictionary[n], address)
        return number_dictionary[n]
    # divide number to parts, each part have up to three digit
    while n != 0:
        lst.append(n % 1000)
        n = n // 1000
    lst = list(reversed(lst))
    # this variable to check the locate of current part
    locate_element = 0
    # we work on each part
    for element in lst:
        y = 0
        # this variable to check the locate of current digit of each part
        locate_char = 0
        # if value of part is zero, we skip each
        if element == 0:
            if len(lst) - x == 2:
                locate_element = len(lst) - x
            x += 1
            continue
        # add some char to accept the rule
        if locate_element in [4, 3]:
            ans += ', '
        elif locate_element == 2:
            ans += ' and '
        # we work on each digit of each part
        for char in str(element):
            # skip if value of digit is zero
            if char == '0':
                y += 1
                continue
            # add some char to accept the rule
            if locate_char == 3:
                ans += ' and '
            elif locate_char == 2:
                ans += '-'
            # check dictionary to cover a digit to string name
            for value in number_dictionary:
                if char == str(value):
                    ans += number_dictionary[value]
            # update the current located of digit
            locate_char = len(str(element)) - y
            # add local_part_name after each digit base on it locates
            for value in local_part_name:
                if locate_char == value:
                    ans += local_part_name[value]
            y += 1
        # update the current located of part
        locate_element = len(lst) - x
        # add glo_pat_name after each part base on it locates
        for value in glo_part_name:
            if locate_element == value:
                ans += glo_part_name[value]
        x += 1
    # replace some name to special name to accept the rule
    for value in replace_dictionary:
        ans = ans.replace(value, replace_dictionary[value])
    # check if we need to speak to text or not
    if tts:
        text_speak.speak_text(ans, address)

    return ans



