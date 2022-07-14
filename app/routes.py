from app.embed import Embed as pbi
from app import app
from flask import render_template

@app.route('/', methods=['GET'])
def home():
    embed = pbi()
    embedURL = embed.getEmbedURL()
    token = embed.getToken()
    reportid = embed.report_id
    return render_template("home.html", embedURL=embedURL, token=token, reportid=reportid)