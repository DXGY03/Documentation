import sqlite3
from flask import Flask, render_template, request,flash,redirect,url_for

app= Flask (__name__)
app.secret_key ='diego'

connection = sqlite3.connect('languages.db', check_same_thread=False)  
cursor = connection.cursor() 

@app.route('/')
def seccion():

   return render_template('page.html')

@app.route('/page', methods=['POST'])
def page():

    return render_template('page.html')

@app.route('/python/documentation')
def return_PyDoc():

    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM python')
    docum = cursor.fetchall()

    return render_template('python-documentation.html', documentations = docum)

@app.route('/documentation', methods=['POST'])
def documentation():

    title = request.form['title']
    doc = request.form['doc']

    data= title,doc

    cursor = connection.cursor() 
    cursor.execute("INSERT INTO python(title,documentation) VALUES (?,?)",data)
    connection.commit()
    flash('Documentation added succesfully')

    return redirect(url_for('return_PyDoc'))
  
@app.route('/nodejs/documentation')
def return_ndjsdoc():

    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM nodejs')
    docum = cursor.fetchall()

    return render_template('nodejspage.html', documentations = docum)

@app.route('/nodejs', methods=['POST'])
def nodejsdocumentation():

    title = request.form['title']
    doc = request.form['doc']

    data= title,doc

    cursor = connection.cursor() 
    cursor.execute("INSERT INTO nodejs(title,documentation) VALUES (?,?)",data)
    connection.commit()
    flash('Documentation added succesfully')

    return redirect(url_for('return_ndjsdoc'))

@app.route('/html/documentation')
def return_htmldoc():

    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM html')
    docum = cursor.fetchall()

    return render_template('htmlpage.html', documentations = docum)

@app.route('/html', methods=['POST'])
def htmldocumentation():

    title = request.form['title']
    doc = request.form['doc']

    data= title,doc

    cursor = connection.cursor() 
    cursor.execute("INSERT INTO html(title,documentation) VALUES (?,?)",data)
    connection.commit()
    flash('Documentation added succesfully')

    return redirect(url_for('return_htmldoc'))

@app.route('/css/documentation')
def return_cssdoc():

    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM css')
    docum = cursor.fetchall()

    return render_template('csspage.html', documentations = docum)

@app.route('/css', methods=['POST'])
def cssdocumentation():

    title = request.form['title']
    doc = request.form['doc']

    data= title,doc

    cursor = connection.cursor() 
    cursor.execute("INSERT INTO css(title,documentation) VALUES (?,?)",data)
    connection.commit()
    flash('Documentation added succesfully')

    return redirect(url_for('return_cssdoc'))

@app.route('/javascript/documentation')
def return_javascriptdoc():

    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM javascript')
    docum = cursor.fetchall()

    return render_template('javascript.html', documentations = docum)

@app.route('/javascript', methods=['POST'])
def javascriptdocumentation():

    title = request.form['title']
    doc = request.form['doc']

    data= title,doc

    cursor = connection.cursor() 
    cursor.execute("INSERT INTO javascript(title,documentation) VALUES (?,?)",data)
    connection.commit()
    flash('Documentation added succesfully')

    return redirect(url_for('return_javascriptdoc'))

if __name__ == '__main__':
    app.run(debug=True)








   
  