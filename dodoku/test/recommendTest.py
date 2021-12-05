from unittest import TestCase
import dodoku.recommend as recommend 
import dodoku.insert as insert 

class RecommendTest(TestCase):
                    # 100 Recomend
    #    Desired level of confidence:    grid value insertion
    #    Input-output Analysis
    #      inputs: dictionary with "cell", "value", "grid", and "integrity"; .GE. 0 and .LT. 100; mandatory, unvalidated
    #      outputs: 
    #         normal:  dictionary with "grid", "integrity", and "status"
    #         abnormal: error
    #         side effects:  none
    
    def getGrid(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-
                6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-
                6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
        return grid
    
    
    
    #  Happy path tests
    #        test 010: checks the validity of inputs
    #            result: True
    
    def test_Recomend_010_CheckInput(self):
        expectedResult = True
        grid = self.getGrid()
        parms = { 'cell' : 'r7c9', 'grid': grid , 'integrity' : '2ab5f3e8'}
        actualResult = recommend._validateParms(parms)
        self.assertEqual(expectedResult, actualResult)
        
        pass
