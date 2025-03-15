from sqlalchemy.orm import Session
from db.models.blog import Blog
from schemas.blog import CreateBlog

def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(title=blog.title,
                slug=blog.slug, 
                content=blog.content,
                author_id=author_id
                )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs

def update_blog_by_id(id: int, blog: CreateBlog, db: Session, author_id: int = 1):
    db_blog = db.query(Blog).filter(Blog.id == id).first()
    if not db_blog:
        return {"error": f"Blog with id {id} does not exist"}
    if not db_blog.author_id == author_id:
        return {"error": "Only author can modify the blog"}
    db_blog.title = blog.title
    db_blog.slug = blog.slug
    db_blog.content = blog.content
    db.add(db_blog)
    db.commit()
    return db_blog

def delete_blog_by_id(id: int, db: Session, author_id: int = 1):
    db_blog = db.query(Blog).filter(Blog.id == id).first()
    if not db_blog:
        return {"error": f"Could not find the blog by {id}"}
    if not db_blog.author_id == author_id:
        return {"error": "Only author can delete the blog"}
    db.delete(db_blog)
    db.commit()
    return {"message": f"Blog with {id} deleted successfully"}
# Compare this snippet from backend/db/repository/blog.py:
