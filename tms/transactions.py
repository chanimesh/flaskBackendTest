from flask import (
    Blueprint, request, jsonify
)

from tms.db import get_db

bp = Blueprint('transactions', __name__, url_prefix='/transactions')


@bp.route('/all', methods=['GET'])
def all_transactions():
    db = get_db()
    cr = db.execute(
        'SELECT * FROM transactions')
    data = cr.fetchall()
    result = []
    for row in data:
        result.append(dict(row))
    return jsonify(result)
