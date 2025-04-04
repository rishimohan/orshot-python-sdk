from dataclasses import dataclass

@dataclass
class RenderOptions:
    template_id: str
    modifications: dict
    response_type: str
    response_format: str
