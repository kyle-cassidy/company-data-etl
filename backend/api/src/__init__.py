from flask import Flask, jsonify, request
from backend.api.src.utils.temp.data_adapters import load_json, CompanyAdapter
from src.clients.fmp_client import FMPClient
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