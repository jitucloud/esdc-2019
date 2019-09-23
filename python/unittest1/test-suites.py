from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
import test1
import test2

example_tests = TestLoader().loadTestsFromTestCase(test1.Test1)
example2_tests = TestLoader().loadTestsFromTestCase(test2.Test2)

suite = TestSuite([example_tests, example2_tests])

runner =    HTMLTestRunner(output='example_suite',combine_reports=True,report_name="MyReport",add_timestamp=True)

runner.run(suite)