

   
   
   


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