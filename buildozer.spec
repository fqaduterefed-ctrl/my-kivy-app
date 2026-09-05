[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (plus Amharic font support)
source.include_exts = py,png,jpg,kv,atlas,ttf,otf

# (str) Application version
version = 0.1

# (list) Application requirements
# እዚህ ላይ የተረጋጋውን የPython 3.11 ስሪት በግልጽ አስገብተነዋል
requirements = python3==3.11.5,kivy==2.3.0

# (int) Target Android API
# ለGoogle Play Store ዝቅተኛው መስፈርት API 34 ስለሆነ ወደ 34 አሳድጌዋለሁ
android.api = 34

# (str) Android NDK version to use
# ከAPI 34 ጋር በትክክል የሚሰራውን የNDK ስሪት መርጫለሁ
android.ndk = 26b

# (int) Minimum API your APK will support
android.minapi = 24

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = android.permission.INTERNET

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Format used to package the app for debug mode
android.debug_artifact = apk

# (str) Format used to package the app for release mode
android.release_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and command output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
