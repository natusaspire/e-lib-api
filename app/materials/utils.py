from functools import wraps

from enum import Enum

from flask import jsonify

from app.materials.models import (
    Text,
    Audio,
    Video
)


ENDPOINT_MODELS = {
    'text': Text,
    'audio': Audio,
    'video': Video
}


def validate_endpoint_and_get_model(endpoint_models):
    def callable(function):
        @wraps(function)
        def wrapped(endpoint, *args, **kwargs):
            model = endpoint_models.get(endpoint)

            if not model:
                return jsonify(error=404), 404

            return function(model, *args, **kwargs)

        return wrapped

    return callable


class Order(Enum):
    DATE_ASC = 'date'
    DATE_DESC = '-date'

    RATING_ASC = 'rating'
    RATING_DESC = '-rating'

    @classmethod
    def is_order_valid(cls, order):
        return any(order == item.value for item in cls)

    @classmethod
    def get_order_result(cls, query, model, order):
        order_results = {
            cls.DATE_ASC.value: query.order_by(model.date_and_time),
            cls.DATE_DESC.value: query.order_by(model.date_and_time.desc()),
            cls.RATING_ASC.value: query.order_by(model.rating),
            cls.RATING_DESC.value: query.order_by(model.rating.desc())
        }

        return order_results.get(order)
