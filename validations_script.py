from marshmallow import Schema,fields,ValidationError,validate

class Validdata(Schema):
        full_name = fields.Str(required=True)
        age = fields.Int(required=True)
        gender = fields.Str(required=True)



def info_method(val):
    try:
         person = Validdata()
         valid_to_return = person.load(val)
         return valid_to_return
    except ValidationError as err:
        return(err.messages)