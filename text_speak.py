import pygame as pg
pg.init()

dictionary = {
    'không': 'khong', 'một': 'mot1', 'bốn': 'bon', 'năm': 'nam',
    'sáu': 'sau', 'bảy': 'bay', 'tám': 'tam', 'chín': 'chin',
    'mười': 'muoi1', 'mươi': 'muoi2', 'lăm': 'lam', 'trăm': 'tram', 'mốt': 'mot2',
    'nghìn': 'nghin', 'ngàn': 'ngan', 'lẻ': 'le', 'triệu': 'trieu', 'tỷ': 'ty',
    'million,': 'million', 'billion,': 'million'
}


def speak_text(arr, address):
    """ This function will speak a input string
    Args:
        arr: a string
        address: a string
    Return:
        Sounds of the input string
    Raise:
        TypeError: if arr or address is not a string
    """
    if not isinstance(arr, str) or not isinstance(address, str):
        raise TypeError
    arr = arr.replace('-', ' ')
    arr = arr.split()
    for i in arr:
        for j in dictionary:
            if i == j:
                arr[arr.index(i)] = dictionary[j]
    for i in arr:
        link = address + i + '.ogg'
        print(address)
        sound = pg.mixer.Sound(link)
        sound.play()
        pg.time.wait(600)
        pg.mixer.stop()

