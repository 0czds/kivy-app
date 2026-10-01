[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (هذا يحل خطأ رقم الإصدار)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow C++ standard library
android.accept_sdk_license = True

[buildozer]

# (int) Log level (2 = debug, very useful for troubleshooting)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
