## 📊 Telegram Guruh Tahlil Loyihasi

Bu loyiha Telegram guruhidagi so‘nggi 7 kunlik xabarlarni tahlil qiladi va eng ko‘p muhokama qilingan mavzularni aniqlaydi. Natijalar JSON formatda qaytariladi.

### 🛠 Texnologiyalar
- Python 3.11+
- Telethon
- asyncio
- pytz
- aiofiles
- dotenv

---

### 🚀 Ishga tushirish

```bash
# 1. Reponi klonlash
git clone https://github.com/username/telegram_analysis.git
cd telegram_analysis

# 2. Virtual muhit yaratish
python -m venv .venv
source .venv/bin/activate

# 3. Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. .env faylni to‘ldiring
cp .env.example .env
nano .env
```

`.env` fayl tarkibi:
```
API_ID=your_api_id
API_HASH=your_api_hash
GROUP_ID=-100xxxxxxxxxx
TIMEZONE=Asia/Tashkent
```
##### API ID VA HASH NI OLISH HAQIDA QUYIDAGI HAVOLA ORQALI BILISHINGIZ MUMKIN: [bu yerda](https://core.telegram.org/api/obtaining_api_id)
> ⚠️ `GROUP_ID` ni aniqlash uchun `main.py` ichida `get_dialogs()` bilan guruh nomini va ID’sini ko‘ring.

---

### ▶️ Loyihani ishga tushirish

```bash
python main.py
```

Natija quyidagi formatda chiqadi:
```json
{
  "timezone": "Asia/Tashkent",
  "days": [
    {
      "date": "2025-10-17",
      "threads": [
        {"topic": "Мавзу номи", "messages": 25, "users": 8}
      ]
    }
  ]
}
```

---

### ✅ Foydali buyruqlar

```bash
# Sessiyani tozalash (agar login xato bo‘lsa)
rm telegram_analysis.session

