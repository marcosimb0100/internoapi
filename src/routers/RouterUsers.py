from flask import Blueprint, jsonify, request, send_file
from helpers.HelperUsers import UsuarioHelper

main = Blueprint('usuarios_blueprint', __name__)


@main.route('/', methods=['POST'])
def post_usuario():
    # has_access = Seguridad.verificar_token(request.headers)
    # if not has_access['status'] == 200:
    #     return jsonify(has_access['data']), has_access['status']
    try:
        datos = request.get_json()
        resultado = UsuarioHelper.crear( datos )
        return jsonify(resultado['data']), resultado['status']
    except Exception as ex:
            return jsonify({'mensaje': str(ex), 'datos': {}}), 500