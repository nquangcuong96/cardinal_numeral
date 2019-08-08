import text_speak

number_dictionary = {
    0: ' không', 1: ' một', 2: ' hai', 3: ' ba', 4: ' bốn', 5: ' năm', 6: ' sáu',
    7: ' bảy', 8: ' tám', 9: ' chín'
}
glo_part_name = {
    2: ' nghìn', 3: ' triệu', 4: ' tỷ'
}
local_part_name = {
    3: ' trăm', 2: ' mươi'
}
replace_dictionary = {
    'một mươi': 'mười', 'mươi một': 'mươi mốt', 'mươi năm': 'mươi lăm', 'mười năm': 'mười lăm'
}


def integer_to_vietnamese(n, region, tts):
    address = './sounds/vie/' + region + '/'
    ans = ''
    lst = []
    x = 0
    # if number is zero, return zero
    if n == 0:
        # check if we need to speak to text or not
        if tts:
            text_speak.speak_text(number_dictionary[n], address)
        return number_dictionary[n].strip()
    # divide number to parts, each part have up to three digit
    while n != 0:
        lst.append(n % 1000)
        n = n // 1000
    lst = list(reversed(lst))
    # this variable to check the locate of current part
    locate_element = 0
    # we work on each part
    for element in lst:
        # if value of part is zero, we skip each
        if element == 0:
            x += 1
            continue
        y = 0
        add = False
        # change type of each part
        element = str(element)
        # except first part, cover value of others to 3 digits
        if locate_element != 0:
            element = '0' * (3 - len(element)) + element
        # we work on each digit of each part
        for char in element:
            # skip if value of digit is zero, except first digit
            if len(element) - y in [2, 1] and char == '0':
                add = True
                y += 1
                continue
            # add some char to accept the rule
            if add:
                ans += ' linh'
            # check dictionary to cover a digit to string name
            for value in number_dictionary:
                if char == str(value):
                    ans += number_dictionary[value]
            # update the current located of digit
            locate_char = len(element) - y
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
    # replace some name to special name to accept the rule if region is change
    if region == 'south':
        ans = ans.replace('linh', 'lẻ')
        ans = ans.replace('nghìn', 'ngàn')
    # check if we need to speak to text or not
    if tts:
        text_speak.speak_text(ans, address)

    return (' '.join(ans.split())).strip()
