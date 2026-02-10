import unittest

from boggle_solver import Boggle

class Test_Boggle_Solver(unittest.TestCase):

  #Testing a normal case
  def test_1(self):
    grid = [["C", "A", "T"], ["R", "R", "E"]]
    dictionary = ["CAT", "CAR", "TREE"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertIn("cat", solver.solutions)
    self.assertIn("car", solver.solutions)

  #Testing no letter reuse
  def test_2(self):
    grid = [["A", "A"]]
    dictionary = ["AAA"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertNotIn("aaa", solver.solutions)

  #Testing an empty dictionary
  def test_3(self):
    grid = [["A", "B"], ["C", "D"]]
    dictionary = []
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertEqual(solver.solutions, [])

  #Testing an empty grid
  def test_4(self):
    grid = []
    dictionary = ["A"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertEqual(solver.solutions, [])
  
  #Testing a single cell grid
  def test_5(self):
    grid = [["A"]]
    dictionary = ["A", "AA", "AAA"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertEqual(solver.solutions, [])

  
  #Testing a larger grid
  def test_6(self):
    grid = [["T", "E", "S", "T"],
           ["W", "O", "R", "D"]]
    dictionary = ["TEST", "WORD"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertIn("test", solver.solutions)
    self.assertIn("word", solver.solutions)
  
  #Testing the prefix as a single tile/ diagonal movement
  def test_qu_single_tile(self):
    grid = [["QU", "I", "T"],
           ["A", "E", "S"],
            ["R", "L", "N"]]
    dictionary = ["QUIT", "QUITE"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertIn("quit", solver.solutions)

  #Testing overlapping words
  def test_8(self):
    grid = [["C", "A", "R"],
          ["A", "T", "S"]]
    dictionary = ["CAR", "CATS", "CAT"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertIn("car", solver.solutions)
    self.assertIn("cat", solver.solutions)
  
  #Testing words longer than the NxN matrix
  def test_9(self):
    grid = [["A", "B"],
           ["C", "D"]]
    dictionary = ["ABCDE"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertNotIn("abcde", solver.solutions)


  #Testing duplicate dictionaries 
  def test_10(self):
    grid = [["D", "O", "G"]]
    dictionary = ["DOG", "DOG", "DOG"]
    solver = Boggle(grid, dictionary)
    solver.solutions = solver.getSolution()
    self.assertIn("dog", solver.solutions)
    self.assertEqual(len(solver.solutions), 1)
  
if __name__ == '__main__':
  unittest.main()

