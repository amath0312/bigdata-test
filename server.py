# -*- coding:utf8 -*-

from flask import Flask, render_template, url_for, request,redirect,make_response,session
import BaiduMapLocation
import JCloudGPS
import Hao7188Location

app = Flask(__name__)
@app.route('/')
def index():
    client_ip = request.remote_addr
    print('============================',client_ip)
    lat,lng = JCloudGPS.Requester().get_gps(client_ip)
    if lat == None:
        lat = '?'
        lng = '?'
        address = 'unknown...'
    else:
        address = BaiduMapLocation.Requester().get_location(lat,lng)
    return render_template('index.html', info=client_ip, address='('+lat+','+lng+') '+address)

@app.route('/gps')
def gps():
    client_ip = request.remote_addr
    print('============================',client_ip)
    #client_ip = '111.198.66.136'
    addresses = Hao7188Location.Requester().get_addr(client_ip)
    print(client_ip+'/r/n'+str(addresses))
    return render_template('gps.html', info=client_ip, addresses=addresses)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)