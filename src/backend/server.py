from flask import jsonify
import app.models.phase_1 as models
from app import create_app, db
import os

app = create_app()


@app.route("/")
def index():
    return "Welcome to the public company insights api"


# returns all companies
@app.route("/companies")
def companies():
    companies = db.session.query(models.SPCompany).all()
    companies_dict = [company.to_dict() for company in companies]
    return jsonify(companies_dict)


# returns a single company by id
@app.route("/companies/id/<int:id>")
def company_id(id):
    company = db.session.query(models.SPCompany).get(id)
    company_dict = company.to_dict()
    return jsonify(company_dict)


# return a company by symbol
@app.route("/companies/symbol/<string:symbol>")
def company_symbol(symbol):
    company = (
        db.session.query(models.SPCompany)
        .filter(models.SPCompany.symbol == symbol)
        .first()
    )
    company_dict = company.to_dict()
    return jsonify(company_dict)


# return all stocks
@app.route("/stocks")
def stocks():
    stocks = db.session.query(models.SPStock).all()
    stocks_dict = [stock.to_dict() for stock in stocks]
    return jsonify(stocks_dict)


# return all stocks by company symbol
@app.route("/stocks/symbol/<string:symbol>")
def stocks_symbol(symbol):
    company = (
        db.session.query(models.SPCompany)
        .filter(models.SPCompany.symbol == symbol)
        .first()
    )
    stocks = company.stocks
    stocks_dict = [stock.to_dict() for stock in stocks]
    breakpoint()
    stocks_json = jsonify(stocks_dict)
    breakpoint()
    return stocks_json


# return all Index Levels
@app.route("/index_levels")
def index_levels():
    index_levels = db.session.query(models.SPIndexLevel).all()
    index_levels_dict = [index_level.to_dict() for index_level in index_levels]
    return jsonify(index_levels_dict)
