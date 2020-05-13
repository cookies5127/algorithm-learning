import re
import os
import sys
import pkgutil


def get_method_name(file_name):
    method_name = re.sub(r'^\d+_', '', file_name)
    return re.sub(r'_[a-z]', lambda x: x.group()[1:].upper(), method_name)


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

    s = module.Solution()
    method_name = get_method_name(file_name)
    method = getattr(s, method_name, None)
    assert method is not None, f'Please check method {method_name}'

    for inputs, excepts in module.EXAMPLES:
        if isinstance(inputs, tuple):
            r = method(*inputs)
        else:
            r = method(inputs)

        print('INPUTS: ', inputs, 'EXCEPTS: ', excepts)
        print('OUTPUT: ', r)


if __name__ == '__main__':
    argv = sys.argv[1:]
    try:
        function_name = argv[0]
    except IndexError as e:
        function_name = None

    assert function_name is not None, 'Please pass function_name'
    execute_from_command_line(function_name, module_name='default')
