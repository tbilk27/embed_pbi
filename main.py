from flask import Flask, render_template
import pbi.run as pbi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    embed = pbi.Embed()
    embedURL = embed.getEmbedURL()
    token = embed.getToken()
    reportid = embed.report_id
    return render_template("home.html", embedURL=embedURL, token=token, reportid=reportid)

if __name__ == "__main__":
    app.run(port=9000, debug=True)