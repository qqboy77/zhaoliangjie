#encoding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>赵良杰</h1><a href="http://baike.baidu.com/link?url=e_3-EEOhHoqu45yvU589kVuYR6NcZsF1JjebZpEfz4W6n8GcIUVQ6LXsgxYu7bHIQQroT_lA6ps7Jtx8gIAb1k6mWjhQT_UEL7DuplBdr93">baiji</a>'


if __name__ == '__main__':
	app.run(debug=True)
