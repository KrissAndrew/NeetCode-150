import unittest
import xmlrunner

def run_tests():
    runner = xmlrunner.XMLTestRunner(output='test-results', verbosity=2)  # Set verbosity to 2 for detailed output
    tests = unittest.TestLoader().discover('Python_NeetCode_150', pattern='test_*.py')
    result = runner.run(tests)
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
