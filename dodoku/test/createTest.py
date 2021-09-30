from unittest import TestCase
import dodoku.create as create 
from _operator import truediv


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
    #        test 010: returns dictionary with keys
    #            result: ['grid', 'status', 'integrity']
    #        test 020: returns level 2
    #            result: grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-
    #                                6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-
    #                                9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-
    #                                1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0] 
    #        test 030: returns level 2
    #            result: status = ok 
    #        test 040: returns level 2
    #            result: value of integrity = 8 AND the value of integrity is a substring of
    #                        6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a
    #        test 050: returns level 1
    #            result:grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,
    #                                0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,
    #                                0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,
    #                                -5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1] 
    #                AND status = 'ok' AND the length of
    #                the value of integrity = 8 AND the value of integrity is a substring of
    #                    5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd
    #         test 060: returns level 3
    #            result:grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-
    #                                5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-
    #                                7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-
    #                                6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0] AND status = 'ok' AND the
    #                           length of the value of integrity = 8 AND the value of integrity is a substring of
    #                            eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9
    
    def test_Create_010_ThreeKeys(self):
        expectedResult = {'grid': '','status': '', 'integrity': ''}
        expectedResult = expectedResult.keys()
        parms = {'op': 'create', 'level' : '1'}
        actualResult = create._create(parms)
        actualResult = actualResult.keys()
        self.assertEqual(expectedResult, actualResult)
        
    def test_Create_020_Lvl2Grid(self):
        expectedResult = {}
        grid = [
            0,-6,0,0,0,0,0,-5,-9,
            -9,-3,0,-4,-8,0,0,0,0,
            0,0,0,0,0,-7,-3,0,0,
            0,-5,0,0,-1,0,0,-4,-6,
            0,0,0,0,0,-6,0,-9,0,
            0,-8,-1,-2,0,0,0,0,0,
            0,0,0,0,-7,0,0,0,0,
            0,0,0,0,-5,0,-8,0,-4,
            0,0,-1,0,0,0,-7,0,0,
            -6,0,-2,0,-9,0,0,0,0,
            0,0,0,0,-5,0,0,0,0,
            0,0,0,0,0,-9,-5,-3,0,
            0,-7,0,-4,0,0,0,0,0,
            -5,-8,0,0,-1,0,0,-9,0,
            0,0,-2,-1,0,0,0,0,0,
            0,0,0,0,-9,-8,0,-6,-1,
            -6,-1,0,0,0,0,0,-7,0
            ]
        status ='ok'
        integrity = '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create', 'level' : '2'}
        actualResult = create._create(parms)
        self.assertEqual(expectedResult['grid'], actualResult['grid'])
        
    def test_Create_030_Lvl2status(self):
        expectedResult = {}
        grid = [
            0,-6,0,0,0,0,0,-5,-9,
            -9,-3,0,-4,-8,0,0,0,0,
            0,0,0,0,0,-7,-3,0,0,
            0,-5,0,0,-1,0,0,-4,-6,
            0,0,0,0,0,-6,0,-9,0,
            0,-8,-1,-2,0,0,0,0,0,
            0,0,0,0,-7,0,0,0,0,
            0,0,0,0,-5,0,-8,0,-4,
            0,0,-1,0,0,0,-7,0,0,
            -6,0,-2,0,-9,0,0,0,0,
            0,0,0,0,-5,0,0,0,0,
            0,0,0,0,0,-9,-5,-3,0,
            0,-7,0,-4,0,0,0,0,0,
            -5,-8,0,0,-1,0,0,-9,0,
            0,0,-2,-1,0,0,0,0,0,
            0,0,0,0,-9,-8,0,-6,-1,
            -6,-1,0,0,0,0,0,-7,0
            ]
        status ='ok'
        integrity = '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create', 'level' : '2'}
        actualResult = create._create(parms)
        self.assertEqual(expectedResult['status'], actualResult['status'])
        
    def test_Create_040_Lvl2Integrity(self):
        expectedResult = {}
        grid = [
            0,-6,0,0,0,0,0,-5,-9,
            -9,-3,0,-4,-8,0,0,0,0,
            0,0,0,0,0,-7,-3,0,0,
            0,-5,0,0,-1,0,0,-4,-6,
            0,0,0,0,0,-6,0,-9,0,
            0,-8,-1,-2,0,0,0,0,0,
            0,0,0,0,-7,0,0,0,0,
            0,0,0,0,-5,0,-8,0,-4,
            0,0,-1,0,0,0,-7,0,0,
            -6,0,-2,0,-9,0,0,0,0,
            0,0,0,0,-5,0,0,0,0,
            0,0,0,0,0,-9,-5,-3,0,
            0,-7,0,-4,0,0,0,0,0,
            -5,-8,0,0,-1,0,0,-9,0,
            0,0,-2,-1,0,0,0,0,0,
            0,0,0,0,-9,-8,0,-6,-1,
            -6,-1,0,0,0,0,0,-7,0
            ]
        status ='ok'
        integrity = '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create', 'level' : '2'}
        actualResult = create._create(parms)
        expectedLength = 8
        self.assertEqual(len(actualResult['integrity']), expectedLength)
        self.assertIn(actualResult['integrity'], expectedResult['integrity'])
        
    def test_Create_050_Lvl1Total(self):
        expectedResult = {}
        grid = [
            0,-2,0,0,-1,0,0,-4,0,
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
            0,-6,0,0,-5,0,0,-3,-1
            ]
        status ='ok'
        integrity = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create', 'level' : '1'}
        actualResult = create._create(parms)
        expectedLength = 8
        self.assertEqual(len(actualResult['integrity']), expectedLength)
        self.assertEqual(expectedResult['grid'], actualResult['grid'])
        self.assertEqual(expectedResult['status'], actualResult['status'])
        self.assertIn(actualResult['integrity'], expectedResult['integrity'])
        
    def test_Create_060_Lvl3Total(self):
        expectedResult = {}
        grid = [
            0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,
            -5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,
            -7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,
            -6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0
            ]
        status ='ok'
        integrity = 'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create', 'level' : '3'}
        actualResult = create._create(parms)
        expectedLength = 8
        self.assertEqual(len(actualResult['integrity']), expectedLength)
        self.assertEqual(expectedResult['grid'], actualResult['grid'])
        self.assertEqual(expectedResult['status'], actualResult['status'])
        self.assertIn(actualResult['integrity'], expectedResult['integrity'])
        
    def test_Create_070_BlankLvlTotal(self):
        expectedResult = {}
        grid = [
            0,-2,0,0,-1,0,0,-4,0,
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
            0,-6,0,0,-5,0,0,-3,-1
            ]
        status ='ok'
        integrity = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create', 'level' : ''}
        actualResult = create._create(parms)
        expectedLength = 8
        self.assertEqual(len(actualResult['integrity']), expectedLength)
        self.assertEqual(expectedResult['grid'], actualResult['grid'])
        self.assertEqual(expectedResult['status'], actualResult['status'])
        self.assertIn(actualResult['integrity'], expectedResult['integrity'])
        
    def test_Create_080_MissingLvlTotal(self):
        expectedResult = {}
        grid = [
            0,-2,0,0,-1,0,0,-4,0,
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
            0,-6,0,0,-5,0,0,-3,-1
            ]
        status ='ok'
        integrity = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
        expectedResult["grid"] = grid
        expectedResult["status"] = status
        expectedResult["integrity"] = integrity
        parms = {'op': 'create'}
        actualResult = create._create(parms)
        expectedLength = 8
        self.assertEqual(len(actualResult['integrity']), expectedLength)
        self.assertEqual(expectedResult['grid'], actualResult['grid'])
        self.assertEqual(expectedResult['status'], actualResult['status'])
        self.assertIn(actualResult['integrity'], expectedResult['integrity'])
        