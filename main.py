from flask import Flask, render_template
import requests

app = Flask(__name__)

# Get json data from API - Data=Post
url_response = 'https://api.npoint.io/45e1b47a1d9ca0fbc906'
response = requests.get(url_response)
json_data = response.json()

date = ['1 August 2021', '24 October 2021', '6 December 2021']

for j in range(3):
    temp = json_data[j]
    temp['date'] = date[j]
    temp['name'] = 'Jeandre Coetzee'


@app.route("/")
def get_all_posts(data=json_data):
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index_var>")
def show_post(index_var):
    requested_page = None
    for blog in json_data:
        if blog['id'] == index_var:
            requested_page = blog
    return render_template("post.html", data=requested_page)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
