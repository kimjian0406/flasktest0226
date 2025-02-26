import sqlite3

def create_database():
    # SQLite 데이터베이스 연결
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    # posts 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and table created successfully.")

