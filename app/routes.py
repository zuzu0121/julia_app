from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'Gast'}
    posts= [
        {
            'author': {'username': 'Paul'},
            'body': 'Was für ein Tag!'
        },
        {
            'author':{'username':'Myriam'},
                'body': 'Das Wetter ist gut!'
        }
    ]

    return render_template ('index.html', title= 'Home?, user=user, posts=posts)