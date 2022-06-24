from flask import Flask
import json

jsonFilePath = open('./.venv/scraping/scraping/spiders/json_file.json')
app = Flask(__name__)

# Members api route
@app.route("/members")
def members():
    data = json.load(jsonFilePath)
    return {"members": ["Member1", "Member2", "Memberss3aazaz"]} #data#{"tag":["oui"]}#{"scraping/scraping/spiders/json_file.json"}#

if __name__ == "__main__":
    app.run(debug=True)
    
