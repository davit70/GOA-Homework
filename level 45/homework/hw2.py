from solution import duplicate_elements
import codewars_test as test

@test.describe("Sample Tests")
def sample_tests():
    @test.it("Should handle duplicates")
    def _():
        test.assert_equals(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True)
        test.assert_equals(duplicate_elements([9, 8, 7], [8, 1, 3]), True)
        test.assert_equals(duplicate_elements([-2, -4, -6, -8], [-2, -3, -5, -7]), True)
        test.assert_equals(duplicate_elements([-9, -8, -7], [-8, -1, -3]), True)

    @test.it("Should handle no duplicates")
    def _():
        test.assert_equals(duplicate_elements([1, 3, 5, 7, 9], [2, 4, 6, 8]), False)
        test.assert_equals(duplicate_elements([9, 8, 7], [6, 5, 4]), False)

    @test.it("Should handle empty lists")
    def _():
        test.assert_equals(duplicate_elements([], [9, 8, 7, 6, 5]), False)
        test.assert_equals(duplicate_elements([9, 8, 7, 6, 5], []), False)
        test.assert_equals(duplicate_elements([], []), False)


def duplicate_elements(m, n):
    res = False
    
    for i in m:
        if i in n:
            res = True
            
    return res