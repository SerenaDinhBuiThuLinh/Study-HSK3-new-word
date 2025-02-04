import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from app import app, db, ChineseWord 

file_path = "yourpath/生词/hsk3_sheng_ci.xlsx" 
df = pd.read_excel(file_path)

with app.app_context():
    for _, row in df.iterrows():
        word = ChineseWord(chinese_character=row['Chữ Hán'], pinyin=row['Pinyin'])
        db.session.add(word)
    db.session.commit()

print("Import data from Excel to MySQL successfully!")
