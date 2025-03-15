from typing import Optional
from pydantic import BaseModel, field_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @field_validator('slug', mode='before')
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get('title').replace(' ', '-')

        return values
    
class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class UpdateBlog(CreateBlog):
    pass