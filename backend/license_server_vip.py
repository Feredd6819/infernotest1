
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# List of valid license keys (you can store in DB or external file in real usage)
VALID_LICENSE_KEYS = {
    "KING-2025-VIP": {"owner": "master", "expires": "2099-12-31"},
    "VIP-ALPHA-01": {"owner": "tester", "expires": "2026-01-01"},
    "VIP-BETA-02": {"owner": "beta", "expires": "2026-06-01"},
}

@app.route('/verify', methods=['POST'])
def verify_license():
    data = request.json
    key = data.get("key", "").strip()
    print(f"[VERIFY] Incoming key: {key} at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    if key in VALID_LICENSE_KEYS:
        return jsonify({
            "valid": True,
            "details": VALID_LICENSE_KEYS[key],
            "message": "✅ Valid license key"
        })
    return jsonify({
        "valid": False,
        "message": "❌ Invalid or expired license key"
    }), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5025)
