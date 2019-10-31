from flask_restplus import fields

namespace1_service2_request_data_model = {
    "Title": fields.String(description="Title of the data", required=True, example='John Smith', type=str),
    "Description": fields.String(description="Description of the data", required=True, example='Its working.', type=str)
}

namespace1_service2_response_data_model = {
    "Message": fields.String(example='John Smith', type=str),
    "Description": fields.String(example='Its working.', type=str)
}

error_response_data_model = {
    "Message": fields.String(description="Title of the data", required=True, example='John Smith', type=str),
    "Description": fields.String(description="Description of the data", required=True, example='Its working.', type=str)
}