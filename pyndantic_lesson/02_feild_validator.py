from pydantic import BaseModel, validator, ValidationError,EmailStr,field_validator
from typing import Annotated


class Patient(BaseModel):
    name:str
    age:int 
    Email:EmailStr
# validator for mail
    @field_validator("Email")
    @classmethod
    def mail_validator(cls,value):
      valid_domains=['hdfc.com', 'icici.com']
      dom_name=value.split('@')[-1]
      if dom_name not in valid_domains:
          raise ValueError(f"Invalid email domain. Valid domains are: {', '.join(valid_domains)}")
      return value


#validator for name 

    @field_validator('name')
    @classmethod
    def name_validator(cls,value):
        return value.upper()
#validator for age 
    @field_validator('age')
    @classmethod
    def age_validator(cls,value):
        if 0< value <120:
            return value
        else:
           raise ValueError("age should be in between 0 to 120")




def update_patient_data(patient=Patient):
    print(patient.name)
    print(patient.age)
    print(patient.Email)

patient_info={'name': "John Doe", 'age': 30, 'Email': "abc@hdfc.com"}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
