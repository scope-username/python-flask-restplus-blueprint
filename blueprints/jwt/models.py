from flask_restplus import fields

login_request_model = {
    "Username": fields.String(description="EmailID", required=True, example="email@domain.com",
                              type=str),
    "Password": fields.String(description="password", required=True, example="password", type=str)
}

login_response_model = {
    "access_token": fields.String(description="Access Token", example="xxxxxxxxxx"),
    "refresh_token": fields.String(description="Refresh Token", example="xxxxxxxxxx")
}

protected_response_model = {
    "username": fields.String(description="Logged EmailID", example="email@domain.com"),
    "permissions": fields.String(description="User Access", example="A")
}

refresh_response_model = {
    "access_token": fields.String(description="New Access Token", example="xxxxxxxxxx")
}
