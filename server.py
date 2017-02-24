# -*- coding:utf8 -*-

from flask import Flask, render_template, url_for, request,redirect,make_response,session
import BaiduMapLocation
import JCloudGPS

app = Flask(__name__)
@app.route('/')
def index():
    client_ip = request.remote_addr
    lat,lng = JCloudGPS.Requester().get_gps(client_ip)
    address = BaiduMapLocation.Requester().get_location(lat,lng)
    return render_template('index.html', info=client_ip, address=lat+','+lng+': '+address)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)