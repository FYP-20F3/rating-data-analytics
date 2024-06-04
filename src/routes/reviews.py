from flask import Blueprint
from src.controllers.reviews import analyze_review

# Blueprint for /review route
review_bp = Blueprint('review_bp', __name__)

# Define routes for semantic analysis and fake review detection
@review_bp.route('/analyze-review', methods=['POST'])
def analyze_review_route():
    return analyze_review()

# @review_bp.route('/detect-fake-review', methods=['POST'])
# def detect_fake_review_route():
#     return detect_fake_review()


# @review_bp.route('/detect-abusive-language', methods=['POST'])
# def detect_abusive_language_route():
#     return detect_abusive_language()
