from django.test import TestCase

# Create your tests here.
from cipher.libraries.cipher import cipher

class CipherTests(TestCase):
    """These functions test that the cipher custom module functions correctly."""

    def test_shifts_lower_case_letters(self):
        test = cipher('abc')
        self.assertEquals(test, 'def')

    def test_shifts_upper_case_letters(self):
        test = cipher('ABC')
        self.assertEquals(test, 'DEF')

    def test_shifts_mixed_letters(self):
        test = cipher('AbC')
        self.assertEquals(test, 'DeF')

    def test_shifts_over_end(self):
        test = cipher('Xyz')
        self.assertEquals(test, 'Abc')

    def test_doesnt_change_spaces(self):
        test= cipher('Abc Xyz')
        self.assertEquals(test, 'Def Abc')

    def test_doesnt_change_numbers(self):
        test = cipher('Abc123 Xyz456')
        self.assertEquals(test, 'Def123 Abc456')

    def test_works_with_small_positive_offset(self):
        test=cipher('Abc Xyz', 1)
        self.assertEquals(test, 'Bcd Yza')

    def test_works_with_big_positive_offset(self):
        test = cipher('Abc Xyz', 50)
        self.assertEquals(test, 'Yza Vwx')