import unittest, json
from libs import consts
from libs.server_utils import create_response_message
from libs.client_utils import create_presence_message, read_presence_message
from libs.errors import ToLongUserName, NoActionCode, WrongResponseCodeLength, WrongResponseCode
from libs.jim_utils import send_message

class TestServerCreateResponse(unittest.TestCase):
    def test_action_time(self):
        self.assertEqual(create_response_message({
            consts.ACTION: consts.PRESENCE,
            consts.TIME: 0.2,
            consts.USER: {'account_name': 'Jhon'}}),
            {consts.RESPONSE: 200})
    def test_time_type(self):
        with self.assertRaises(TypeError):
            create_response_message({
                consts.ACTION: consts.PRESENCE,
                consts.TIME: 22,
                consts.USER: {'account_name': 'Jhon'}})
    def test_action_tipe(self):
        self.assertEqual(create_response_message({
                consts.ACTION: consts.RESPONSE,
                consts.TIME: 222,
                consts.USER: {'account_name': 'Jhon'}}),
            {consts.RESPONSE: 400, consts.ERROR: 'Не верный запрос'})

class TestClientCreatePresence(unittest.TestCase):
    def test_account_type(self):
        with self.assertRaises(TypeError):
            create_presence_message(235)

    def test_account_length(self):
        with self.assertRaises(ToLongUserName):
            create_presence_message('jhuiiuhygiyggigy7gg8gi76gg6itgg6ytgyk')

class TestClientReadPresence(unittest.TestCase):
    def test_response_in_message(self):
        with self.assertRaises(NoActionCode):
            read_presence_message({})

    def test_response_code_length(self):
        with self.assertRaises(WrongResponseCodeLength):
            read_presence_message({consts.RESPONSE: 2022})

    def test_response_code_valid(self):
        with self.assertRaises(WrongResponseCode):
            read_presence_message({consts.RESPONSE: 343})

class TestJIMUtils(unittest.TestCase):
    message = ''
    socket = 'socket'

    def setUp(self):
        self.message = json.dumps({consts.RESPONSE: 343}).encode(consts.ENCODING)

    def test_send_message(self):
        with self.assertRaises(TypeError):
            send_message(self.socket, 'kjhgf')


if __name__ == '__main__':
    unittest.main()