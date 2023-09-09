# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.

import os
import stripe

from flask import Flask, redirect, render_template

app = Flask(__name__,template_folder='templates')

stripe.api_key = 'sk_test_tR3PYbcVNZZ796tH88S4VQ2u'

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/success")
def success():
  return render_template('success.html')

@app.route("/cancel")
def cancel():
  return redirect('/')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'inr',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:4242/success',
    cancel_url='http://localhost:4242/cancel',
  )

  return redirect(session.url, code=303)

if __name__== '__main__':
    app.run(port=4242)