from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__,
            template_folder="html",
            static_folder="assets")
app.secret_key = 'your_secret_key'

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",              # Replace with your MySQL username
    password="your_password", # Replace with your MySQL password
    database="user_data"
)

@app.route('/')
def home():
    # Redirect to login if not logged in
    if 'userid' in session:
        return redirect(url_for('welcome'))  # Redirect to welcome if already logged in
    return redirect(url_for('login'))  # Redirect to login if not logged in

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userid' in session:  # If already logged in, redirect to welcome page
        return redirect(url_for('welcome'))

    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']

        cursor = db.cursor()
        # Querying from user_space instead of users
        cursor.execute("SELECT * FROM user_space WHERE user_id = %s AND password = %s", (userid, password))
        user = cursor.fetchone()

        if user:
            session['userid'] = userid  # Set session for logged-in user
            return redirect(url_for('welcome'))
        else:
            return "Invalid credentials! Please try again."
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'userid' in session:  # If already logged in, redirect to welcome page
        return redirect(url_for('welcome'))

    if request.method == 'POST':
        userid = request.form['userid']
        mobile_number = request.form['mobile_number']
        password = request.form['password']

        cursor = db.cursor()

        # Check if the user already exists in user_space
        cursor.execute("SELECT * FROM user_space WHERE user_id = %s", (userid,))
        existing_user = cursor.fetchone()

        if existing_user:
            return "User ID already exists! Please try a different one."

        # Insert new user into user_space
        cursor.execute("INSERT INTO user_space (user_id, mobile_number, password) VALUES (%s, %s, %s)",
                       (userid, mobile_number, password))
        db.commit()  # Commit the transaction
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    # If not logged in, redirect to the login page
    if 'userid' not in session:
        return redirect(url_for('login'))

    # You can add more data here if needed for the welcome page
    return render_template('welcome.html', userid=session['userid'])

@app.route('/logout')
def logout():
    session.pop('userid', None)  # Remove the user from the session
    return redirect(url_for('login'))  # Redirect to login after logging out

if __name__ == '__main__':
    app.run(debug=True)
