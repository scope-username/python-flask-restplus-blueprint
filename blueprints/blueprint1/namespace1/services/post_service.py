def post_service(title, description):
    return {
        "Message": "Hello " + title + "! This is 'POST' response of the service in blueprint1-namespace1.",
        "Description": description
    }
