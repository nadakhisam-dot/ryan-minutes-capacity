my = input('أهلا بك في الساعة ')
import os
os.system('clear')
print('جاري أنتهاء الوقت')
seconds = int(my)
import time
time.sleep(seconds)
os.system('clear')
print('أنتها الوقت')
print('حالة الهاتف')
import os

# هذا الأمر يطلب من الموبايل "مباشرة" عرض معلومات المعالج
# المعالج بيفهم الأمر ده أسرع من أي كود تاني
print("--- معلومات المعالج بلغة النظام ---")
os.system('cat /proc/cpuinfo')

# أمر آخر لجعل الموبايل "يفكر" ويخرج قائمة الملفات
os.system('ls')
