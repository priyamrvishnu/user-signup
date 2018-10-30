from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    username = request.args.get('Username')
    username_error= request.args.get ('username_error')
    passwd = request.args.get('Passwd')
    passwd_error = request.args.get('passwd_error')
    confi_pass = request.args.get('confi_pass')
    confi_pass_error = request.args.get('confi_pass_error')
    e_mail = request.args.get('E_mail')
    e_mail_error = request.args.get('e_mail_error')

    return render_template('userform.html', username_error=username_error, 
        passwd_error=passwd_error,
        confi_pass_error=confi_pass_error,
        e_mail_error=e_mail_error,
        username=username,
        passwd=passwd,
        confi_pass=confi_pass,
        e_mail=e_mail )

@app.route("/welcome", methods=['POST'])
def validate_login():

    username = request.form['Username']
    passwd = request.form['Passwd']
    confi_pass = request.form['confi_pass']
    e_mail = request.form['E_mail']

    username_error = ''
    passwd_error = ''
    confi_pass_error=''
    e_mail_error=''

    numupper =0
    numlower =0
    numdigit=0
    for c in username:
        if c.isupper():
            numupper = numupper + 1
        if c.islower():
            numlower = numlower + 1
        if c.isdigit():
            numdigit = numdigit + 1


    if numupper <= 0:
        username_error=('username must contain at least one uppercase character')
        
       
    if numlower <= 0:
        username_error=('username must contain at least one lowercase character')
        

    if len(username)<6:
        username_error = ('username must be greater than 6 characters')
        
          
    if numdigit <= 0:
        username_error= ('username must contain at least one number')
           

    numupper =0
    numlower =0
    numdigit=0
    for c in passwd:
        if c.isupper():
           numupper = numupper + 1
        if c.islower():
            numlower = numlower + 1
        if c.isdigit():
            numdigit = numdigit + 1

    if numupper <= 0:
        passwd_error=('password must contain at least one uppercase character')
        passwd=''

    elif numlower <= 0:
        passwd_error=('password must contain at least one lowercase character')
        passwd=''

    elif len(passwd)<8:
        passwd_error = ('password must be greater than 8 characters')
        passwd=''

    else:
        if numdigit <= 0:
            passwd_error= ('password must contain at least one number')
            passwd=''
    
    if confi_pass == passwd:
        confi_pass=''
    else:
        confi_pass_error= ('Password does not Match')   

    if '@' not in e_mail or '.com' not in e_mail:
        e_mail_error=('Not a valid email')



    if not username_error and not passwd_error and not confi_pass_error and not e_mail_error:
        return render_template('welcome.html', name= username)
    else:
        return redirect('/?username_error='+username_error+
        '&passwd_error='+passwd_error+
        '&confi_pass_error='+confi_pass_error+
        '&e_mail_error='+e_mail_error+
        '&username='+username+
        '&passwd='+passwd+
        '&confi_pass='+confi_pass+
        '&e_mail='+e_mail)

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['Username']
    return render_template('welcome.html', name=username)

app.run()