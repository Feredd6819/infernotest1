
#!/bin/bash

REPO_DIR="infernotest1"
SOURCE_DIR="InfernoLogHunter_Full_Repo_2025"

echo "🚀 بدء تحديث ملفات مشروع GitHub بدون حذف القديم..."

cd .. || { echo "❌ لا يمكن الصعود لمجلد أب."; exit 1; }

cd "$REPO_DIR" || { echo "❌ مجلد الريبو $REPO_DIR غير موجود!"; exit 1; }

# إعداد git user إن لم يكن موجود
git config user.name || git config --global user.name "inferno-auto-bot"
git config user.email || git config --global user.email "auto@inferno.bot"

# نسخ وتحديث الملفات من المشروع الجديد إلى الريبو
cp -r ../$SOURCE_DIR/* .

# رفع التغييرات
git add .
git commit -m "📤 تحديث ملفات Inferno بدون حذف القديم"
git push origin main

echo "✅ تم رفع الملفات بنجاح دون حذف أي شيء."
