
# Struktura

Ushbu loyiha uchun quyidagi papka va fayl strukturasi yaratilgan:

## Loyihaning papka va fayl tuzilmasi

```
business-trip/
├── app/
│   ├── api/           # API endpointlar va marshrutlar (SOLID printsiplari asosida)
│   ├── core/          # Konfiguratsiya va asosiy yordamchi funksiyalar
│   ├── db/            # Ma'lumotlar bazasi bilan ishlash (ulanish va sozlamalar)
│   ├── models/        # ORM modellari (ma'lumotlar bazasi uchun)
│   ├── repository/    # Ma'lumotlar qatlamiga kirish (repository pattern)
│   ├── schemas/       # Pydantic sxemalari (ma'lumotlarni tekshirish va serializatsiya)
│   ├── service/       # Biznes logika va servis funksiyalari
│   └── views/         # Frontend yoki tashqi ko'rinish uchun endpointlar
├── requirements.txt   # Loyihada ishlatiladigan kutubxonalar ro'yxati
├── README.md          # Loyihaning qisqacha tavsifi
└── .env               # Maxfiy sozlamalar (token, db url va boshqalar)
```

### Papka va fayllar izohi

- **app/api/** — API endpointlar va marshrutlar (SOLID printsiplari asosida).
- **app/core/** — Loyihaning asosiy konfiguratsiyasi va yordamchi funksiyalari.
- **app/db/** — Ma'lumotlar bazasi bilan ishlash va ulanish.
- **app/models/** — ORM modellari, ma'lumotlar bazasi tuzilmasi.
- **app/repository/** — Repository pattern orqali ma'lumotlar qatlamiga kirish.
- **app/schemas/** — Ma'lumotlarni tekshirish va serializatsiya uchun sxemalar.
- **app/service/** — Biznes logika va servis funksiyalari.
- **app/views/** — Frontend yoki tashqi ko'rinish uchun endpointlar.
- **requirements.txt** — Loyihada ishlatiladigan barcha kutubxonalar ro'yxati.
- **.env** — Maxfiy sozlamalar va atrof-muhit o'zgaruvchilari.


