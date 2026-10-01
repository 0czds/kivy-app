[app]

# (str) عنوان التطبيق
title = My Kivy App

# (str) اسم الحزمة (أحرف صغيرة فقط وبدون مساحات)
package.name = mykivyapp

# (str) النطاق
package.domain = com.mycompany

# (str) المجلد الذي يحتوي على main.py
source.dir = .

# (list) الامتدادات المضمنة
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 0.1
# (list) التبعات المطلوبة للتطبيق
# تنبيه: لا تضع cython هنا إطلاقاً، سيتم التعامل معها من النظام
requirements = python3,kivy==2.3.0

# (str) اتجاه الشاشة (portrait, landscape)
orientation = portrait

# (bool) ملء الشاشة أم لا
fullscreen = 0

# (list) الأذونات المطلوبة (مثال: INTERNET)
# android.permissions = INTERNET

# (int) Target Android API (33 أو 34)
android.api = 34

# (int) أدنى إصدار أندرويد يدعمه التطبيق
android.minapi = 24

# (str) إصدار Android NDK
android.ndk = 25b

# (bool) القبول التلقائي لترخيص SDK
android.accept_sdk_license = True

# (str) المعمارية الموجهة (اختيار arm64-v8a يضمن السرعة وعدم التعارض)
android.archs = arm64-v8a

# (bool) تفعيل دعم AndroidX (ضروري جداً للإصدارات الحديثة)
android.enable_androidx = True

# (str) فرع python-for-android
p4a.branch = master

[buildozer]

# (int) مستوى التوثيق (2 تعني طباعة كل التفاصيل للتصحيح)
log_level = 2

# (int) إظهار تحذير إذا تم التشغيل كـ root
warn_on_root = 1
