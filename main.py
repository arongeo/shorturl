import string
import random
import os.path as paths
from flask import *
import sys


def make_random_id(length):
    chars = string.ascii_letters + string.digits
    result = "".join(random.choice(chars) for i in range(length))
    return result

def make_link(link):
    if "http://" in link or "https://" in link:
        origin_file = open("example").read()
        final_text = origin_file.replace("example", link)

        random_id = make_random_id(5)
        final_link = random_id + ".html"
        if paths.exists("templates/"+final_link) == True:
            random_id = make_random_id(5)
            final_link = random_id + ".html"
            if paths.exists("templates/"+final_link) == True:
                random_id = make_random_id(6)
                final_link = random_id + ".html"
                if paths.exists("templates/"+final_link) == True:
                    random_id = make_random_id(6)
                    final_link = random_id + ".html"
            

        final_final_link = "http://127.0.0.1:5000/" + final_link

        result_file = open("templates/" + final_link, "w")
        result_file.write(final_text)
        return final_final_link
    else:
        return "invalid"

app = Flask(__name__)
app.secret_key = ""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        link = request.form["url"]
        short_link = make_link(link)
        if short_link == "invalid":
            flash("Invalid URL")
        else:
            flash("Short URL: " + short_link)
    return render_template("index.html")

@app.route("/<path:path>", methods=["GET"])
def render_redirect(path):
    does_exist = paths.exists("templates/"+path)
    if does_exist == False:
        does_exist = paths.exists("templates/"+path+".html")
        if does_exist == True:
            path = path+".html"

    print(str(does_exist), file=sys.stderr)

    if does_exist == True:
        return render_template(path[0:])
    else:
        return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=False)
