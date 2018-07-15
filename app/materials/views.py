from flask import (
    Blueprint,
    request,
    jsonify
)

from app import db

from app.materials.models import (
    Text,
    Audio,
    Video
)

from app.materials.utils import (
    Order,
    ENDPOINT_MODELS,
    validate_endpoint_and_get_model
)


materials = Blueprint('materials', __name__)


@materials.route('/<string:endpoint>/<int:material_id>', methods=['GET'])
@validate_endpoint_and_get_model(ENDPOINT_MODELS)
def get_material(model, material_id):
    material = model.query.get(material_id)

    if material:
        return jsonify(material.serialized)

    return jsonify(error=404), 404


@materials.route('/<string:endpoint>', methods=['GET'])
@validate_endpoint_and_get_model(ENDPOINT_MODELS)
def get_materials(model):
    page = request.args.get('page', type=int, default=1)
    per_page = request.args.get('perPage', type=int, default=20)
    search = request.args.get('search', type=str, default='')
    order = request.args.get('order', type=str, default=Order.DATE_DESC.value)

    if not Order.is_order_valid(order):
        return jsonify(error=400), 400

    filter_query = model.query.filter(
        model.title.ilike('%' + search + '%')
    )

    materials = Order.get_order_result(
        filter_query,
        model,
        order
    ).paginate(
        per_page=per_page,
        page=page
    )

    return jsonify({
        'pages': materials.pages,
        'page': page,
        'perPage': per_page,
        'search': search,
        'order': order,
        'total': materials.total,
        'data': [material.serialized for material in materials.items]
    })


@materials.route('/text/add', methods=['POST'])
def add_text():
    data = request.get_json()

    if not data:
        return jsonify(error=400), 400

    title = data.get('title')
    text_content = data.get('textContent')

    if not title or not text_content:
        return jsonify(error=400), 400

    try:
        text = Text(title=title, text_content=text_content)

        db.session.add(text)
        db.session.commit()
    except:
        db.session.rollback()

        return jsonify(error=500), 500

    return jsonify(), 200


@materials.route('/audio/add', methods=['POST'])
def add_audio():
    data = request.get_json()

    if not data:
        return jsonify(error=400), 400

    title = data.get('title')
    url = data.get('url')

    if not title or not url:
        return jsonify(error=400), 400

    try:
        audio = Audio(title=title, url=url)

        db.session.add(audio)
        db.session.commit()
    except:
        db.session.rollback()

        return jsonify(error=500), 500

    return jsonify(), 200


@materials.route('/video/add', methods=['POST'])
def add_video():
    data = request.get_json()

    if not data:
        return jsonify(error=400), 400

    title = data.get('title')
    url = data.get('url')

    if not title or not url:
        return jsonify(error=400), 400

    try:
        video = Video(title=title, url=url)

        db.session.add(video)
        db.session.commit()
    except:
        db.session.rollback()

        return jsonify(error=500), 500

    return jsonify(), 200
