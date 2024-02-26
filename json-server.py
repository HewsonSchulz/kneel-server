import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status
from views import get_all_orders, get_single_order, create_order


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] != 0:
                response_body = get_single_order(url["pk"])
                return (
                    self.response(response_body, status.HTTP_200_SUCCESS.value)
                    if response_body
                    else self.response(
                        "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
                    )
                )

            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_POST(self):
        """Handle POST requests from a client"""

        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            content_len = int(self.headers.get("content-length", 0))
            request_body = self.rfile.read(content_len)
            request_body = json.loads(request_body)
            order = create_order(request_body)
            if order:
                return self.response(
                    json.dumps(order), status.HTTP_201_SUCCESS_CREATED.value
                )
            else:
                return self.response("", status.HTTP_500_SERVER_ERROR.value)

        else:
            return self.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )


def main():
    host = ""
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
