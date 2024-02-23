from flask import Flask, jsonify, request
import api.src.db as db
from api.src.models import phase_1 as models
from config import current_config
import simplejson as json
import sqlite3
# from secrets_manager.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER, DEBUG, TESTING
# from src.clients.fmp_client import FMPClient

# old postgres connection
# def create_app():
#     """Create and configure an instance of the Flask application."""
#     app = Flask(__name__)
#     app.config.from_mapping(
#         DB_USER = DB_USER,
#         DB_PASSWORD = DB_PASSWORD,
#         DATABASE= DB_NAME,
#         DB_HOST = DB_HOST,
#         DEBUG = DEBUG,
#         TESTING = TESTING
#     )

def create_app(current_config):
    app = Flask(__name__)
    app.config.from_object(current_config)

    @app.route('/')
    def index():
        return 'Welcome to the public company insights api'

    # returns all companies
    @app.route('/companies')
    def companies():
        conn = db.get_db()
        cursor = conn.cursor()

        companies = db.find_all(models.SPCompany, cursor)
        company_dicts = [company.__dict__ for company in companies]
        return json.dumps(company_dicts, default = str)
    
    # returns a single company by id
    @app.route('/companies/<id>')
    def company_id(id):
        conn = db.get_db()
        cursor = conn.cursor()
        company = db.find(models.SPCompany, id, cursor)
        
        return json.dumps(company.__dict__, default = str)
        
    # return a company by symbol
    @app.route('/companies/symbol/<symbol>')
    def company_symbol(symbol):
        conn = db.get_db()
        cursor = conn.cursor()
        
        company = db.find_by_symbol(models.SPCompany, symbol, cursor)  
        return json.dumps(company.__dict__, default = str)    
    
    
        
    return app
        
        
        
        
        
    # hard coded connection to sqlite3    
    # @app.route('/all')
    # def select_all():
    #     # try:
    #     #     conn = sqlite3.connect('api/data/sp500_p1.sqlite')
    #     #     print("Connected to the database successfully")
    #     #     cursor = conn.cursor()
    #     # except sqlite3.OperationalError as e:
    #     #     print(f"Error: {e}")

    #     # cursor.execute("SELECT * FROM sp_500_companies")  
    #     # records = cursor.fetchall()
    #     # conn.close()
        # return jsonify(records)

    # @app.route('/company/search')
    # def search_companies():
    #     conn = db.get_db()
    #     cursor = conn.cursor()

    #     params = dict(request.args) # {'price': 2}
    #     companies = models.Company.search(params, cursor)
    #     company_dicts = [company.to_json(cursor) for company in companies]
    #     return json.dumps(company_dicts, default = str)

    # @app.route('/companies/<id>')
    # def company(id):
    #     conn = db.get_db()
    #     cursor = conn.cursor()
    #     company = db.find(models.Company, id, cursor)

    #     return json.dumps(company.__dict__, default = str)

    # @app.route('/categories')
    # def categories():
    #     conn = db.get_db()
    #     cursor = conn.cursor()
    #     categories = models.Category.avg_ratings(cursor)
    #     return json.dumps(categories, default = str)

    # return app