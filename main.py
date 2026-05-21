import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Đảm bảo cho phép mọi header custom qua CORS
CORS(app, expose_headers="*", allow_headers="*")

VEXERE_BASE = "https://nhaxe.vexere.com"

# Proxy API lấy phương tiện (forward toàn bộ headers)
@app.route('/api/vehicles')
def proxy_vehicles():
    company_id = request.args.get('company_id', '46249')
    url = f"{VEXERE_BASE}/api/v1/vehicle?filter[where][comp_id]={company_id}&filter[per_page]=100000"
    # Forward toàn bộ headers từ request extension
    incoming_headers = dict(request.headers)
    # Xóa các header không cần thiết hoặc gây lỗi
    for h in ['Host', 'Content-Length', 'Connection', 'Accept-Encoding']: incoming_headers.pop(h, None)
    print("[DEBUG] Headers nhận được từ extension:", dict(request.headers))
    print("[DEBUG] Headers gửi đi Vexere:", incoming_headers)
    print("[DEBUG] URL gọi tới:", url)
    try:
        resp = requests.get(url, headers=incoming_headers, timeout=10)
        print("[DEBUG] Response từ vexere:", resp.status_code, resp.text[:1000])
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        print(f"Error fetching vehicles: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Proxy API lấy tài xế (forward toàn bộ headers)
@app.route('/api/drivers')
def proxy_drivers():
    company_id = request.args.get('company_id', '46249')
    url = f"{VEXERE_BASE}/api/v1/driver?company_id={company_id}&type=2"
    incoming_headers = dict(request.headers)
    for h in ['Host', 'Content-Length', 'Connection', 'Accept-Encoding']: incoming_headers.pop(h, None)
    print("[DEBUG] Headers nhận được từ extension:", dict(request.headers))
    print("[DEBUG] Headers gửi đi Vexere:", incoming_headers)
    print("[DEBUG] URL gọi tới:", url)
    try:
        resp = requests.get(url, headers=incoming_headers, timeout=10)
        print("[DEBUG] Response từ vexere:", resp.status_code, resp.text[:1000])
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        print(f"Error fetching drivers: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Proxy API lấy chuyến (forward toàn bộ headers)
@app.route('/api/trips')
def proxy_trips():
    company_id = request.args.get('company_id', '46249')
    url = f"{VEXERE_BASE}/api/v1/trip/get_trips?comp_id={company_id}"
    incoming_headers = dict(request.headers)
    for h in ['Host', 'Content-Length', 'Connection', 'Accept-Encoding']: incoming_headers.pop(h, None)
    print("[DEBUG] Headers nhận được từ extension:", dict(request.headers))
    print("[DEBUG] Headers gửi đi Vexere:", incoming_headers)
    print("[DEBUG] URL gọi tới:", url)
    try:
        resp = requests.get(url, headers=incoming_headers, timeout=10)
        print("[DEBUG] Response từ vexere:", resp.status_code, resp.text[:1000])
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        print(f"Error fetching trips: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)