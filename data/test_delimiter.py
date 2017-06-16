import unittest
import delimit

class DelimitTest(unittest.TestCase):
    """
    Delimit a file that is human readable with white spaces and no delimiter.
    """
    def test_find_delimiter_indexes(self):
        """
        Find the indexes of a delimiter in a line of data.
        """
        line = "AQW00061705,-14.3306,-170.7136,0003.7,AS,PAGO PAGO WSO AP              ,GSN,   ,91765"
        indexes = delimit.find_delimiter_indexes(line, delimiter=',')
        expected_indexes = [11, 20, 30, 37, 40, 71, 75, 79]
        self.assertEqual(expected_indexes, indexes)
    
    def test_learn_delimiter(self):
        """
        Find the only characters that have a space in every line.
        """
        lines = [
            'AQW00061705 -14.3306 -170.7136    3.7 AS PAGO PAGO WSO AP               GSN     91765',
            'RQC00660040  18.1469  -66.4919  598.9 PR ACEITUNA WATER TREATMENT PLANT              ',
            'USC00026353  31.9356 -109.8378 1325.9 AZ PEARCE - SUNSITES                  HCN      ',
            'USC00049185  37.7719 -122.1675  120.1 CA UPPER SAN LEANDRO FILTERS                   '
        ]
        indexes = delimit.learn_delimiter(lines, delimiter=' ')
        expected_indexes = [11, 20, 30, 37, 40, 71, 75, 79]
        self.assertEqual(expected_indexes, indexes)
        
    def test_delimit_indexes(self):
        """
        After learning the indexes of potential delimiters, mark those positions with the delimiter
        """
        lines = [
            'AQW00061705 -14.3306 -170.7136    3.7 AS PAGO PAGO WSO AP               GSN     91765',
            'RQC00660040  18.1469  -66.4919  598.9 PR ACEITUNA WATER TREATMENT PLANT              ',
            'USC00026353  31.9356 -109.8378 1325.9 AZ PEARCE - SUNSITES                  HCN      ',
            'USC00049185  37.7719 -122.1675  120.1 CA UPPER SAN LEANDRO FILTERS                   '
        ]
        expected_lines = [
            'AQW00061705,-14.3306,-170.7136,   3.7,AS,PAGO PAGO WSO AP              ,GSN,   ,91765',
            'RQC00660040, 18.1469, -66.4919, 598.9,PR,ACEITUNA WATER TREATMENT PLANT,   ,   ,     ',
            'USC00026353, 31.9356,-109.8378,1325.9,AZ,PEARCE - SUNSITES             ,   ,HCN,     ',
            'USC00049185, 37.7719,-122.1675, 120.1,CA,UPPER SAN LEANDRO FILTERS     ,   ,   ,     '
        ]
        indexes = delimit.learn_delimiter(lines, delimiter=' ')
        new_lines = delimit.delimit_indexes(lines, indexes, delimiter=',')
        self.assertEqual(new_lines, expected_lines)

