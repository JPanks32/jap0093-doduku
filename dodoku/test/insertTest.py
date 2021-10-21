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
    
    def getNewGrid(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,
                -8,0,-1,-9,0,0,0,0,-5,
                0,0,0,0,-3,0,0,-1,0,
                0,-3,0,0,0,0,-4,0,-6,
                -5,0,-9,0,0,0,0,0,-7,
                0,0,0,0,0,0,-2,-8,0,
                -2,0,0,-6,0,0,0,0,3,
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
    
    def getValidResult2(self):
        result = {'grid': [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,5,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1],'integrity': '2a2706879b00dc00937cea6d2f057b72bd1141ab09fd1b1e8a5c53f6fb6789db','status':'warning'}
        return result
    
    def getValidResult3(self):
        result = {'grid': [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1],'integrity': '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd','status':'ok'}
        return result
    
    def getParms1(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        parms={'value':'3', 'cell':'r7c9', 'grid': grid, 'integrity':'12345678'}
        return parms
    
    def getParms2(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        parms={'cell':'r7c9', 'grid': grid, 'integrity':'12345678'}
        return parms
    
    def getValidResult(self):
        result = {'grid': [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1],'integrity': '72a87aa0938dfb1b7edf4c31cd75bb0db75e916ff3f7ea9c1671cdd569cef463','status':'ok'}
        return result
    
    #  Happy path tests
    #        test 010: checks the validity of inputs
    #            result: True
    #        test 020: calculates the integrity
    #            result: 64 sha-256
    #        test 030: parses the cell into array that's easy to read
    #            result: [row, col, cell]
    #        test 040: organizes the grid into 3 2d arrays, sorted by row, column, and block
    #            result: 3 arrays
    #        test 050: calculates the index in the origional grid list of a cell
    #            result: int
    #        test 060: checks if it can insert, and if there would be a conflict
    #            result: int (1 for valid, -1 for conflict, -2 for error if trying to replace a hint)
    #        test 070: Actually changes the cell in grid
    #            result: grid
    #        test 080: Main function with a valid, nonconflicting value and location
    #            result: dict
    #        test 090: Main function with a valid but conflicting value and location
    #            result: dict
    #        test 100: Main function removing a cell
    #            result: dict
    #        
    
    def test_Insert_010_CheckInput(self):
        expectedResult = True
        grid = self.getGrid()
        parms = {'value': '3', 'cell' : 'r7c9', 'grid': grid , 'integrity' : 'bcb2ab5f'}
        actualResult = insert._check_input(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_Insert_020_find_integrity(self):
        grid = self.getGrid()
        actualResult = insert._find_integrity(grid)
        self.assertIn('93d46bcb', actualResult)
        
    def test_Insert_030_find_location(self):
        loc = 'r11c7'
        actualResult = insert._find_location(loc)
        self.assertEqual([11,7, 12], actualResult)
        
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
        ind1 = 49
        loc2 = 'r8c11'
        ind2 = 79
        loc3 = 'r11c11'
        ind3 = 112
        loc4 = 'r10c7'
        ind4 = 99
        actualInd1 = insert._find_index(loc1)
        actualInd2 = insert._find_index(loc2)
        actualInd3 = insert._find_index(loc3)
        actualInd4 = insert._find_index(loc4)
        self.assertEqual(ind1, actualInd1)
        self.assertEqual(ind2, actualInd2)
        self.assertEqual(ind3, actualInd3)
        self.assertEqual(ind4, actualInd4)
        
    def test_Insert_060_can_insert(self):
        grid = self.getGrid()
        loc = 'r7c9'
        val1 = 3
        val2 = 5
        loc2 = 'r1c2'
        loc3 = 'r12c13'
        ans1 = insert._can_insert(val1, loc, grid)
        ans2 = insert._can_insert(val2, loc, grid)
        ans3 = insert._can_insert(val2, loc2, grid)
        self.assertEquals(1, ans1)
        self.assertEquals(-1, ans2)
        self.assertEquals(-2, ans3)

    def test_Insert_070_change_val(self):
        grid = self.getGrid()
        val = 3
        loc = 'r7c9'
        expected_grid = self.getNewGrid()
        new_grid = insert._change_val(val, loc, grid)
        self.assertEquals(new_grid, expected_grid)
        
    def test_Insert_080_valid_insert(self):
        parms = self.getParms1()
        expected_result = self.getValidResult()
        expected_grid = expected_result['grid']
        expected_integrity = expected_result['integrity']
        expected_status = expected_result['status']
        actual_result = insert._insert(parms)
        actual_grid = actual_result['grid']
        actual_integrity = actual_result['integrity']
        actual_status = actual_result['status']
        self.assertEquals(expected_grid, actual_grid)
        self.assertIn(actual_integrity, expected_integrity)
        self.assertEquals(expected_status, actual_status)

    def test_Insert_090_warning_insert(self):
        parms = self.getParms1()
        parms['value'] = '5'
        expected_result = self.getValidResult2()
        expected_grid = expected_result['grid']
        expected_integrity = expected_result['integrity']
        expected_status = expected_result['status']
        actual_result = insert._insert(parms)
        actual_grid = actual_result['grid']
        actual_integrity = actual_result['integrity']
        actual_status = actual_result['status']
        self.assertEquals(expected_grid, actual_grid)
        self.assertIn(actual_integrity, expected_integrity)
        self.assertEquals(expected_status, actual_status)
    
    def test_Insert_100_remove(self):
        parms = self.getParms2()
        expected_result = self.getValidResult3()
        expected_grid = expected_result['grid']
        expected_integrity = expected_result['integrity']
        expected_status = expected_result['status']
        actual_result = insert._insert(parms)
        actual_grid = actual_result['grid']
        actual_integrity = actual_result['integrity']
        actual_status = actual_result['status']
        self.assertEquals(expected_grid, actual_grid)
        self.assertIn(actual_integrity, expected_integrity)
        self.assertEquals(expected_status, actual_status)

    #  Sad path tests 
    #        test 910: tests invalid cell reference
    #            result: error message
    #        test 920: non-integer string:  '1.1'
    #            result: error message
    #        test 930: lower bound of string:  '0'
    #            result: error message
    #        test 940: upper bound of string:  '4'
    #            result: error message
    
    
    def test100_910_invalid_cell(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        parms={'value':'3', 'cell':'r10c1', 'grid': grid, 'integrity':'12345678'}
        actualResult = insert._insert(parms)
        expectedResult = {'status':'error: invalid cell reference'}
        self.assertEqual(expectedResult, actualResult)
        
    def test100_920_missing_cell(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        parms={'value':'3', 'grid': grid, 'integrity':'12345678'}
        actualResult = insert._insert(parms)
        expectedResult = {'status':'error: missing cell reference'}
        self.assertEqual(expectedResult, actualResult) 
        
    def test100_930_invalid_value(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        parms={'value':'a', 'cell':'r7c9', 'grid': grid, 'integrity':'12345678'}
        actualResult = insert._insert(parms)
        expectedResult = {'status':'error: invalid value'}
        self.assertEqual(expectedResult, actualResult) 
    
    def test100_940_target_hint(self):
        grid = '[0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]'
        parms={'value':'1', 'cell':'r1c2', 'grid': grid, 'integrity':'12345678'}
        actualResult = insert._insert(parms)
        expectedResult = {'status':'error: attempt to change fixed hint'}
        self.assertEqual(expectedResult, actualResult) 



         