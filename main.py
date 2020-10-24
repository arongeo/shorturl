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

        # with this we have 57 716 368 416 possible url combinations
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
        return "Invalid URL"

app = Flask(__name__)
app.secret_key = "Wv8O3T4Yj4AhE7M7s5NRHDKLRSv0gMjBcwSTEcQPwieu5CyB37HUnT4PVG4LaqteOWM7YYnLJarNtAWiS6JMHmDnY24oq337HsvhrHvHgBNukbLsBJZ0Es7cTmgdhzERXsRxiqbrPyyZfOAUoLXMfVXXUD9MdFM1zTHj4jvIs1vgOtLyl2I3VEGydOCyDRgP4HQcVVWNvgbeQ9yNdugOwHBNKELKDrMHt1a0TISZJbxMkuTR9mhy5bkPBeJiaAGQzoXKqmSeFZMQKXgHmv4g5fzo0M7Pd74jgqyML6imYFZ1IycsKfjrDz8QryRGxZkQROGx5RxoF28HRcPVGbO1Cde77Qgnw4MLyvMOXYDObEL0LMPP0TCjyP1bK8a3jqWMmkbqnS7xgl9DTk9M3bjdaQMpSiFzjaYl6FYjPlUmKNhV8SPd72WeIRLTktlim8R0Jt5KuTKau1cGUqmuFfhct0ynkm54nhfR80EU4ejljnjKFVnxX2ev9wVdBkjDAHUDSqC8gLc1lHo48tXC75oMUmknXHuyN7IgoXGP7e6Kjr6kOdqk4S94NdfwCg3IOsjFQ0vWLM01K9vcwhpU2hDDnP5E3rvP20snOt1GAt288kXsPksTKPzKljkNe6ZpqlEKxJxaNxawKrxp4RpdgzSgQ1ISPchgfs2513QURsAEVhXAyEF0DAOyrH9r52MFBdTd1KG4a4I7tKTYbcxEVY1DgkjAFx73W5ZzZk1o69x9P5Faad"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        link = request.form["url"]
        short_link = make_link(link)
        flash("Short URL: " + short_link)
    return render_template("index.html")

@app.route("/<path:path>", methods=["GET"])
def render_redirect(path):
    does_exist = paths.exists("templates/"+path)

    print(str(does_exist), file=sys.stderr)

    if does_exist == True:
        return render_template(path[0:])
    else:
        return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)