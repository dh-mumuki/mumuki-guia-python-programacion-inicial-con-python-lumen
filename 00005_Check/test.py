class TestFixtures(unittest.TestCase):
  def test_True(self):
    self.assertTrue(estar(5,[1, 5, 8, 3]))

  def test_False(self):
    self.assertEqual(estar(2, [1, 5, 8, 3]), [1, 5, 8, 3, 2])
    
