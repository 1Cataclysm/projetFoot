from flask import Flask

app = Flask(__name__)

# Members api route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Memberss3"]}

if __name__ == "__main__":
    app.run(debug=True)
    