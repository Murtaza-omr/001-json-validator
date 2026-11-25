# 001-json-validator

أداة سطر أوامر للتحقق من مستندات JSON محليًا، وعرض نوع القيمة العليا وعدد عناصر المصفوفة أو مفاتيح الكائن. لا ترفع الملفات أو تعدّلها.

## المتطلبات

Python 3.10 أو أحدث؛ لا تحتاج إلى مكتبات خارجية.

## التشغيل

```bash
python3 tool.py --help
python3 tool.py sample.json
cat sample.json | python3 tool.py
python3 tool.py sample.json --output report.json
```

يعيد البرنامج رمز خروج `0` عند صحة JSON و`1` عند الخطأ. يتضمن التقرير سطر وعمود الخطأ النحوي عندما تتوفر هذه المعلومات.

## Termux

```bash
pkg update && pkg install python
python tool.py sample.json
```

## iSH

```sh
apk update && apk add python3
python3 tool.py sample.json
```

كل المعالجة محلية على جهازك، ومدخلات الأداة لا تُرسل إلى أي خدمة خارجية.
