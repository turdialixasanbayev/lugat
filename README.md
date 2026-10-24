# Lug'at (Uz-En)

Django asosida yaratilgan oddiy **o'zbekcha - inglizcha va inglizcha - o'zbekcha lug'at** veb-ilovasi. Foydalanuvchi so'z kiritadi, ilova uni ma'lumotlar bazasidan qidirib, tarjimasini ko'rsatadi.

## Imkoniyatlar

- Ikki yo'nalishda tarjima: **Inglizcha → O'zbekcha** va **O'zbekcha → Inglizcha**
- Yo'nalishni bitta tugma bilan almashtirish
- Katta-kichik harfga bog'liq bo'lmagan qidiruv (`iexact`)
- So'z topilmasa, "Bunday so'z topilmadi." xabarini ko'rsatish
- So'zlarni Django Admin paneli orqali qo'shish, tahrirlash va o'chirish
- Moslashuvchan (responsive) sodda interfeys

## Texnologiyalar

- Python (Django 6.x talabiga ko'ra 3.12 yoki undan yuqori versiya)
- Django 6.1.2
- SQLite3 (Development)
- HTML, CSS, JavaScript

## Loyiha tuzilishi

```text
lugat/
├── config/              # Loyiha sozlamalari (settings, urls, wsgi, asgi)
├── tarjimon/            # Asosiy ilova
│   ├── migrations/
│   ├── admin.py         # Dictionary modelini adminga ulash
│   ├── models.py        # Dictionary modeli
│   ├── urls.py          # Ilova URL manzillari
│   └── views.py         # Qidiruv logikasi (search_view)
├── templates/
│   └── index.html       # Yagona sahifa (qidiruv va natija)
├── manage.py
├── requirements.txt
└── README.md
```

## Ma'lumotlar modeli

`tarjimon.models.Dictionary`:

| Maydon    | Turi                    | Tavsif                |
|-----------|-------------------------|-----------------------|
| `uzbek`   | `CharField(max_length=225)` | So'zning o'zbekcha ko'rinishi |
| `english` | `CharField(max_length=225)` | So'zning inglizcha ko'rinishi |

## Qanday ishlaydi

Bosh sahifa (`/`) `search_view` funksiyasiga ulangan va ikkita GET parametr qabul qiladi:

| Parametr    | Qiymatlar                     | Tavsif                                   |
|-------------|-------------------------------|------------------------------------------|
| `q`         | istalgan matn                 | Qidirilayotgan so'z                      |
| `direction` | `en_uz` (standart), `uz_en`   | Tarjima yo'nalishi                       |

Misollar:

```text
/?q=book&direction=en_uz     # inglizcha so'zning o'zbekcha tarjimasi
/?q=kitob&direction=uz_en    # o'zbekcha so'zning inglizcha tarjimasi
```

Qidiruv so'zning **to'liq mosligi** bo'yicha amalga oshiriladi (qisman moslik emas), katta-kichik harf farqlanmaydi. Bir nechta mos yozuv bo'lsa, birinchisi ko'rsatiladi.

## O'rnatish va ishga tushirish

### 1. Repozitoriyni yuklab olish

```bash
git clone https://github.com/turdialixasanbayev/lugat.git
cd lugat
```

### 2. Virtual muhit yaratish va faollashtirish

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Bog'liqliklarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Migratsiyalarni qo'llash

```bash
python manage.py migrate
```

### 5. Admin foydalanuvchi yaratish

```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish

```bash
python manage.py runserver
```

Ilova `http://127.0.0.1:8000/` manzilida ochiladi.

## So'z qo'shish

1. `http://127.0.0.1:8000/admin/` manziliga kiring va superuser hisobi bilan tizimga kiring.
2. **Lug'atlar** bo'limini oching.
3. **Lug'at qo'shish** tugmasini bosib, `uzbek` va `english` maydonlarini to'ldiring.
4. Saqlang. So'z darhol qidiruvda ishlay boshlaydi.

## Muhim eslatmalar

- Bayroq rasmlari `flagcdn.com` dan yuklanadi, shuning uchun ularni ko'rish uchun internet aloqasi kerak.
- Hozirgi `config/settings.py` **faqat ishlab chiqish (development)** uchun mo'ljallangan: `DEBUG = True`, `ALLOWED_HOSTS = ['*']` va `SECRET_KEY` kod ichida turibdi. Productionga chiqarishdan oldin `DEBUG=False`, aniq `ALLOWED_HOSTS` va muhit o'zgaruvchisidan olinadigan `SECRET_KEY` sozlanishi kerak.
- Ma'lumotlar bazasi sifatida SQLite (`db.sqlite3`) ishlatiladi; fayl repozitoriyga qo'shilmasligi kerak.

## Muallif

**Turdiali Xasanbayev**

- GitHub: [github.com/turdialixasanbayev](https://github.com/turdialixasanbayev)
- Telegram: [t.me/turdialixasanbayev](https://t.me/turdialixasanbayev)
- Sayt: [xasanbayev.uz](https://xasanbayev.uz)
