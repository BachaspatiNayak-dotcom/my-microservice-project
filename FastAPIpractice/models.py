from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped,relationship
from sqlalchemy import String,Integer,ForeignKey


class Base(DeclarativeBase):
    pass

class Emp(Base):

    __tablename__="Emps"

    eid:Mapped[int]=mapped_column(Integer,primary_key=True)
    ename:Mapped[str]=mapped_column(String(30))
    password:Mapped[str]=mapped_column(String(255))
    sal:Mapped[int]=mapped_column(Integer)
    role:Mapped[str]=mapped_column(String(10))
    deptno:Mapped[int|None]=mapped_column(ForeignKey("Depts.did"),nullable=True)

    dept=relationship("Dept")

class Dept(Base):
    __tablename__="Depts"

    did:Mapped[int]=mapped_column(Integer,primary_key=True)
    dname:Mapped[str]=mapped_column(String(10))

    emps=relationship("Emp")
