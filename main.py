from sqlalchemy import create_engine,MetaData,Integer,String,FLOAT,DATE,Column,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

engine= create_engine("postgresql://postgres:12345@localhost:5432/db_1",echo=False)
a=engine.connect()
Session=sessionmaker(bind=engine)
session=Session()
base=declarative_base()
class company(base):
    __tablename__='Company'
    company_id=Column(Integer,primary_key=True)
    company_name=Column(String)
    location=Column(String)
class user(base):
    __tablename__='User'
    user_id=Column(Integer,primary_key=True)
    user_name=Column(String)
    company_id = Column(Integer, ForeignKey('Company.company_id'))
    joining_date=Column(DATE)
base.metadata.create_all(engine)
company1=company(company_id=1001,company_name="benz",location="germany")
company2=company(company_id=1002,company_name="audi",location="france")
company3=company(company_id=1003,company_name="rollsroyce",location="usa")
company4=company(company_id=1004,company_name="maruti",location="india")
company5=company(company_id=1005,company_name="toyota",location="india")
user1=user(user_id=41,user_name="rohit",company_id=1005,joining_date="2017-02-12")
user2=user(user_id=42,user_name="pique",company_id=1004 ,joining_date="2017-05-18")
user3=user(user_id=43,user_name="fati" ,company_id=1003, joining_date="2017-09-12")
user4=user(user_id=44,user_name="jong",company_id=1002,joining_date="2017-08-26")
user5=user(user_id=45,user_name="gavi",company_id=1001,joining_date="2017-09-29")
session.add_all([company1,company2,company3,company4,company5])
session.add_all([user1,user2,user3,user4,user5])
session.commit()
a=session.query(company)
for company in a:
    print(company.company_name)
a=session.query(company).filter(company.company_id==1003)
for company in a:
    print(company.company_name,company.location)
