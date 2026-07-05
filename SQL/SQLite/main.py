from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

from sqlalchemy.orm import Session
from database import engine, Base, get_database
import mymodel
import schemas

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.post("/Jobs/", response_model = schemas.JobResponse)
def create_job(job : schemas.JobCreate, db : Annotated[Session, Depends(get_database)]):
    db_job = mymodel.Job(title=job.title, company=job.company)
    db.add(db_job)
    db.commit()
    
    db.refresh(db_job)
    return db_job


@app.get("/Jobs/{job_id}", response_model=schemas.JobResponse)
def read_job(job_id: int, db: Annotated[Session, Depends(get_database)]):
    job = db.query(mymodel.Job).filter(mymodel.Job.id == job_id).first()
    if not job:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Job Not Found"
        )
    return job


@app.delete("/DeleteJob/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id : int, db : Annotated[Session, Depends(get_database)]):
    job = db.query(mymodel.Job).filter(mymodel.Job.id == job_id).first()
    
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job Not Found")
    
    db.delete(job)
    db.commit()
    return None


@app.put("/Jobs/{job_id}", response_model=schemas.JobResponse)
def update_job(
    job_id : int, 
    update_job : schemas.JobCreate, 
    db : Annotated[Session, Depends(get_database)]):
    job = db.query(mymodel.Job).filter(mymodel.Job.id == job_id).first()
    
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job Not Found")
    
    job.title = update_job.title
    job.company = update_job.company
    db.commit()
    db.refresh(job)
    return job