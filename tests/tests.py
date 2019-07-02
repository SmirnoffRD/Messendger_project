import unittest
from libs import consts
from libs.server_utils import create_response_message
from libs.client_utils import create_presence_message, read_presence_message

class TestServerCreateResponse(unittest.TestCase):
    def test_action_time(self):
        self.assertEqual(create_response_message({
            consts.ACTION: consts.PRESENCE,
            consts.TIME: 0.2,
            consts.USER: {'account_name': 'Jhon'}}),
            {consts.RESPONSE: 200})
    def test_time_type(self):
        self.assertRaises(TypeError, create_response_message({
            consts.ACTION: consts.PRESENCE,
            consts.TIME: 2,
            consts.USER: {'account_name': 'Jhon'}}),
            {consts.RESPONSE: 200})

class TestClientCreatePresence(unittest.TestCase):
    pass

class TestClientReadPresence(unittest.TestCase):
    pass





if __name__ == '__main__':
    unittest.main()