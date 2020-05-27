call "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
::SET CMAKE_GENERATOR="Visual Studio 15 2017 Win64"
SET CMAKE_GENERATOR_TOOLSET="host=x64"
SET CMAKE_GENERATOR_PLATFORM="x64"
SET CMAKE_CL_64=1
SET CMAKE_GENERATOR="Visual Studio 15 2017"
python setup.py bdist_wheel
