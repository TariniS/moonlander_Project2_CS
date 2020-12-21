#Name: Tarini Srikanth
#Instructor: Turner
#Project 2- Functions test, non-IO
import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
       #testing the standard number
       self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
       
   def test_update_acc2(self):
       #testing a different value
       self.assertAlmostEqual(updateAcceleration(8.4,9),6.72)
       
   def test_update_alt1(self):
       #testing the altitude using the 1300 and -1.62
       self.assertAlmostEqual(updateAltitude(1300,0,-1.62),1299.19)
       
   def test_update_al2(self):
       #using a different velocity value, as well as a negative altitude
       self.assertAlmostEqual(updateAltitude(-9,1.3,5),3.8)
       
   def test_update_vel1(self):
       #testing updating the velocity
       self.assertAlmostEqual(updateVelocity(8,9),17)
       
   def test_update_vel2(self):
       #testing with a negative value
       self.assertAlmostEqual(updateVelocity(-1.5,9),7.5)
       
   def test_update_feul1(self):
       #testing with diferent values of fuel rate
       self.assertAlmostEqual(updateFuel(8.7,1.5),7.2)
       
   def test_update_fuel2(self):
       self.assertAlmostEqual(updateFuel(7.6,1.2),6.4)


      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

