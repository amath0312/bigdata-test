# -*- coding:utf8 -*-

from flask import Flask, render_template, url_for, request,redirect,make_response,session

app = Flask(__name__)
@app.route('/')
def index():
    client_ip = request.remote_addr
    lat,lng = JCloudGPS().get_gps(client_ip)
    return render_template('index.html', info=client_ip, address=lat+','+lng)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)