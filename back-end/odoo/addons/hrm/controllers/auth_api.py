from odoo import http
from odoo.http import request

class AuthAPI(http.Controller):

    @http.route('/api/auth/login', type='json', auth='none', methods=['POST'], csrf=False)
    def login(self, **kwargs):

        db = kwargs.get('db')
        login = kwargs.get('login')
        password = kwargs.get('password')

        if not all([db, login, password]):
            return {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": 400,
                    "message": "Bad Request: Missing database, login, or password."
                }
            }

        try:
            uid = request.session.authenticate(db, login, password)
            
            if uid:
                return {
                    "jsonrpc": "2.0",
                    "id": None,
                    "result": {
                        "uid": uid,
                        "session_id": request.session.sid,
                        "message": "Login successful"
                    }
                }
            else:
                return {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": 401,
                        "message": "Authentication failed: Invalid login or password."
                    }
                }

        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": 500,
                    "message": f"An unexpected error occurred: {str(e)}"
                }
            }