import unittest

import flaskr

class FlaskrTest(unittest.TestCase):

    def test_i_will_always_pass(self):
        self.assertTrue(True)


    def test_i_will_always_fail(self):
        self.assertTrue(False, "This test will always fail, dont panic!")


    def test_i_will_always_error(self):
        raise RuntimeError('Test error!')


    def test_there_are_a_number_of_assertions(self):

        assertTrue(True)
        #assertFalse(x, msg=None)
        #assertIsNone(x, msg=None)
        #assertIsNotNone(x, msg=None)
        #assertEqual(a, b, msg=None)
        #assertNotEqual(a, b, msg=None)
        #assertIs(a, b, msg=None)
        #assertIsNot(a, b, msg=None)
        #assertIn(a, b, msg=None)
        #assertNotIn(a, b, msg=None)
        #assertIsInstance(a, b, msg=None)
        #assertNotIsInstance(a, b, msg=None)

        # and loads more..

        #assertTrue(x, msg=None)
        #assertFalse(x, msg=None)
        #assertIsNone(x, msg=None)
        #assertIsNotNone(x, msg=None)
        #assertEqual(a, b, msg=None)
        #assertNotEqual(a, b, msg=None)
        #assertIs(a, b, msg=None)
        #assertIsNot(a, b, msg=None)
        #assertIn(a, b, msg=None)
        #assertNotIn(a, b, msg=None)
        #assertIsInstance(a, b, msg=None)
        #assertNotIsInstance(a, b, msg=None)


if __name__ == '__main__':
    
    unittest.main()
