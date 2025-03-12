from flask import Flask
from flask_restx import Api
from routes.proposals import proposals_bp
from routes.auth import auth_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(proposals_bp, url_prefix="/api/proposals")
app.register_blueprint(auth_bp, url_prefix="/api/auth")

api = Api(app, title="DAO Workflow API", version="2.0", description="Upgraded DAO API with Authentication & Voting")

if __name__ == "__main__":
    app.run(debug=True)
