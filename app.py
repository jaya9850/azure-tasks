from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='text-align:center; margin-top:100px;'>Welcome to Azure App Service 🚀</h1>"

if __name__ == "__main__":
    # Azure App Service automatically sets PORT env variable
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
