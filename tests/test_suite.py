import importlib.util
import pathlib
import unittest


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    tests_dir = pathlib.Path(__file__).parent

    for test_file in sorted(tests_dir.glob("*-test.py")):
        module_name = "tests.{}".format(test_file.stem.replace("-", "_"))
        spec = importlib.util.spec_from_file_location(module_name, test_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        suite.addTests(loader.loadTestsFromModule(module))

    return suite
