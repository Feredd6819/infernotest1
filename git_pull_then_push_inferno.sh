
#!/bin/bash

REPO_DIR="infernotest1"
SOURCE_DIR="InfernoLogHunter_Full_Repo_2025"

echo "🔄 جاري سحب التحديثات من GitHub (pull)..."

cd .. || { echo "❌ لا يمكن الصعود لمجلد الأب"; exit 1; }

cd "$REPO_DIR" || { echo "❌ مجلد الريبو $REPO_DIR غير موجود"; exit 1; }

# إعداد git user إذا غير موجود
git config user.name || git config --global user.name "inferno-auto-bot"
git config user.email || git config --global user.email "auto@inferno.bot"

# دمج التحديثات من الريبو البعيد
git pull origin main --allow-unrelated-histories

# نسخ ملفات المشروع دون حذف
cp -r ../$SOURCE_DIR/* .

# رفع التغييرات
git add .
git commit -m "📥 دمج التغييرات من GitHub + تحديث ملفات محلياً"
git push origin main

echo "✅ تم الدمج والدفع إلى GitHub بنجاح!"
