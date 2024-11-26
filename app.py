from flask import Flask

app = Flask(__name__)

# Tạo route (đường dẫn) cho ứng dụng
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!", 200  # Phản hồi HTTP 200 (OK)

if __name__ == '__main__':
    app.run(debug=True)  # Chạy ứng dụng Flask
