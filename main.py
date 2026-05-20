import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    resp = requests.get(url, headers=headers)
    return (resp.text, resp.status_code, resp.headers.items())

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
    resp = requests.get(url, headers=headers)
    return (resp.text, resp.status_code, resp.headers.items())

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
    resp = requests.get(url, headers=headers)
    return (resp.text, resp.status_code, resp.headers.items())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)