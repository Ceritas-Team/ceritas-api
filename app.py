from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from gql.schema import schema
# Create a Flask app
app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))

if __name__ == '__main__':
    app.run(debug=True)