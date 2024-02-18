# FIXME - This file is not complete. It is a very rough template for the api module.

# from flask import Flask, jsonify
# from backend.api.src.db import get_db, close_db, find, find_all
# from backend.api.src.models import Company


# def create_app(config_class):
    
#     app = Flask(__name__)
#     app.config.from_object(config_class)


#     @app.route('/')
#     def index():
#         return 'Welcome to the company insights api'
    
#     @app.route('/companies')
#     def xXXXXXXXs():
#         conn = get_db()
#         curr = conn.cursor()
#         xXXXXXXXs = find_all(XXXXXXXX, conn, curr)
#         # xXXXXXXX_names = [xXXXXXXX.name for xXXXXXXX in xXXXXXXXs]
#         records = [xXXXXXXX.to_json(conn) for xXXXXXXX in actors]
#         json_records = jsonify(records)
#         # breakpoint()
#         return json_records
    
#     @app.route('/company/<id>')
#     def company_id(id):
#         conn = get_db()
#         curr = conn.cursor()
#         actor = find(Company, id, conn, curr)
#         return actor.to_json(conn)
    
#     @app.route('/...')
#     def XXXXXXXXX():
#         conn = get_db()
#         curr = conn.cursor()
#         XXXXXXXXX = find_all(XXXXXXX, conn, curr)
#         xXXXXXX_dicts = [xXXXXXX.to_json(conn) for xXXXXXX in XXXXXXXXX]
#         return xXXXXXX_dicts
   