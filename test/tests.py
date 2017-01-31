import os
import unittest
import json
import flaskr

class FlaskrTest(unittest.TestCase):

    def test_i_will_always_pass(self):
        self.assertTrue(True)


    #def test_i_will_always_fail(self):
    #    self.assertTrue(False, "This test will always fail, dont panic!")


    #def test_i_will_always_error(self):
    #    raise RuntimeError('Test error!')


    def test_there_are_a_number_of_assertions(self):

        self.assertTrue(True)
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



class FixturesTest(unittest.TestCase):


    def setUp(self):
       # print('In setUp()')
        self.fixture = range(1, 10)


    def tearDown(self):
        #print('In tearDown()')
        del self.fixture


    def test(self):
        #print('in test()')
        self.assertEqual(self.fixture, range(1, 10))



class FirewallRuleTest(unittest.TestCase):

    FIREWALL_CONFIG = os.path.join(os.path.dirname(__file__), '../fake_firewall_config.json')

    def setUp(self):

        print "-] Testing firewall rules for security compliance"

        with open(self.FIREWALL_CONFIG) as data_file:    
                self.firewalljson = json.load(data_file)


    def test_no_telnet(self):

        is_there_telnet = False

        for allow_rule in self.firewalljson["allow"]:
            if str(allow_rule).find("23") != -1:
                is_there_telnet = True    

        self.assertFalse(is_there_telnet, "TEST FAILED: telnet in use and is insecure")



if __name__ == '__main__':
    
    unittest.main()
