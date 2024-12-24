from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return f'Welcome {name}!'

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
       return '''
        <form action="/login" method="post">
            <p>Enter Name:</p>
            <p><input type="text" name="nm"></p>
            <p><input type="submit" value="submit"></p>
        </form>
        '''

if __name__ == '__main__':
   app.run(debug = True)
   