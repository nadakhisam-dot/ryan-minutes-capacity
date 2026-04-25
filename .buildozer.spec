[app]
# اسم التطبيق اللي هيظهر للمستخدم
title = Ryan Minutes Capacity

# الاسم البرمجي (لازم يكون حروف صغيرة وبدون مسافات)
package.name = ryanminutes

# النطاق (ممكن تسيبه كدة)
package.domain = org.ryan

# مكان الكود (النقطة تعني المجلد الحالي)
source.dir = .

# أنواع الملفات اللي هيستخدمها
source.include_exts = py,png,jpg

version = 0.1

# المكتبات المطلوبة (بايثون وكيفي)
requirements = python3,kivy

# وضع الشاشة (طولي)
orientation = portrait

fullscreen = 0

# الصلاحيات (الإنترنت)
android.permissions = INTERNET

# إعدادات الأندرويد (متوافقة مع جيت هب)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.arch = armeabi-v7a
