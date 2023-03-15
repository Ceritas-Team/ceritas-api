from flask import Flask, request, jsonify
from gql.schema import schema
# Create a Flask app
app = Flask(__name__)

# Define the Flask endpoint
@app.route('/graphql', methods=['POST'])
def graphql():
    data = request.get_json()
    result = schema.execute(data['query'])
    response = {'data': result.data}
    if result.errors:
        response['errors'] = [str(error) for error in result.errors]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)