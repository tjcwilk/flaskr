import os
import unittest
import json
import flaskr

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
