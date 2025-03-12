from flask import Flask
from flask_restx import Api
from routes.proposals import proposals_bp

# Initialize Flask
app = Flask(__name__)

# Register Blueprint
app.register_blueprint(proposals_bp, url_prefix="/api")

# API Docs
api = Api(app, title="DAO Workflow API", version="1.0", description="API for analyzing DAO proposals")

if __name__ == "__main__":
    app.run(debug=True)
