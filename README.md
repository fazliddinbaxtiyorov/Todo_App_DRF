## Todo App Django-Rest-Framework

**Yuklab Olish**
```
git clone https://github.com/fazliddinbaxtiyorov/Todo_App_DRF.git
```
**Foydalanish**
```
 pip install -r requirements.txt
```
**Dasturni Ishlatish**
  * Dasturni pasdagi komandani terminal bilan ishga tushuring: 
```
python manage.py runserver
```


**Dasturni Boshqarish**

* GET/  http://127.0.0.1:8000/api/ - Barcha todolarni ko'rish uchun
* Post/  http://127.0.0.1:8000/api/new - yangi todo yaratish
* GET/  http://127.0.0.1:8000/api/id - todolarni id bo'yicha ko'rish
* Delete/  http://127.0.0.1:8000/api/id/delete - todolarni id bo'yicha o'chirish
* Put/Patch  http://127.0.0.1:8000/api/id/update - todolarni id bo'yicha yangilash
