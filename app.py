from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Aasth@2006'   
app.config['MYSQL_DB'] = 'artgallery'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/artists')
def artists():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Artist")
    data = cur.fetchall()
    cur.close()
    return render_template('artists.html', artists=data)

@app.route('/add_artist', methods=['POST'])
def add_artist():
    fname = request.form['fname']
    lname = request.form['lname']
    birthplace = request.form['birthplace']
    style = request.form['style']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Artist (fname, lname, birthplace, style) VALUES (%s, %s, %s, %s)",
                (fname, lname, birthplace, style))
    mysql.connection.commit()
    cur.close()
    return redirect('/artists')


@app.route('/galleries')
def galleries():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Gallery")
    data = cur.fetchall()
    cur.close()
    return render_template('galleries.html', galleries=data)

@app.route('/add_gallery', methods=['POST'])
def add_gallery():
    gname = request.form['gname']
    location = request.form['location']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Gallery (gname, location) VALUES (%s, %s)", (gname, location))
    mysql.connection.commit()
    cur.close()
    return redirect('/galleries')

@app.route('/exhibitions')
def exhibitions():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT e.exhibition_id, e.start_date, e.end_date, g.gname
                   FROM Exhibition e LEFT JOIN Gallery g ON e.gallery_id = g.gallery_id""")
    data = cur.fetchall()
    cur.close()
    return render_template('exhibitions.html', exhibitions=data)

@app.route('/add_exhibition', methods=['POST'])
def add_exhibition():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    gallery_id = request.form['gallery_id']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Exhibition (start_date, end_date, gallery_id) VALUES (%s, %s, %s)",
                (start_date, end_date, gallery_id))
    mysql.connection.commit()
    cur.close()
    return redirect('/exhibitions')


@app.route('/artworks')
def artworks():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT a.artwork_id, a.title, a.type_of_art, a.year_created, a.price, ar.fname, ar.lname
                   FROM Artwork a LEFT JOIN Artist ar ON a.artist_id = ar.artist_id""")
    data = cur.fetchall()
    cur.close()
    return render_template('artworks.html', artworks=data)

@app.route('/add_artwork', methods=['POST'])
def add_artwork():
    title = request.form['title']
    type_of_art = request.form['type_of_art']
    year_created = request.form['year_created']
    price = request.form['price']
    artist_id = request.form['artist_id']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Artwork (title, type_of_art, year_created, price, artist_id) VALUES (%s, %s, %s, %s, %s)",
                (title, type_of_art, year_created, price, artist_id))
    mysql.connection.commit()
    cur.close()
    return redirect('/artworks')

@app.route('/customers')
def customers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Customer")
    data = cur.fetchall()
    cur.close()
    return render_template('customers.html', customers=data)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    fname = request.form['fname']
    lname = request.form['lname']
    address = request.form['address']
    dob = request.form['dob']
    phone = request.form['phone']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Customer (fname, lname, address, dob, phone) VALUES (%s, %s, %s, %s, %s)",
                (fname, lname, address, dob, phone))
    mysql.connection.commit()
    cur.close()
    return redirect('/customers')


@app.route('/contacts')
def contacts():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT c.contact_id, cu.fname, cu.lname, c.phone, c.email 
                   FROM Contacts c LEFT JOIN Customer cu ON c.customer_id = cu.customer_id""")
    data = cur.fetchall()
    cur.close()
    return render_template('contacts.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    customer_id = request.form['customer_id']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Contacts (customer_id, phone, email) VALUES (%s, %s, %s)",
                (customer_id, phone, email))
    mysql.connection.commit()
    cur.close()
    return redirect('/contacts')

if __name__ == '__main__':
    app.run(debug=True)
