import os
from setuptools import setup, Extension, find_packages

packages = find_packages()
print(packages)

setup(
    name='py_c_miniextension',
    # packages=['src'],
    # install_requires=[''],
    classifiers=['Development Status :: 3 - Alpha'],
    ext_modules=[
        # Extension('ctypes_foo_module', ['mylib/py_ctypes_foo/foo.cpp']),
        Extension('cos_module', ['mylib/py_c_interface_cos/cos_module.c']),
        Extension('_cswig_cos', ['mylib/cswig_cos/cos_wrap.c', 'mylib/cswig_cos/cos.c']),
        Extension('_fact', ['mylib/cppswig_factorial/factorial_wrap.cxx',
                            'mylib/cppswig_factorial/factorial.cpp'],
                  extra_compile_args=['-std=c++11']),
        Extension('_mystack', ['mylib/cppswig_stack/mystack.cpp', 'mylib/cppswig_stack/mystack_wrap.cxx']),
        # Boost linking: https://www.quora.com/How-do-you-distribute-Boost.Python-modules
        Extension('_stat_printer', ['mylib/myboost/stat_printer_wrap.cxx'],
                include_dirs=['C:/Libraries/boost_1_59_0'], extra_compile_args=['/EHsc'])
     ],
    packages = packages,
    entry_points={'console_scripts': ['miniextension_test=mylib.script.miniextension_test:main']}
)
