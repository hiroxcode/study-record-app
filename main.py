import sqlite3
conn = sqlite3.connect("study.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    study TEXT
)
""")

#メニュー
while True:
    print("\n---▽ メニュー ▽---")
    print("1: 記録の追加")
    print("2: 一覧表示")
    print("3: 検索")
    print("4: 記録の修正")
    print("5: 記録の削除")
    print("6: 終了")

    menu = input("▷選択してください: ")

# 記録追加
    if menu == "1":
        day = input("日付: ")
        study = input("学習内容: ")
        cursor.execute("""
        INSERT INTO records (day, study)
        VALUES (?, ?)
        """, (day, study))
        conn.commit()

# 一覧表示
    elif menu == "2":
        cursor.execute("SELECT * FROM records")
        records = cursor.fetchall()
        print("\n---▽ 学習記録一覧 ▽---")
        print("----------------")

        for record in records:
            print("ID:", record[0])
            print("日付:", record[1])
            print("内容:", record[2])
            print("----------------")

# 検索
    elif menu == "3":
        search_day = input("検索したい日付: ")
        cursor.execute("""
        SELECT * FROM records
        WHERE day = ?
        """, (search_day,))
        records = cursor.fetchall()
        print("\n--- 検索結果 ---")
        print("----------------")

        if records:
            for record in records:
                print("ID:", record[0])
                print("日付:", record[1])
                print("内容:", record[2])
                print("----------------")
        else:
            print("【記録がありません】")

# 記録の修正
    elif menu == "4":
        update_id = input("修正するID: ")
        new_study = input("新しい学習内容: ")

        cursor.execute("""
        UPDATE records
        SET study = ?
        WHERE id = ?
        """, (new_study, update_id))
        conn.commit()
        print("【更新しました】")
        print("")

# 記録の削除
    elif menu == "5":
        delete_id = input("削除するID: ")
        cursor.execute("""
        DELETE FROM records
        WHERE id = ?
        """, (delete_id,))
        conn.commit()
        print("削除しました")
        print("")

# 終了
    elif menu == "6":
        break

#番号外
    else:
        print("【1〜6で選んでください】")

conn.close()