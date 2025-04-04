import requests
from orshot.constants import (
    ORSHOT_SOURCE,
    ORSHOT_API_VERSION,
    ORSHOT_API_BASE_URL,
    DEFAULT_RESPONSE_TYPE,
    DEFAULT_RESPONSE_FORMAT
)
from orshot.types import RenderOptions
from orshot.exceptions import APIException, BadRequestException

class Orshot:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get_base_url(self):
        return f"{ORSHOT_API_BASE_URL}/{ORSHOT_API_VERSION}"
    
    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def render_from_template(self, render_options: RenderOptions):
        template_id = render_options.get('template_id')
        modifications = render_options.get('modifications')
        response_type = render_options.get('response_type', DEFAULT_RESPONSE_TYPE)
        response_format = render_options.get('response_format', DEFAULT_RESPONSE_FORMAT)

        endpoint_url = f"{self._get_base_url()}/generate/images/{template_id}"

        data = {
            'source': ORSHOT_SOURCE,
            'modifications': modifications,
            'response': {
                'type': response_type,
                'format': response_format
            }
        }

        response = requests.post(endpoint_url, headers=self._get_headers(), json=data)

        if response.status_code == 200:
            if response_type == "base64" or response_type == "url":
                return response.json()
            else:
                return response
        elif response.status_code == 400:
            error_response = response.json().get('error')

            raise BadRequestException(error_response)
        else:
            raise APIException(f"An error occurred while generating an image. Status code: {response.status_code}. Error: {response.json().get('error')}")
