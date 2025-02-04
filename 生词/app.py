from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cấu hình MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Serena2103@localhost/pinyin_practice"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Mô hình dữ liệu
class ChineseWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chinese_character = db.Column(db.String(10), nullable=False)
    pinyin = db.Column(db.String(50), nullable=False)

class PracticeHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chinese_character = db.Column(db.String(10), nullable=False)
    correct = db.Column(db.Boolean, nullable=False)

# Tạo bảng trong MySQL
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_words", methods=["GET"])
def get_words():
    words = ChineseWord.query.all()
    word_list = [{"id": w.id, "chinese": w.chinese_character, "pinyin": w.pinyin} for w in words]
    return jsonify(word_list)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    chinese_character = data.get("chinese")  # Người dùng nhập chữ Hán
    user_input = data.get("user_input")  # Chữ Hán mà user nhập vào để so sánh

    correct = chinese_character == user_input  # So sánh chữ Hán đúng không

    history = PracticeHistory(chinese_character=chinese_character, correct=correct)
    db.session.add(history)
    db.session.commit()

    return jsonify({"correct": correct})


if __name__ == "__main__":
    app.run(debug=True)
