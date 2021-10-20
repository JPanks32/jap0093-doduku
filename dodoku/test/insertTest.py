from unittest import TestCase
import dodoku.insert as insert 

class InsertTest(TestCase):
            # 100 Insert
    #    Desired level of confidence:    grid value insertion
    #    Input-output Analysis
    #      inputs: dictionary with "cell", "value", "grid", and "integrity"; .GE. 0 and .LT. 100; mandatory, unvalidated
    #      outputs: 
    #         normal:  dictionary with "grid", "integrity", and "status"
    #         abnormal: error
    #         side effects:  none
    
    #  Happy path tests
    #        test 010: check_integrity returns true
    #            result: true
    #   
    def getGrid(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,
                -8,0,-1,-9,0,0,0,0,-5,
                0,0,0,0,-3,0,0,-1,0,
                0,-3,0,0,0,0,-4,0,-6,
                -5,0,-9,0,0,0,0,0,-7,
                0,0,0,0,0,0,-2,-8,0,
                -2,0,0,-6,0,0,0,0,0,
                0,-1,-4,0,-6,0,0,0,-6,
                0,0,-3,0,0,0,-2,0,0,
                -1,0,-9,0,-4,0,-5,-7,0,
                0,0,0,0,0,-7,0,0,-5,
                0,0,-6,0,0,0,0,-9,0,
                -2,0,0,0,0,0,-4,0,-8,
                -7,0,-9,0,0,0,0,0,0,
                0,-5,0,0,-9,0,0,0,0,
                -4,0,0,-6,0,-3,-9,0,0,
                0,-6,0,0,-5,0,0,-3,-1]
        return grid
    def test_CheckInput(self):
        expectedResult = True
        grid = self.getGrid()
        parms = {'value': '3', 'cell' : 'r7c9', 'grid': grid , 'integrity' : '93d46bcb'}
        actualResult = insert._check_input(parms)
        self.assertEqual(expectedResult, actualResult)
        
        
        
    def test_find_integrity(self):
        grid = self.getGrid()
        actualResult = insert._find_integrity(grid)
        print(actualResult)
        self.assertIn('93d46bcb', actualResult)