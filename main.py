from flask import Flask, request
import random

app = Flask(__name__)

# Define responses for the chatbot
greeting_responses = ['Hello!', 'Hi there!', 'Welcome!', 'Greetings!']
product_responses = [
    'Our frameless glazing technology provides an elegant, modern look for any space. It offers unobstructed views, energy efficiency, and easy maintenance.',
    'Our frameless glazing technology is the perfect solution for those who want a sleek and modern look for their space. It provides great energy efficiency and ease of maintenance.',
    'Our frameless glazing technology is the perfect choice for those who want a minimalist look for their space. It provides great energy efficiency, ease of maintenance, and a seamless transition from indoor to outdoor.']
contact_responses = ['Feel free to contact us at 1-800-123-4567 or email us at sales@glazingtech.com.',
                     'If you have any questions, don’t hesitate to contact us at 1-800-123-4567 or email us at sales@glazingtech.com. We’d be happy to help!',
                     'Need more information? Don’t hesitate to contact us at 1-800-123-4567 or email us at sales@glazingtech.com. We’re here to help!']
fallback_response = 'I am sorry, I am not sure I understand. Could you please rephrase your question?'


# Define a function to generate a response to a user's message
def generate_response(message):
    if 'hi' in message or 'hello' in message or 'hey' in message:
        return random.choice(greeting_responses)
    elif 'product' in message or 'glazing' in message or 'technology' in message:
        return random.choice(product_responses)
    elif 'contact' in message or 'help' in message or 'question' in message:
        return random.choice(contact_responses)
    else:
        return fallback_response


# Define a route to handle incoming chatbot requests
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get the user's message from the request body
    message = request.form['message']

    # Generate a response to the user's message
    response = generate_response(message)

    # Return the response to the user
    return {'message': response}


if __name__ == '__main__':
    # Start the server
    app.run()
