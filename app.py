import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 【修复】之前没配置，保存文件会报错

TARGET_LIST = [
    {"name": "张三", "email": "zhangsan@example.com"},
    {"name": "李四", "email": "lisi@example.com"},
    {"name": "王五", "email": "wangwu@example.com"},
    {"name": "小明", "email": "xiaoming@test.com"},
    {"name": "小黄", "email": "xiaoming@test.com"},
]

@app.route('/')
def index():
    return render_template('index.html', targets=TARGET_LIST)

# 【新增】前端实际调用的路由，和 /submit 逻辑一致
@app.route('/submit_single', methods=['POST'])
def submit_single():
    username = request.form.get('username')
    email = request.form.get('email')
    resume = request.files.get('resume')

    if not username:
        return jsonify({"message": "请填写姓名！"})

    if resume:
        resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume.filename))

    return jsonify({"message": f"{username} 提交成功！"})

@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form.get('username')
    email = request.form.get('email')
    resume = request.files.get('resume')

    if not username:
        return jsonify({"status": "error", "message": "请填写姓名！"})

    if resume:
        resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume.filename))

    return jsonify({"status": "success", "message": f"{username} 提交成功！"})

@app.route('/submit_batch', methods=['POST'])
def submit_batch():
    data = request.get_json()
    count = len(data) if data else 0
    print(f"批量提交 {count} 条数据")
    return jsonify({"status": "success", "count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)