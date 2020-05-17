call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
SET CMAKE_GENERATOR_PLATFORM="x64"
python -VV
cl /?
set
python setup.py bdist_wheel

