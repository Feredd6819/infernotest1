
#!/bin/bash

echo "🚀 بدء رفع مشروع InfernoLogHunter إلى GitHub..."

# إعداد المشروع
git init
git remote remove origin 2> /dev/null
git remote add origin https://github.com/Feredd6819/infernotest1.git
git add .
git commit -m "🔥 Initial launch of InfernoLogHunter with Dashboard & Smart Bot"
git branch -M main

# رفع المشروع بالقوة
git push -f origin main

echo "✅ تم رفع المشروع بنجاح إلى GitHub!"
