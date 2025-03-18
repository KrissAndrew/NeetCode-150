import unittest

def run_tests():
    runner = unittest.TextTestRunner(verbosity=1)  # Use TextTestRunner for console output
    tests = unittest.TestLoader().discover('Python_NeetCode_150', pattern='test_*.py')
    result = runner.run(tests)
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
