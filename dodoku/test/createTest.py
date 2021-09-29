from unittest import TestCase
import dodoku.create as create 


class CreateTest(TestCase):

    # 100 create
    #    Desired level of confidence:    grid creation
    #    Input-output Analysis
    #      inputs: value -> numeric; .GE. 0 and .LT. 100; mandatory, unvalidated
    #      outputs: 
    #         normal:  dictionary with "grid", "integrity", and "status"
    #         abnormal: error
    #         side effects:  none
    
    
    #  Happy path tests
    #        test 010: nominal value that has one digit:  '9'
    #            result: '9'
    #        
    
    
    def test100_010_CreateWithThreeParams(self):
        expectedResult = {'grid','status', 'integrity'}.keys()
        parms = {'op': 'create', 'level' : '1'}
        actualResult = create._create(parms).keys()
        self.assertDictEqual(expectedResult, actualResult)

        