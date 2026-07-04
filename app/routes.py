from flask import Blueprint, render_template, jsonify
from app.logger import configure_logger

logger = configure_logger()


main = Blueprint("main", __name__)


@main.route("/")
def home():
    logger.info("Home page requested")
    return render_template("index.html")


@main.route("/about")
def about():
    logger.info("About page requested")
    return render_template("about.html")


@main.route("/health")
def health():
    logger.info("Health endpoint requested")
    return jsonify({
        "status": "healthy"
    }), 200