from flask import jsonify
# import backend.app.models.phase_1 as models
from app import create_app, db

import os

app = create_app()

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