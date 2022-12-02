from fastapi import FastAPI,Depends,status,Response,HTTPException
from database import engine
import models
import schemas
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List

app=FastAPI()

models.Base.metadata.create_all(bind= engine)

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get('/')
# def abc():
#     return {'data':{'name':'aslam'}}

# @app.get('/blog/{id}')
# def abc(id:int):
#     return {'data':id}



# @app.post('/blog')
# def create_blog(request:Blog):
#     return {'data':f"Blog created with title as {request.title}"}

@app.post('/blog')
def create(request:schemas.BlogBase,db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs   

@app.get('/blog/{id}', status_code=200,response_model=schemas.BlogBase,tags=['blogs'])
def show(id, response: Response, db: Session = Depends (get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:

        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with the id {id} is not available")

        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with this {id} not exist"}
    return blog

