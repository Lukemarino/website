import sqlite3
def main():
    conn = sqlite3.connect("site_data.db")
    #Add new
    cursor = conn.execute("INSERT INTO messages VALUES ('Luke', 'just trying to pass',0)")
    cursor.close()
    conn.commit()
    #Query
    cursor = conn.execute("SELECT User, Content, Likes from messages")
    records = cursor.fetchall()
    for record in records:
        print('%s says %s' % (record[0],record[1]))
    cursor.close()
    conn.close()

if __name__=='__main__':
    main()