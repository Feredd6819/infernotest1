
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useEffect, useState } from "react";
import { Progress } from "@/components/ui/progress";
import { Switch } from "@/components/ui/switch";
import { Input } from "@/components/ui/input";

const VALID_KEYS = ["KING-2025-VIP", "VIP-ALPHA-01", "VIP-BETA-02"]; // ← add real licensed keys here

export default function InfernoLogHunterDashboard() {
  const [stats, setStats] = useState({ total: 0, elite: 0, today: 0 });
  const [loading, setLoading] = useState(false);
  const [aiMode, setAiMode] = useState(true);
  const [licenseKey, setLicenseKey] = useState("");
  const [licenseValid, setLicenseValid] = useState(false);
  const [generatedKey, setGeneratedKey] = useState("");

  const fetchStats = async () => {
    setLoading(true);
    try {
      const res = await fetch("https://your-api/stats");
      const data = await res.json();
      setStats(data);
    } catch {
      setStats({ total: 666, elite: 66, today: 6 });
    }
    setLoading(false);
  };

  const validateKey = () => {
    if (VALID_KEYS.includes(licenseKey.trim())) {
      setLicenseValid(true);
      alert("✅ تم التحقق من المفتاح! تم تفعيل الوضع النخبوي.");
    } else {
      alert("❌ مفتاح غير صحيح.");
    }
  };

  const generateKey = () => {
    const key = "VIP-" + Math.random().toString(36).substring(2, 6).toUpperCase() + "-" + Date.now().toString().slice(-4);
    setGeneratedKey(key);
    navigator.clipboard.writeText(key);
    alert("🔐 تم توليد المفتاح ونسخه للحافظة.");
  };

  useEffect(() => {
    fetchStats();
  }, []);

  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-4xl font-bold text-center text-red-600 drop-shadow-md">
        InfernoLogHunter Dashboard 🔥
      </h1>
      <p className="text-center text-lg text-muted-foreground">
        🧠 تحت قيادة: <span className="text-yellow-500 font-bold">ملك المبرمجين وملك الكل 👑</span>
      </p>

      <Card>
        <CardContent className="p-6">
          <h2 className="text-2xl font-semibold mb-4">📊 الإحصائيات اللحظية</h2>
          <div className="grid gap-2">
            <div>
              <strong>إجمالي القنوات:</strong> {stats.total}
              <Progress value={(stats.total / 1000) * 100} className="mt-1" />
            </div>
            <div>
              <strong>Elite 🔥:</strong> {stats.elite}
              <Progress value={(stats.elite / stats.total) * 100} className="mt-1" />
            </div>
            <div>
              <strong>قنوات اليوم:</strong> {stats.today}
              <Progress value={(stats.today / stats.total) * 100} className="mt-1" />
            </div>
          </div>
        </CardContent>
      </Card>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Button onClick={fetchStats}>🔄 تحديث</Button>
        <Button variant="destructive" disabled={!licenseValid}>
          🚀 إرسال القنوات الآن
        </Button>
        <Button variant="secondary" disabled={!licenseValid}>
          📥 تصدير البيانات
        </Button>
      </div>

      <Card className="mt-6">
        <CardContent className="p-4">
          <h3 className="text-xl font-semibold mb-2">🧬 خصائص الذكاء المستقبلي</h3>
          <div className="flex items-center justify-between">
            <span>نمط الذكاء الاصطناعي المتقدم</span>
            <Switch checked={aiMode} onCheckedChange={setAiMode} />
          </div>
        </CardContent>
      </Card>

      <Card className="mt-4">
        <CardContent className="p-4">
          <h3 className="text-xl font-semibold mb-2">🔑 نظام الترخيص VIP</h3>
          <p className="text-muted-foreground mb-2">أدخل مفتاح الترخيص لتفعيل كل الميزات:</p>
          <div className="flex gap-2 mb-2">
            <Input
              type="text"
              placeholder="أدخل المفتاح هنا..."
              value={licenseKey}
              onChange={(e) => setLicenseKey(e.target.value)}
            />
            <Button onClick={validateKey}>تفعيل 🔐</Button>
          </div>
          <p className="text-sm text-green-600">
            {licenseValid ? "🟢 تم التحقق من الترخيص - الوضع النخبوي مفعّل!" : ""}
          </p>
        </CardContent>
      </Card>

      <Card className="mt-2">
        <CardContent className="p-4">
          <h3 className="text-xl font-semibold mb-2">🎟️ توليد مفتاح ترخيص VIP</h3>
          <Button onClick={generateKey}>🎫 توليد مفتاح جديد</Button>
          {generatedKey && (
            <p className="text-blue-600 mt-2 text-sm">
              مفتاح جديد: <b>{generatedKey}</b> (تم نسخه تلقائياً)
            </p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
