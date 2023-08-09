from flask import Flask, render_template, url_for
app =  Flask(__name__, template_folder='template')

posts = [
    {
        'author': 'Person 1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 7, 2023'
    },
    {
        
        'author': 'Person 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 8, 2023'
    
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About' )

if __name__ == '__main__':
    app.run(debug=True)