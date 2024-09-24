@app.route('/user/<path:user_id>')
def get_user(user_id):
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("SELECT name, email FROM users WHERE user_id = ?", (user_id,))
data = cursor.fetchone()
return render_template_string(f'''<!doctype html>
<title>User information</title>
<h1>User</h1>
<p>Name: {data[0]}</p>
<p>Email: {data[1]}</p>
</form>''')
