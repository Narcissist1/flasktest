from alipay import Alipay
from flask import Flask
from config import *

app = Flask(__name__)
alipay = Alipay(pid=PID, key=KEY, seller_email=EMAIL)


@app.route('/')
def alipay_test():
    url = alipay.create_direct_pay_by_user_url(
        out_trade_no='00001',
        subject='Alipay test payment',
        total_fee='0.01',
        return_url='/success')
    return "<a href='%s'>click me</a>" % url


@app.route('/success')
def success():
    return 'payment success'


if __name__ == '__main__':
    app.run(debug=True)
