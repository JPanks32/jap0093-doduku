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
    def indexGrid(self):
        grid = [0]*153
        for i in range(0,153):
            grid[i] = i
        return grid
    
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
    
    def getBlocks(self):
        blocks = [[0,-2,0,-8,0,-1,0,0,0],
                          [0,-1,0,-9,0,0,0,-3,0],
                          [0,-4,0,0,0,-5,0,-1,0],
                          [0,-3,0,-5,0,-9,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [-4,0,-6,0,0,-7,-2,-8,0],
                          [-2,0,0,0,0,-6,0,-4,0],
                          [-6,0,0,0,0,-3,-5,-7,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,-1,-4,-2,0,0,0,0,-7],
                          [0,-6,0,-1,0,-9,0,0,-5],
                          [0,0,-6,-2,0,0,-7,0,-9],
                          [0,0,0,0,0,0,0,0,0],
                          [0,-9,0,-4,0,-8,0,0,0],
                          [0,-5,0,-4,0,0,0,-6,0],
                          [0,-9,0,-6,0,-3,0,-5,0],
                          [0,0,0,-9,0,0,0,-3,-1]]
        return blocks
    
    def getRows(self):
        rows = [[0, -2, 0, 0, -1, 0, 0, -4, 0],
                [-8, 0, -1, -9, 0, 0, 0, 0, -5],
                [0, 0, 0, 0, -3, 0, 0, -1, 0],
                [0, -3, 0, 0, 0, 0, -4, 0, -6],
                [-5, 0, -9, 0, 0, 0, 0, 0, -7],
                [0, 0, 0, 0, 0, 0, -2, -8, 0],
                [-2, 0, 0, -6, 0, 0, 0, 0, 0, 0, -1, -4, 0, -6, 0],
                [0, 0, -6, 0, 0, -3, 0, 0, 0, -2, 0, 0, -1, 0, -9],
                [0, -4, 0, -5, -7, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5],
                [0, 0, -6, 0, 0, 0, 0, -9, 0],
                [-2, 0, 0, 0, 0, 0, -4, 0, -8],
                [-7, 0, -9, 0, 0, 0, 0, 0, 0],
                [0, -5, 0, 0, -9, 0, 0, 0, 0],
                [-4, 0, 0, -6, 0, -3, -9, 0, 0],
                [0, -6, 0, 0, -5, 0, 0, -3, -1]]

        return rows
    
    def getCols(self):
        cols = [[0, -8, 0, 0, -5, 0, -2, 0, 0],
                [-2, 0, 0, -3, 0, 0, 0, 0, -4],
                [0, -1, 0, 0, -9, 0, 0, -6, 0],
                [0, -9, 0, 0, 0, 0, -6, 0, -5],
                [-1, 0, -3, 0, 0, 0, 0, 0, -7],
                [0, 0, 0, 0, 0, 0, 0, -3, 0],
                [0, 0, 0, -4, 0, -2, 0, 0, 0, 0, -2, -7, 0, -4, 0],
                [-4, 0, -1, 0, 0, -8, 0, 0, 0, 0, 0, 0, -5, 0, -6],
                [0, -5, 0, -6, -7, 0, 0, 0, 0, -6, 0, -9, 0, 0, 0],
                [0, -2, 0, 0, 0, 0, 0, -6, 0],
                [-1, 0, 0, 0, 0, 0, -9, 0, -5],
                [-4, 0, -7, 0, 0, 0, 0, -3, 0],
                [0, -1, 0, 0, -4, 0, 0, -9, 0],
                [-6, 0, 0, -9, 0, 0, 0, 0, -3],
                [0, -9, -5, 0, -8, 0, 0, 0, -1]]

        return cols
    #  Happy path tests
    #        test 010: check_integrity returns true
    #            result: true
    #   
    
    def test_Insert_010_CheckInput(self):
        expectedResult = True
        grid = self.getGrid()
        parms = {'value': '3', 'cell' : 'r7c9', 'grid': grid , 'integrity' : '93d46bcb'}
        actualResult = insert._check_input(parms)
        self.assertEqual(expectedResult, actualResult)
        
        
        
    def test_Insert_020_find_integrity(self):
        grid = self.getGrid()
        actualResult = insert._find_integrity(grid)
        self.assertIn('93d46bcb', actualResult)
        
    def test_Insert_030_find_location(self):
        loc = 'r11c7'
        actualResult = insert._find_location(loc)
        self.assertEqual([11,7], actualResult)
        
    def test_Insert_040_organize(self):
        grid = self.getGrid()
        blocks = self.getBlocks()
        cols = self.getCols()
        rows = self.getRows()
        actualBlocks, actualRows, actualCols = insert._organize(grid)
        self.assertEqual(blocks, actualBlocks)
        self.assertEqual(cols, actualCols)
        self.assertEqual(rows, actualRows)
        
    def test_Insert_050_index_location(self):
        grid = self.indexGrid()
        loc1 = 'r6c5'
        ind1 = 41
        loc2 = 'r8c11'
        ind2 = 79
        loc3 = 'r11c11'
        ind3 = 112
        loc4 = 'r7c10'
        ind4 = 99
        actualInd1 = insert._find_index(loc1)
        actualInd2 = insert._find_index(loc2)
        actualInd3 = insert._find_index(loc3)
        actualInd4 = insert._find_index(loc4)
        self.assertEqual(ind1, actualInd1)
        self.assertEqual(ind2, actualInd2)
        self.assertEqual(ind3, actualInd3)
        self.assertEqual(ind4, actualInd4)
