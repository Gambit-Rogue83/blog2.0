from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
    # name = request.form['name']
    # email = request.form['email']
    # phone = request.form['phone']
    # message = request.form['message']
    # print(f"{name}\n, {email}\n, {phone}\n, {message}\n")


if __name__ == "__main__":
    app.run(debug=True)