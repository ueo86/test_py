import io
import time
import numpy as np
import pandas as pd
import json
import requests
import zlib

def test_standardsend():
    df = pd.read_csv("out.csv", header=None)
    sendData = {"data": df[0].to_list()}

    sendData = json.dumps(sendData)

    s = time.time()
    r = requests.post("http://192.168.50.16:8002/req", data=sendData)
    print(r.text)

    print(time.time()-s)

def test_withzip():
    iob = io.StringIO()
    ios = io.BytesIO()

    df = pd.read_csv("out.csv", header=None)
    headers = {
        'Content-Encoding': 'gzip',
        'Content-Type': 'multipart/form-data'
    }

    d = json.dumps({"data": df[0].to_list()})

    iob.write(d)

    payloadData = zlib.compress(iob.getvalue().encode("utf-8"), level=2)
    params = {
        'キー1':'値1'
    }
    files = {"file": ("filename", payloadData)}
    s = time.time()
    r = requests.post("http://192.168.50.16:8002/req_compress", files=files)
    print(r.text)

    print(time.time()-s)


if __name__ == "__main__":
    test_standardsend()
    # test_withzip()