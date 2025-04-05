from dataclasses import dataclass

@dataclass
class RenderOptions:
    template_id: str
    modifications: dict
    response_type: str
    response_format: str

@dataclass
class SignedUrlOptions:
    template_id: str
    response_format: str
    render_type: str
    modifications: dict
    expires_at: int
