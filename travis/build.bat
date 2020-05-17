::call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
cmake --help
SET CMAKE_GENERATOR="Visual Studio 16 2019"
set
python setup.py bdist_wheel

