from flask import Flask, jsonify, request
from .src.utils.data_adapters import load_json, CompanyAdapter
from .src.clients.fmp_client import FMPClient
import api.src.db as db

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/')
    def index():
        return 'Welcome to the public company insights api'

    @app.route('/companies')
    def companies():
        conn = db.get_db()
        cursor = conn.cursor()

        companies = db.find_all(models.Company, cursor)
        company_dicts = [company.to_json(cursor) for company in companies]
        return json.dumps(company_dicts, default = str)

    @app.route('/company/search')
    def search_companies():
        conn = db.get_db()
        cursor = conn.cursor()

        params = dict(request.args) # {'price': 2}
        companies = models.Company.search(params, cursor)
        company_dicts = [company.to_json(cursor) for company in companies]
        return json.dumps(company_dicts, default = str)

    @app.route('/companies/<id>')
    def company(id):
        conn = db.get_db()
        cursor = conn.cursor()
        company = db.find(models.Company, id, cursor)

        return json.dumps(company.__dict__, default = str)

    @app.route('/categories')
    def categories():
        conn = db.get_db()
        cursor = conn.cursor()
        categories = models.Category.avg_ratings(cursor)
        return json.dumps(categories, default = str)

    return app

   
   
   


    # @app.route('/companies', methods=['POST'])
    # def load_companies():
    #     # Ensure JSON content type
    #     if not request.is_json:
    #         return jsonify({"error": "Request must be JSON"}), 400

    #     # Extract ticker from the JSON body
    #     ticker = request.json.get('ticker')
    #     if not ticker:
    #         return jsonify({"error": "Ticker is required"}), 400

    #     # Fetch company profile using the FMPClient
    #     client = FMPClient()
    #     company_profile = client.request_company_profile(ticker)
    #     if not company_profile:
    #         return jsonify({"error": "Company profile not found"}), 404

    #     # Load company profile into the database
    #     conn = get_db()
    #     cursor = conn.cursor()
    #     try:
    #         CompanyAdapter.load(company_profile, conn, cursor)
    #     except Exception as e:
    #         conn.rollback()
    #         return jsonify({"error": str(e)}), 500
    #     finally:
    #         cursor.close()

    #     return jsonify({"message": "Company profile loaded successfully"}), 200

    # return app