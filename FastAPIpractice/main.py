from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import joinedload
from pwdlib import PasswordHash
# from database import SessionLocal
from schemas import *
from models import *
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone
import time

app=FastAPI()

"""allowing cross origin requests"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"]
)

"""creating object from PasswordHash class"""
password_hash=PasswordHash.recommended()

"""loding contents from .env file"""
# load_dotenv()

# def get_db():
#     db=SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()


security=HTTPBearer()


@app.get("/")
def greet():
    return "welcome to my fastapi application"


def get_current_user(credentials=Depends(security)):
    token=credentials.credentials

    user_details=jwt.decode(
        token,
        security_key,
        algorithms=algorithm
    ) 

    return user_details


# @app.post("/create_emp/")
# def create_emp(emp:EmpCreate,db=Depends(get_db)):

#     hashed_pw=password_hash.hash(emp.password)

#     db_emp=Emp(
#         ename=emp.ename,
#         password=hashed_pw,
#         sal=emp.sal,
#         role=emp.role,
#         deptno=emp.deptno,

#     )
#     db.add(db_emp)
#     db.commit()

#     return "emp created successfully"

# @app.patch("/update_emp/{id}")
# def update_emp(id:int,emp:EmpUpdate,db=Depends(get_db),user_details=Depends(get_current_user)):
#     if user_details["role"]=="ceo":
#         emp_db=db.get(Emp,id)

#         if not emp_db:
#             raise HTTPException(
#                 status_code=404,
#                 detail="student not found"
#             )
#         emp_db.sal=emp.sal
#         emp_db.role=emp.role
#         emp_db.deptno=emp.deptno

#         db.commit()

#         return "emp updated successfully"

#     return "You have no authorisation to update employee data"


# @app.delete("/del_emp/")
# def delete_emp(id:int,db=Depends(get_db)):
#     db_emp=db.get(Emp,id)

#     db.delete(db_emp)
#     db.commit()
#     return "emp deleted successfully"


# @app.post("/create_dept/")
# def create_dept(dept:DeptCreate,db=Depends(get_db)):

#     db_dept=Dept(
#         did=dept.did,
#         dname=dept.dname
#     )

#     db.add(db_dept)
#     db.commit()

#     return "dept created successfully"


"""login functionality"""

security_key=os.getenv("security_key")
algorithm="HS256"


# @app.post("/login/")
# def login(data:Login,db=Depends(get_db)):
#     db_emp=db.query(Emp).filter(Emp.ename==data.username).first()

#     if db_emp is None:
#         return "invalid username"

#     if not password_hash.verify(data.password,db_emp.password):
#         return "wrong password"

#     payload={
#         "id":db_emp.eid,
#         "ename":db_emp.ename,
#         "role":db_emp.role,
#         "sal":db_emp.sal,
#         "deptno":db_emp.deptno,
#         "exp":datetime.now(timezone.utc)+timedelta(minutes=5)
#     }

#     token=jwt.encode(payload,security_key,algorithm=algorithm)

#     return {"msg":"login successfull","access_token":token}

"""role based access control"""

# @app.get("/emp_details/")
# def emp_details(db=Depends(get_db),user_details=Depends(get_current_user)):
#     if user_details["role"]=="ceo":
#         emps=db.query(Emp).all()

#     elif user_details["role"]=="emp":
#         user_id=user_details["id"]
#         emp=db.get(Emp,user_id)
#         emps=[emp]
#     else:
#         dept_no=user_details["deptno"]
#         emps=db.query(Emp).filter(Emp.deptno==dept_no).all()

#     return [
#         {
#             "eid":emp.eid,
#             "ename":emp.ename,
#             "sal":emp.sal,
#             "deptno":emp.deptno
#         } for emp in emps
#     ]

"""creating custom middleware"""

@app.middleware("http")
async def time_calculator(request,call_next):
    st=time.time()
    response=await call_next(request)
    et=time.time()
    print(et-st)
    return response

"""solving N+1 query problem by join"""

# @app.get("/emp_dept/")
# def emp_dept(db=Depends(get_db)):
#     emps=db.query(Emp).options(
#         joinedload(Emp.dept)
#     )
#     return [
#         {
#             "ename":emp.ename,
#             "sal":emp.sal,
#             "dname":emp.dept.dname if emp.dept else None,
#             "role":emp.role
#         }  for emp in emps
#     ]

# @app.get("/abc/")
# async def demo(db=Depends(get_db)):
#     emps=await db.query(Emp).all()
#     return emps

# @app.get("/emp_details/")
# def emp_details(db=Depends(get_db)):
#     emps=db.query(Emp).all()

#     return [
#         {
#             "eid":emp.eid,
#             "ename":emp.ename,
#             "sal":emp.sal,
#             "deptno":emp.deptno
#         } for emp in emps   ]

# @app.get("/dept_details/")
# def dept_details(db=Depends(get_db)):
#     depts=db.query(Dept).all()

#     return [
#         {
#             "ID":dept.did,
#             "dname":dept.dname
#         } for dept in depts
#     ]

@app.get("/emp_details/")
def emp_details():
    return "hello from fastapi"