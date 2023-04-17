from pymongo import MongoClient,InsertOne,DeleteOne,UpdateOne,ReplaceOne


client = MongoClient('localhost',27017)
db = client.project2
collection = db.document

class MongoOperations:

    def __init__(self,data_need_to_insert=None,find_data_var=None,update_the_data = None,delete_var = None,query_data=None,bluk_data=None) -> None:
        self.data_need_to_insert = data_need_to_insert
        self.find_data_var = find_data_var
        self.update_the_data = update_the_data
        self.delete_var= delete_var
        self.query_data = query_data
        self.bluk_data = bluk_data
    
    def insert_data(self):
        dict_to_insert = {"full_name":self.data_need_to_insert['full_name'],"age":self.data_need_to_insert['age'],"gender":self.data_need_to_insert['gender']}
        response = collection.insert_one(dict_to_insert)
        if response.acknowledged:
            return ({"Meassage":"Data is inserted successfully",
                      "Success": True,
                      "Status":200})
        else:
            return ({"Meassage":"Data is not inserted successfully",
                      "Success": False,
                      "Status":500})
    def find_the_user(self):
        out = collection.find_one({"full_name":self.find_data_var})
        if out== None:
            return False
        else:
            return True
    def update_data(self):
        dict_to_update = {"full_name":self.update_the_data['full_name'],"age":self.update_the_data['age'],"gender":self.update_the_data['gender']}
        collection.update_one({"full_name":dict_to_update["full_name"]},{"$set":{"age":dict_to_update["age"],"gender":dict_to_update['gender']}})
        return ({"Message":"Data is sucessfully updated",
                      "Success": True,
                      "Status":200,
                      "Updated_data":collection.find_one({"full_name":dict_to_update["full_name"]},{'_id':0})})
    
    def delete_data(self):
        delete_obj = collection.delete_one({"full_name":self.delete_var})
        return ({"Message":"Data is sucessfully deleted",
                      "Success": True,
                      "Status":200,
                     })
    

    def query_one(self):
        dict_to_query = (self.query_data)
        dist_keys = list((self.query_data.keys()))
        dist_keys.remove('operation')
        list_app = []
        for key in dist_keys:
            if key == 'full_name':
                list_app.append({"full_name":dict_to_query[key]})
            if key == 'age':
                list_app.append({"age":dict_to_query[key]})
            if key == 'gender':
                list_app.append({"gender":dict_to_query[key]})
            
            if dict_to_query['operation'] =='or':
                data = collection.find({},{"$or": list_app})
                return_list =[]
                for x in data:
                        return_list.append(x)
                if len(return_list)!=0:
                    return return_list
                else:
                    return  {"Message":"Their is no data as per query",
                             "Success": True,
                            "Status":200,}
            
            if dict_to_query['operation'] =='and':
                    data = collection.find({"full_name":self.query_data["full_name"],"age":self.query_data["age"]})
                    return_list =[]
                    for x in data:
                            return_list.append(x)
                    if len(return_list)!=0:
                        return return_list
                    else:
                        return  {"Message":"Their is no data as per query",
                             "Success": True,
                            "Status":200,}
            if dict_to_query['operation'] =='like':
                data = collection.find({"full_name": {"$regex": self.query_data['full_name']}},{"_id":0})
                return_list =[]
                for x in data:
                    return_list.append(x)
                if len(return_list)!=0:
                    return return_list
                else:
                    return  {"Message":"Their is no data as per query",
                             "Success": True,
                            "Status":200,}
        

    def bluk(self):
        list_pass = []
        for opration in self.bluk_data:

            if opration['operation'] =='update':
                list_pass.append(UpdateOne({"full_name":opration['full_name']},{"$set":{"age":opration['age']}}))
            if opration['operation'] =='insert':
                list_pass.append(InsertOne({"full_name":opration['full_name'],"age":opration['age'],"gender":opration['gender']}))
            if opration['operation'] =='delete':
                list_pass.append(DeleteOne({"full_name":opration['full_name']}))
        data = collection.bulk_write(list_pass)
        return ({"Message":"Data is sucessfully performed bulk operation",
                      "Success": True,
                      "Status":200,
                     })
        



