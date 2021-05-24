from flask import Blueprint
from src.http.controllers.auth import login, logout, key

authRouter = Blueprint('auth', __name__, url_prefix='/api/auth')


authRouter.route('/login', endpoint='login', methods=['POST'])(login.login_ctrl)
authRouter.route('/key-renew', endpoint='key-renew', methods=['POST'])(key.regenerate_key_ctrl)
authRouter.route('/logout', endpoint='logout', methods=['POST'])(logout.logout_ctrl)