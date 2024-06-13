import sqlite3

def init_db():
    # إنشاء اتصال بقاعدة البيانات
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # إنشاء جدول المستخدمين إذا لم يكن موجودًا
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
