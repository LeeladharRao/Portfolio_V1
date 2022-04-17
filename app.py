from flask import Flask, render_template, url_for
import json


app = Flask(__name__)

@app.route("/")
def home():
    i = 0
    extra = ()
    with open ('templates/posts/postsInfo.json', 'r') as f:
        data = json.loads(f.read())
    for post in data['post_data']:
        if (i>=1): break
        else : extra+= (post,)
        i+=1
    return render_template('home.html', postsinfo=extra)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/blog")
def blog():
    with open ('templates/posts/postsInfo.json', 'r') as f:
        data = json.loads(f.read())

    return render_template('blog.html',postsinfo=data)

@app.route("/blog/<bname>")
def blogpost(bname):
    return render_template('posts/'+bname+'.html', url=bname)

if __name__ == '__main__':
    app.run(debug=True)