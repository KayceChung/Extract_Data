import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Đảm bảo cho phép mọi header custom qua CORS
CORS(app, expose_headers="*", allow_headers="*")

VEXERE_BASE = "https://nhaxe.vexere.com"

# Proxy API lấy phương tiện
@app.route('/api/vehicles')
def proxy_vehicles():
    company_id = request.args.get('company_id', '46249')
    url = f"{VEXERE_BASE}/api/v1/vehicle?filter[where][comp_id]={company_id}&filter[per_page]=100000"
    headers = {
        'User-Agent': request.headers.get('User-Agent', ''),
        'Authorization': request.headers.get('Authorization', ''),
        'Cookie': request.headers.get('Cookie', ''),
        'x-signature': request.headers.get('x-signature', ''),
        'device-id': request.headers.get('device-id', ''),
        'productname': request.headers.get('productname', ''),
        'origin-request-id': request.headers.get('origin-request-id', ''),
        'origin-request-product': request.headers.get('origin-request-product', ''),
        'x-data-mode': request.headers.get('x-data-mode', ''),
        'x-requested-with': request.headers.get('x-requested-with', 'XMLHttpRequest'),
        'Content-Type': 'application/json; charset=utf-8',
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9,en-US;q=0.8',
    }
    try:
        print("[DEBUG] Headers nhận được:", headers)
        print("[DEBUG] URL gọi tới:", url)
        resp = requests.get(url, headers=headers, timeout=10)
        print("[DEBUG] Response từ vexere:", resp.status_code, resp.text[:1000])
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        print(f"Error fetching vehicles: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Proxy API lấy tài xế
@app.route('/api/drivers')
def proxy_drivers():
    company_id = request.args.get('company_id', '46249')
    url = f"{VEXERE_BASE}/api/v1/driver?company_id={company_id}&type=2"
    headers = {
        'User-Agent': request.headers.get('User-Agent', ''),
        'Authorization': request.headers.get('Authorization', ''),
        'Cookie': request.headers.get('Cookie', ''),
        'x-signature': request.headers.get('x-signature', ''),
        'device-id': request.headers.get('device-id', ''),
        'productname': request.headers.get('productname', ''),
        'origin-request-id': request.headers.get('origin-request-id', ''),
        'origin-request-product': request.headers.get('origin-request-product', ''),
        'x-data-mode': request.headers.get('x-data-mode', ''),
        'x-requested-with': request.headers.get('x-requested-with', 'XMLHttpRequest'),
        'Content-Type': 'application/json; charset=utf-8',
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9,en-US;q=0.8',
    }
    try:
        print("[DEBUG] Headers nhận được:", headers)
        print("[DEBUG] URL gọi tới:", url)
        resp = requests.get(url, headers=headers, timeout=10)
        print("[DEBUG] Response từ vexere:", resp.status_code, resp.text[:1000])
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        print(f"Error fetching drivers: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Proxy API lấy chuyến
@app.route('/api/trips')
def proxy_trips():
    company_id = request.args.get('company_id', '46249')
    url = f"{VEXERE_BASE}/api/v1/trip/get_trips?comp_id={company_id}"
    headers = {
        'User-Agent': request.headers.get('User-Agent', ''),
        'Authorization': request.headers.get('Authorization', ''),
        'Cookie': request.headers.get('Cookie', ''),
        'x-signature': request.headers.get('x-signature', ''),
        'device-id': request.headers.get('device-id', ''),
        'productname': request.headers.get('productname', ''),
        'origin-request-id': request.headers.get('origin-request-id', ''),
        'origin-request-product': request.headers.get('origin-request-product', ''),
        'x-data-mode': request.headers.get('x-data-mode', ''),
        'x-requested-with': request.headers.get('x-requested-with', 'XMLHttpRequest'),
        'Content-Type': 'application/json; charset=utf-8',
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9,en-US;q=0.8',
    }
    try:
        print("[DEBUG] Headers nhận được:", headers)
        print("[DEBUG] URL gọi tới:", url)
        resp = requests.get(url, headers=headers, timeout=10)
        print("[DEBUG] Response từ vexere:", resp.status_code, resp.text[:1000])
        return (resp.text, resp.status_code, resp.headers.items())
    except Exception as e:
        print(f"Error fetching trips: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)