# NanoDet NCNN Demo

This project provides NanoDet image inference, webcam inference and benchmark using
[Tencent's NCNN framework](https://github.com/Tencent/ncnn).

# How to build

## Windows
### Step1.
Download and Install Visual Studio from https://visualstudio.microsoft.com/vs/community/

### Step2.
Download and install OpenCV from https://github.com/opencv/opencv/releases
rebuild source code and cut build files into `../build`
~~~
> cd <path_for_opencv>
> cd build
> cmake ..
> cd ..
> robocopy build ../build /s
> rd /s /q build
~~~

set `<openCV_path>\build\x64\vc14\bin` in environment settings `PATH`.

### Step3(Optional).
Download and install Vulkan SDK from https://vulkan.lunarg.com/sdk/home

### Step4.
Clone NCNN repository

``` shell script
git clone --recursive https://github.com/Tencent/ncnn.git
```
Build NCNN following this tutorial: [Build for Windows x64 using VS2017](https://github.com/Tencent/ncnn/wiki/how-to-build#build-for-windows-x64-using-visual-studio-community-2017)

**NOTICE: `x64 Native Tools Command Prompt` means `x64 本机工具命令提示符` in Chinese.**


### Step5.

Modify CMakeLists.txt to your environment settings.

Build project

Open x64 Native Tools Command Prompt(Chinese: `x64 本机工具命令提示符`) for VS 2019 or 2017

``` cmd
cd <this-folder>
mkdir -p build
cd build
cmake .. 
msbuild nanodet_demo.vcxproj /p:configuration=release /p:platform=x64
```


**Issue may happen:**
 - Could not find "FindOpenCV.cmake" when run `cmake ..`
     ~~~
     CMake Error at CMakeLists.txt:15 (find_package):
      By not providing "FindOpenCV.cmake" in CMAKE_MODULE_PATH this project has
      asked CMake to find a package configuration file provided by "OpenCV", but
      CMake did not find one.
      ...
     ~~~
    - Solution: set a new line in CMakeList.txt: `set(OpenCV_DIR "<path for openCV>/build/x64/vc14/lib")`, where can find `OpenCVConfig.cmake`. Restart `x64 Native Tools Command Prompt` after modification.
 - Found OpenCV Windows Pack but it has no bineries compatible with your configuration.
      ~~~
     You should manually point CMake variable OpenCV_DIR to your build of OpenCV library.
    Call Stack (most recent call first):
      CMakeLists.txt:15 (find_package)
      ...
     ~~~
    - Solution: set a new line in CMakeList.txt: `set(OpenCV_DIR "<path for openCV>/build/x64/vc14/lib")`, where can find `OpenCVConfig.cmake`. Restart `x64 Native Tools Command Prompt` after modification.
 - error MS8020: The build tools for VS 2010 cannot be fond.
   ~~~
    “E:\03personal\DeepLearning\nanodet\demo_ncnn\build-vs2015\nanodet_demo.vcxproj”(默认目标) (1) ->
    “E:\03personal\DeepLearning\nanodet\demo_ncnn\build-vs2015\ZERO_CHECK.vcxproj”(默认目标) (2) ->
    (PlatformPrepareForBuild 目标) ->
      C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.Cpp.Platform.targets(55,5): error MSB8020: The build
     tools for Visual Studio 2010 (Platform Toolset = 'v100') cannot be found. To build using the v100 build tools, please
    install Visual Studio 2010 build tools.  Alternatively, you may upgrade to the current Visual Studio tools by selecting
     the Project menu or right-click the solution, and then selecting "Retarget solution". [E:\03personal\DeepLearning\nano
    det\demo_ncnn\build-vs2015\ZERO_CHECK.vcxproj]
   ~~~
    - Solution: replace `cmake -DCMAKE_GENERATOR_PLATFORM=x64 ..` to `cmake ..`. And then run `msbuild nanodet_demo.vcxproj /p:configuration=release /p:platform=x64`

## Linux

### Step1.
Build and install OpenCV from https://github.com/opencv/opencv

### Step2(Optional).
Download Vulkan SDK from https://vulkan.lunarg.com/sdk/home

### Step3.
Clone NCNN repository

``` shell script
git clone --recursive https://github.com/Tencent/ncnn.git 
```

Build NCNN following this tutorial: [Build for Linux / NVIDIA Jetson / Raspberry Pi](https://github.com/Tencent/ncnn/wiki/how-to-build#build-for-linux)

### Step4.

Modify CMakeLists.txt to your environment settings.

Build project

``` shell script
cd <this-folder>
mkdir build
cd build
cmake ..
make
```

# Run demo

Download NanoDet ncnn model.
* [NanoDet ncnn model download link](https://github.com/RangiLyu/nanodet/releases/download/v0.0.1/nanodet_ncnn_model.zip)

Copy nanodet_m.param and nanodet_m.bin to demo program folder.

## Webcam

```shell script
nanodet_demo 0 0
```

## Inference images

```shell script
nanodet_demo 1 IMAGE_FOLDER/*.jpg
```

## Inference video

```shell script
nanodet_demo 2 VIDEO_PATH
```

## Benchmark

```shell script
nanodet_demo 3 0
```
![bench_mark](benchmark.jpg)
****

Notice:

If benchmark speed is slow, try to limit omp thread num.

Linux:

```shell script
export OMP_THREAD_LIMIT=4
```
