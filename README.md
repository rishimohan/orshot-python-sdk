# Orshot API Python SDK

View on pypi.org: [pypi.org/project/orshot](https://pypi.org/project/orshot/)

## Installation

```
pip install orshot
```

## Usage

If you don't have your API key, get one from [orshot.com](https://orshot.com).

### Initialise

```python
os = orshot.Orshot('YOUR_ORSHOT_API_KEY')
```

### Render from template

```python
response = os.render_from_template({'template_id': 'open-graph-image-1', 'modifications': {'title': 'From python sdk new'}, 'response_type': 'base64', 'response_format': 'png'})
print(response['data'])
```

### Generate signed URL

```python
response = os.generate_signed_url({'template_id': 'open-graph-image-1', 'modifications': {'title': 'From python sdk new'}, 'render_type': 'images', 'response_format': 'png', 'expires_at': 1744276943})
print(response['data'])
```

## Example

### `Base64` response format

```python
import orshot

os = orshot.Orshot('os-he2jdus1cbz1dpt4mktgjyvx')
modifications = {
    'title': 'From Orshot Python SDK',
    'description': 'Create Visuals and Automate Image Generation'
}
response = os.render_from_template({ 
    'template_id': 'open-graph-image-1',
    'modifications': modifications,
    'response_type': 'base64',
    'response_format': 'png'
})
print(response)
```

Base64 output

```
{
    'data': {
        'content': 'data:image/png;base64,iVBORw0KGgoAAA',
        'format': 'png',
        'type': 'base64',
        'responseTime': 3208.03
    }
}
```

### `Binary` response format

```python
from io import BytesIO

import orshot
from PIL import Image

os = orshot.Orshot('os-he2jdus1cbz1dpt4mktgjyvx')
modifications = {
    'title': 'From Orshot Python SDK',
    'description': 'Create Visuals and Automate Image Generation'
}
response = os.render_from_template({ 
    'template_id': 'open-graph-image-1',
    'modifications': modifications,
    'response_type': 'binary',
    'response_format': 'png'
})

with Image.open(BytesIO(response.content)) as im:
    im.save('og.png')
```

This example writes the binary image to the file `og.png`

### `URL` response format

```python
import orshot

os = orshot.Orshot('os-he2jdus1cbz1dpt4mktgjyvx')
modifications = {
    'title': 'From Orshot Python SDK',
    'description': 'Create Visuals and Automate Image Generation'
}
response = os.render_from_template({ 
    'template_id': 'open-graph-image-1',
    'modifications': modifications,
    'response_type': 'url',
    'response_format': 'png'
})
print(response)
```

URL output

```
{
    'data': {
        'content': 'https://storage.orshot.com/00632982-fd46-44ff-9a61-f52cdf1b8e62/images/AuBgAsKzLJl.png',
        'type': 'url',
        'format': 'png',
        'responseTime': 3387.08
    }
}
```

### Signed URL

```python
import orshot

os = orshot.Orshot('os-he2jdus1cbz1dpt4mktgjyvx')
modifications = {
    'title': 'From Orshot Python SDK',
    'description': 'Create Visuals and Automate Image Generation'
}

response = os.generate_signed_url({ 
    'template_id': 'open-graph-image-1',
    'modifications': modifications,
    'render_type': 'images',
    'response_format': 'png',
    'expires_at': 1744276943
})
print(response)
```

Output

```
{
  "data": {
    "url": "https://api.orshot.com/v1/generate/images?expiresAt=1744276943&id=28&templateId=open-graph-image-1&title=From%20python%20sdk%20new&signature=fa4ea0aa4cf05bd9b836be031dccfc26abf41dcc623561ac262c75b658f725f1"
  }
}
```

## render_from_template

Use this function to generate an image.

| argument | required | description |
|----------|----------|-------------|
| `template_id` | Yes | ID of the template (`open-graph-image-1`, `tweet-image-1`, `beautify-screenshot-1`) |
| `modifications` | Yes | Modifications for the selected template. |
| `response_type` | No | `base64`, `binary`, `url` (Defaults to `base64`). |
| `response_format` | No | `png`, `webp`, `pdf`, `jpg`, `jpeg` (Defaults to `png`) |

For available templates and their modifications refer [Orshot Templates Page](https://orshot.com/templates)

## generate_signed_url

Use this function to get a signed URL.

| argument | required | description |
|----------|----------|-------------|
| `template_id` | Yes | ID of the template (`open-graph-image-1`, `tweet-image-1`, `beautify-screenshot-1`) |
| `modifications` | Yes | Modifications for the selected template. |
| `expires_at` | Yes | Expires at time in UNIX timestamp (Integer) |
| `render_type` | No | `images`, `pdfs` (Defaults to `images`). |
| `response_format` | No | `png`, `webp`, `pdf`, `jpg`, `jpeg` (Defaults to `png`) |

## Local development and testing

Install `uv` - https://docs.astral.sh/uv/getting-started/installation/#installation-methods

`uv venv` to create the virtual environment. 

Uninstall before building and installing again

`uv pip uninstall orshot`

Build

`python -m build`

To install the package locally for testing

`uv pip install dist/orshot-0.2.1-py3-none-any.whl`

You can create a `test.py` file with a sample code to render an image.
