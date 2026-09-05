[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,otf
source.include_filters = *.ttf, *.otf, *.py
version = 0.1

# ለየትኛው የፓይተን ስሪት መገንባት እንዳለበት እዚህ ጋር በግልጽ አስገድደነዋል
requirements = python3==3.11.5,kivy==2.3.0

android.api = 33
android.ndk = 25b
android.minapi = 24

# Buildozer አላስፈላጊ የሆኑ የፓይተን የሙከራ (test) ፋይሎችን ሰርዞ እንዲጥል የሚያዝዘው መስመር
android.p4a_extra_args = --exclude-dirs=test,tests

p4a.branch = master
fullscreen = 0
android.permissions = android.permission.INTERNET
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.debug_artifact = apk
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
