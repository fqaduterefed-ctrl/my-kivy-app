[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,otf

# (list) Application requirements
# ⚠️ ማስተካከያ 1: Cython ስሪት መወሰን አለበት። ለ Kivy አብዛኛውን ጊዜ cython==0.29.33 ይመረጣል
requirements = python3,kivy==2.3.0,cython==0.29.33

# (str) Application versioning (method 1)
version = 0.1

# (list) Supported orientations
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific
# -----------------------------------------------------------------------------

# (int) Target Android API
# ⚠️ ማስተካከያ 2: API 33 እና 34 መረጋጋት እንዲኖራቸው የ NDK ስሪት በግልጽ መጻፍ አለበት
android.api = 33

# (str) Android NDK version
# ⚠️ ማስተካከያ 3: ይህንን አዲስ መስመር ከ android.api በታች ጨምረው (የእስካሁኑ ስህተት መፍትሄ ነው)
android.ndk = 25b

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Format used to package the app for debug mode (apk or aab)
android.debug_artifact = apk

# (str) Format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# [buildozer]
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and command output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
