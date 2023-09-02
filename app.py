from flask import Flask, request, abort

app = Flask(__name__)

def is_sql_injection_attack(payload):
    # Implement your SQL injection detection logic here
    # Return True if an attack is detected, False otherwise
    # Example detection logic: check for common SQL keywords or malicious patterns
    sql_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE"]
    for keyword in sql_keywords:
        if keyword in payload:
            return True
    return False

@app.before_request
def waf_protect():
    payload = request.args.get("q")  # Example: Assuming the payload is passed as a query parameter named 'q'
    if payload and is_sql_injection_attack(payload):
        abort(403)  # Reject the request with HTTP status code 403 (Forbidden)

@app.route("/search")
def search():
    query = request.args.get("q")
    # Process the search query
    return "Search results for: " + str(query)

if __name__ == "__main__":
    app.run()
