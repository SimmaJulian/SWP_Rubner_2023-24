from flask import Flask, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db', check_same_thread=False)
con = connection.cursor()

con.execute("CREATE TABLE IF NOT EXISTS choises_table (name TEXT, count INTEGER)")

@app.route('/post_player_choise', methods=['POST'])
def post():    
    con.execute('SELECT * FROM choises_table')
    rows = con.fetchall()
    
    db_dict = {}
    for row in rows:
        db_dict[row[0].strip()] = row[1]
        
    data = request.form
    for key in data:
        if key in db_dict.keys():
            sql = f"UPDATE choises_table SET count = {int(db_dict[key]) + int(data[key])} WHERE name = '{key}'"
            con.execute(sql)
        else:
            sql = f"INSERT INTO choises_table (name, count) VALUES('{key}', {data[key]})"
            con.execute(sql)
                
        connection.commit()
    return request.form

if __name__ == '__main__':
    app.run(debug=True)