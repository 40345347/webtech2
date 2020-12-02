
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homes(): return render_template('web1.html')

@app.route("/guides/")
def guides():  return render_template('guides.html')

@app.route("/character/")
def character():  return render_template('character.html')

@app.route("/characterstats/")
def characterstats(): return render_template('characterstats.html')

@app.route("/player/")
def player(): return render_template('player.html')

@app.route("/stats/")
def stats(): return render_template('stats.html')

@app.route("/lastgamestats/")
def lastgamestats(): return render_template('lastgamestats.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



