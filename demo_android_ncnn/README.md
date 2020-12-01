# NanoDet NCNN Android Demo

This repo is an Android object detection demo of NanoDet using
[Tencent's NCNN framework](https://github.com/Tencent/ncnn).

# Tutorial

## Step1. 
Download ncnn-android-vulkan-lib.zip from ncnn repo or build ncnn-android from source.

- [ncnn-android-vulkan-lib.zip download link](https://github.com/Tencent/ncnn/releases)



## Step2.
Unzip ncnn library into demo_android_ncnn/app/src/main/cpp or change the ncnn path in demo_android_ncnn/app/src/main/cpp/CMakeLists.txt

Place as below dir tree:
~~~
.
├─assets
├─cpp
│  └─ncnnvulkan
│      ├─arm64-v8a
│      ├─armeabi-v7a
│      ├─include
│      ├─x86
│      └─x86_64
├─java
└─res
~~~

## Step3.
Copy the NanoDet ncnn model file (nanodet_m.param and nanodet_m.bin) from models folder into demo_android_ncnn/app/src/main/assets

* [NanoDet ncnn model download link](https://github.com/RangiLyu/nanodet/releases/download/v0.0.1/nanodet_ncnn_model.zip)

If you want to run yolov4-tiny and yolov5s, download them and also put in demo_android_ncnn/app/src/main/assets.

* [Yolov4 and v5 ncnn model download link](https://drive.google.com/file/d/1Qk_1fDvOcFmNppDnaMFW-xFpMgLDyeAs/view?usp=sharing)

## Step4.
Open demo_android_ncnn folder with Android Studio and then build it.

**Issue may happen**:
 - Only 4.0 version or newer Android Studio can open it: 
    - Solution: open build.gradle and midify `classpath 'com.android.tools.build:gradle:4.0.0` to your Android Studio version.
 - Invoke-customs are only supported starting with Android O (--min-api 26)
    - Solution:1. Open build.gradle(Module:app) add code in andriod include and Sync
        ~~~
        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }
        ~~~
      see [example](https://blog.csdn.net/dkbnull/article/details/86719390).
    - 2  Add a newer Virtual Device.

# Screenshot
![](Android_demo.jpg)


# Reference

* [ncnn](https://github.com/tencent/ncnn)
* [YOLOv5_NCNN](https://github.com/WZTENG/YOLOv5_NCNN) 

