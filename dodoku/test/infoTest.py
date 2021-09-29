
import unittest
import dodoku.info as info

class InfoTest(unittest.TestCase):


    def test_Info_010_ShouldReturnMyUsername(self):
        expectedResult = {'info': 'jap0093'}
        parms = {'op': 'info'}
        actualResult = info._info(parms)
        self.assertDictEqual(expectedResult, actualResult)

