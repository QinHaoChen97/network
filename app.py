#! /usr/bin/env
# -*- coding: utf-8 -*-
import logging

from flask import Flask, request
from multiprocessing import Process

app = Flask(__name__)


@app.route('/00000001/reserve', methods=["GET"])
def reserve_bandwidth():
    """
    请求ryu预留带宽
    """
    # 先进行参数校验，错误返回404 return false,404 返回还是按字典格式返回吧
    bandwidth = request.args.get("bandwidth")
    path = request.args.get("path")
    client_address = request.args.get("client_address")
    if not (bandwidth and path and client_address):
        return {"done": "false", "message": "Parameter transmission error"}, 404
    # 预留资源 return true,200 or false,200

    return {"done": "true", "message": "Bandwidth reservation success"}, 200


@app.route('/00000001/allocate', methods=["GET"])
def allocate_bandwidth():
    """
    请求ryu分配带宽
    """
    bandwidth = request.args.get("bandwidth")
    path = request.args.get("path")
    client_address = request.args.get("client_address")
    if not (bandwidth and path and client_address):
        return {"done": "false", "message": "Parameter transmission error"}, 404

    return {"done": "true", "message": "Resource allocation completed"}, 200


def run():
    app.run(host='0.0.0.0')


p = Process(target=run, args=())
p.daemon = True
p.start()
p.join()
