import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS study_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    study_date TEXT,
    content TEXT,
    hours INTEGER
)
""")

cursor.execute("""
INSERT INTO study_records
(study_date, content, hours)
VALUES (?, ?, ?)
""", ("2026-05-21", "Git学習", 2))

conn.commit()

cursor.execute("""
SELECT * FROM study_records
""")

records = cursor.fetchall()

for record in records:
    print(record)

print("完了")