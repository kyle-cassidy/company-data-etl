from flask import jsonify
import app.models.phase_1 as models
from app import create_app, db

import os

app = create_app()

@app.route('/')
def index():
    return 'Welcome to the public company insights api'

# returns all companies
@app.route('/companies')
def companies():
    companies = db.session.query(models.SPCompany).all()
    companies_dict = [company.to_dict() for company in companies]
    return jsonify(companies_dict)
    
# returns a single company by id
@app.route('/companies/<int:id>')
def company_id(id):
    company = db.session.query(models.SPCompany).get(id)
    company_dict = company.to_dict()
    return jsonify(company_dict)
    
# return a company by symbol
@app.route('/companies/symbol/<string:symbol>')
def company_symbol(symbol):
    company = db.session.query(models.SPCompany).filter(models.SPCompany.symbol == symbol).first()
    company_dict = company.to_dict()    
    return jsonify(company_dict)