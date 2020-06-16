import unittest
import re
import os
import argparse
import pkgutil


def get_method_name(file_name):
    method_name = re.sub(r'^\d+_', '', file_name)
    return re.sub(r'_[a-zA-Z]', lambda x: x.group()[1:].upper(), method_name)


def load_module(file_name, module_name=None):
    r = None

    dir = os.path.realpath(os.path.join('leetcode', module_name))
    for file_path, name, _ in pkgutil.iter_modules([dir]):
        if name.startswith(file_name):
            r = file_path
            file_name = name
            break

    if r is None:
        raise Exception('Please check file')

    module = r.find_module(file_name)
    return module.load_module(), file_name


def execute_from_command_line(name, module_name=None):
    module, file_name = load_module(name, module_name=module_name)

    if getattr(module, 'Solution', None):
        s = module.Solution()
        method_name = get_method_name(file_name)
        method = getattr(s, method_name, None)
        assert method is not None, f'Please check method {method_name}'

        for inputs, expectation in module.EXAMPLES:
            if isinstance(inputs, tuple):
                r = method(*inputs)
            else:
                r = method(inputs)

            print('INPUTS: ', inputs, 'EXCEPTS: ', expectation)
            print('OUTPUT: ', r)
            print('CORRECT: ', expectation == r)
    elif getattr(module, 'TestCase', None):
        suite = unittest.makeSuite(module.TestCase, 'test')
        runner = unittest.TextTestRunner()
        runner.run(suite)
    else:
        raise Exception(f'Please check method {method_name}, or add TestCase')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('function_name')
    parser.add_argument('-m', '--module', default='default')

    args = parser.parse_args()

    assert args.function_name is not None, 'Please pass function_name'
    execute_from_command_line(args.function_name, module_name=args.module)
