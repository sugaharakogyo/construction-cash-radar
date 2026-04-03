import stripe
from flask import Flask, request

app = Flask(__name__)

# 本番ではRenderのEnvironmentに入れるのが安全
stripe.api_key ="sk_test_xhhUbwLqLkcNGGNJvdF2jH5oP90tY4gc"
endpoint_secret ="whsec_OKnVudQrYN7ZgyBSC6RNuV3LEJLJLhXA"

@app.route("/", methods=["GET"])
def home():
    return "webhook server running", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        return str(e), 400

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_details = session.get("customer_details", {}) or {}
        email = customer_details.get("email")

        print("支払い成功:", email)

        if email:
            with open("pro_users.txt", "a", encoding="utf-8") as f:
                f.write(email + "\n")

    return "OK", 200
