from pydantic import BaseModel
from typing import Literal


class EmpCreate(BaseModel):
    ename:str
    password:str
    sal:int
    role:str
    deptno:Literal[100,200,300,400,None]

class EmpUpdate(BaseModel):
    sal:int
    role:str
    deptno:Literal[100,200,300,400]

class DeptCreate(BaseModel):
    did:int
    dname:str

class Login(BaseModel):
    username:str
    password:str