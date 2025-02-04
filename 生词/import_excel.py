import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from app import app, db, ChineseWord 

file_path = "/Users/dinhbuithulinh/Desktop/HSK/生词/hsk3_sheng_ci.xlsx" 
df = pd.read_excel(file_path)

with app.app_context():
    for _, row in df.iterrows():
        word = ChineseWord(chinese_character=row['Chữ Hán'], pinyin=row['Pinyin'])
        db.session.add(word)
    db.session.commit()

print("Nhập dữ liệu từ Excel vào MySQL thành công!")
