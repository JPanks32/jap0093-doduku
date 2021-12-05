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
    
    def getGridString1(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        return grid
    
    def getGridString2(self):
        grid = '[0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        return grid
    
    def getGridString3(self):
        grid = '[0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        return grid
    
    def getGridString4(self):
        grid = '[0,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'        
        return grid
    
    def getGridString5(self):
        grid = '[a,-2,5,7,-1,6,9,-4,3,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        return grid
    
    #  Happy path tests
    #        test 010: checks the validity of inputs
    #            result: True
    #        test 020: calculates the valid entries
    #            result: [2,3,5,7,8]
    
    def test_Recomend_010_CheckInput(self):
        expectedResult = True
        grid = self.getGrid()
        parms = { 'cell' : 'r7c9', 'grid': grid , 'integrity' : '2ab5f3e8'}
        actualResult = recommend._validateParms(parms)
        self.assertEqual(expectedResult, actualResult)
    
    def test_Recomend_020_ValidEntries(self):
        expectedResult = [3,8]
        grid = self.getGrid()
        parms = { 'cell' : 'r7c9', 'grid': grid , 'integrity' : '2ab5f3e8'}
        actualResult = recommend._identifyValues(parms['cell'], parms['grid'])
        self.assertEqual(expectedResult, actualResult)

    def test_Recomend_030_ValidInput(self):
        expectedResult = {'recommendation' : [3,8], 'status' : 'ok'}
        grid = self.getGridString1()
        parms = { 'cell' : 'r7c9', 'grid': grid , 'integrity' : '2ab5f3e8'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_Recomend_040_ValidInputr1c1(self):
        expectedResult = {'recommendation' : [], 'status' : 'ok'}
        grid = self.getGridString2()
        parms = { 'cell' : 'r1c1', 'grid': grid , 'integrity' : '2a505998'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
    
    def test_Recomend_050_ValidInputReservedSpotr1c2(self):
        expectedResult = {'recommendation' : [], 'status' : 'ok'}
        grid = self.getGridString3()
        parms = { 'cell' : 'r1c2', 'grid': grid , 'integrity' : 'c0522556'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
    
    def test_Recomend_060_ValidInputReservedSpotr1c3(self):
        expectedResult = {'recommendation' : [5], 'status' : 'ok'}
        grid = self.getGridString4()
        parms = { 'cell' : 'r1c3', 'grid': grid , 'integrity' : '47bc7544'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
        
        
        
         #  Sad path tests 
    #        test 910: tests invalid cell reference
    #            result: error message
    #        test 920: tests Missing cell reference
    #            result: error message
    #        test 930: tests invalid grid
    #            result: error message
    #        test 940: tests invalid integrity
    #            result: error message

    
    
    
    def test_Recomend_910_OutOfBounds(self):
        expectedResult = {'status':'error: invalid cell reference'}
        grid = self.getGridString4()
        parms = { 'cell' : 'r1c10', 'grid': grid , 'integrity' : '47bc7544'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_Recomend_920_MissingCell(self):
        expectedResult = {'status':'error: missing cell reference'}
        grid = self.getGridString4()
        parms = {'grid': grid , 'integrity' : '47bc7544'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_Recomend_930_InvalidGrid(self):
        expectedResult = {'status':'error: invalid grid'}
        grid = self.getGridString5()
        parms = { 'cell' : 'r1c1', 'grid': grid , 'integrity' : '47bc7544'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_Recomend_940_BadIntegrity(self):
        expectedResult = {'status':'error: integrity mismatch'}
        grid = self.getGridString4()
        parms = { 'cell' : 'r1c2', 'grid': grid , 'integrity' : '1234abcd'}
        actualResult = recommend._recommend(parms)
        self.assertEqual(expectedResult, actualResult)
        pass
