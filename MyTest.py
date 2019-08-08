import unittest
import cardinal_numeral



class MyTest(unittest.TestCase):
    def test_cardinal_numerals_eng(self):
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90,
                  100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000,
                  101, 1005, 10100, 100055, 1000011, 100056000, 100800000, 1008900000, 10452005600, 100068458904]
        ans = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
               'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
               'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one hundred',
               'one thousand', 'ten thousand', 'one hundred thousand', 'one million', 'ten million',
               'one hundred million', 'one billion', 'ten billion', 'one hundred billion', 'one hundred and one',
               'one thousand and five', 'ten thousand and one hundred', 'one hundred thousand and fifty-five',
               'one million and eleven', 'one hundred million, fifty-six thousand',
               'one hundred million, eight hundred thousand', 'one billion, eight million, nine hundred thousand',
               'ten billion, four hundred and fifty-two million, five thousand and six hundred',
               'one hundred billion, sixty-eight million, four hundred and fifty-eight thousand and nine hundred and four'
               ]
        for i in range(len(number)):
            self.assertEqual(cardinal_numeral.integer_to_english_numeral(activate_tts=False, n=number[i]), ans[i])

    def test_cardinal_numerals_vie_north(self):
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 21, 101, 105, 1001, 1031, 96, 405, 1915, 5061, 1002003,
                  1000000, 1030000, 1002003004, 1002000004, 100000004, 999999999999]
        ans = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười', 'mười một', 'mười lăm',
               'hai mươi mốt', 'một trăm linh một', 'một trăm linh năm', 'một nghìn không trăm linh một',
               'một nghìn không trăm ba mươi mốt', 'chín mươi sáu', 'bốn trăm linh năm', 'một nghìn chín trăm mười lăm',
               'năm nghìn không trăm sáu mươi mốt', 'một triệu không trăm linh hai nghìn không trăm linh ba',
               'một triệu', 'một triệu không trăm ba mươi nghìn',
               'một tỷ không trăm linh hai triệu không trăm linh ba nghìn không trăm linh bốn',
               'một tỷ không trăm linh hai triệu không trăm linh bốn', 'một trăm triệu không trăm linh bốn',
               'chín trăm chín mươi chín tỷ chín trăm chín mươi chín triệu chín trăm chín mươi chín nghìn chín trăm chín mươi chín']
        for i in range(len(number)):
            self.assertEqual(cardinal_numeral.integer_to_vietnamese_numeral(region='north', n=number[i], activate_tts=False), ans[i])

    def test_cardinal_numerals_vie_south(self):
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 21, 101, 105, 1001, 1031, 96, 405, 1915, 5061, 1002003,
                  1000000, 1030000, 1002003004, 1002000004, 100000004, 999999999999]
        ans = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười', 'mười một', 'mười lăm',
               'hai mươi mốt', 'một trăm lẻ một', 'một trăm lẻ năm', 'một ngàn không trăm lẻ một',
               'một ngàn không trăm ba mươi mốt', 'chín mươi sáu', 'bốn trăm lẻ năm', 'một ngàn chín trăm mười lăm',
               'năm ngàn không trăm sáu mươi mốt', 'một triệu không trăm lẻ hai ngàn không trăm lẻ ba',
               'một triệu', 'một triệu không trăm ba mươi ngàn',
               'một tỷ không trăm lẻ hai triệu không trăm lẻ ba ngàn không trăm lẻ bốn',
               'một tỷ không trăm lẻ hai triệu không trăm lẻ bốn', 'một trăm triệu không trăm lẻ bốn',
               'chín trăm chín mươi chín tỷ chín trăm chín mươi chín triệu chín trăm chín mươi chín ngàn chín trăm chín mươi chín']
        for i in range(len(number)):
            self.assertEqual(cardinal_numeral.integer_to_vietnamese_numeral(n=number[i],activate_tts=False, region='south' ), ans[i])

