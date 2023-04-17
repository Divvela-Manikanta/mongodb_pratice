from flask import Flask,request,jsonify
from dataclasses_scripts import Info
from validations_script import info_method
from mongo_db_connection import MongoOperations

app  = Flask(__name__)

@app.route("/insert",methods=["POST"])
def to_inser():
    data_to_insert  = request.json
    obj = Info.from_dict(data_to_insert) 
    dict_to_pass = {"full_name":obj.full_name,"age":obj.age,"gender":obj.gender}
    data_from_validation  = info_method(dict_to_pass)
    valid_to_db = MongoOperations(data_from_validation)
    return jsonify(valid_to_db.insert_data())
        
@app.route('/update',methods=["POST"])
def upadate_the_data():
    data_to_update = (request.json)
    obj = Info.from_dict(data_to_update)
    find_obj = MongoOperations(find_data_var=obj.full_name)
    if(find_obj.find_the_user()):
          dict_to_pass_update = {"full_name":obj.full_name,"age":obj.age,"gender":obj.gender}
          obj_update = MongoOperations(update_the_data=dict_to_pass_update)
          return jsonify(obj_update.update_data())
    else:
         return jsonify({"Meassage": f"Data not found with the name {obj.full_name}",
                      "Success": True,
                      "Status":200})
   
@app.route("/delete/<name>")
def data_to_be_deleted(name):
     find_obj = MongoOperations(find_data_var=name)
     if(find_obj.find_the_user()):
          delete_obj = MongoOperations(delete_var=name)
          return jsonify(delete_obj.delete_data())
     else:
         return jsonify({"Meassage": f"Data not found with the name {name}",
                      "Success": True,
                      "Status":200})
  
@app.route("/query",methods=["Post"])
def query_the_documenet():
     qurey_data = dict(request.get_json())
     print(qurey_data)
     query_obj = MongoOperations(query_data=qurey_data)
     return jsonify(query_obj.query_one())
    
@app.route("/bluk",methods=['post'])
def bluk_method():
      bluk_data = (request.get_json())
      user_obj = MongoOperations(bluk_data= bluk_data)
      return jsonify(user_obj.bluk())

if __name__ == "__main__":
    app.run(debug=True)