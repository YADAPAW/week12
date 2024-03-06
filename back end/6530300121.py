import certifi 
from pymongo.mongo_client import MongoClient 
 
client = MongoClient("mongodb+srv://yadapaw:yadapaw@cluster0.iiwr0te.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where()) 
     
def showall_table(collection): 
    print(f'found {collection.count_documents({})} records') 
    all_students = collection.find() 
    for std in all_students: 
        print(std) 
 
def insert_table(collection): 
    id = input("Input student id:") 
    name = input("Input fullname:") 
    major = input("Input major:") 
    gpa = input("Input gpa:") 
    gpa = float(gpa) 
    try: 
        collection.insert_one({ "_id":id, 
                                "fullname":name, 
                                "major":major, 
                                "gpa":gpa 
                                }) 
    except Exception as e: 
        print(e) 
 
def select_update_table(collection): 
    print("Which column do you want to update?") 
    print("Choose 1 : fullname") 
    print("Choose 2 : major") 
    print("Choose 3 : gpa") 
 
    choose = int(input("Please select: ")) 
    where_id = input("Where ID? : ") 
 
    if choose == 1: 
        new_fullname = input("Please enter new fullname: ") 
        update_table(collection, "fullname", new_fullname, where_id) 
    elif choose == 2: 
        new_major = input("Please enter new Major: ") 
        update_table(collection, "major", new_major, where_id) 
    elif choose == 3: 
        new_gpa = float(input("Please enter new gpa : ")) 
        update_table(collection, "gpa", new_gpa, where_id) 
 
def update_table(collection, title_name, new_value, where): 
    try: 
        myquery = {"_id" : where} 
        newvalues = {"$set" : {title_name : new_value}} 
        result = collection.update_one(myquery, newvalues) 
        if result.modified_count > 0: 
            print("Update successfully!") 
        else: 
            print("No document was updated. Check your 'where' condition.") 
    except Exception as e: 
        print(f"Error: {e}") 
 
def delete_table(collection): 
    where = input("Where is ID? : ") 
    try: 
        result = collection.delete_one({"_id" : where}) 
        if result.deleted_count > 0: 
            print("Delete succesful!") 
        else: 
            print("No document found for deletion.") 
    except Exception as e: 
        print(f"Error : {e}") 
 
try: 
    client.admin.command('ping') 
    print("Pinged your deployment. You successfully connected to MongoDB!") 
    db = client["students"] 
    collection = db["std_info"] 
    while True: 
        print("===MENU===") 
        print("1: show all records") 
        print("2: insert record") 
        print("3: update record") 
        print("4: delete record") 
        print("5: exit") 
        choice = input("Please choose: ") 
        choice = int(choice) 
        if choice == 1: 
            showall_table(collection) 
        elif choice == 2: 
            insert_table(collection) 
        elif choice == 3: 
            select_update_table(collection) 
        elif choice == 4: 
            delete_table(collection) 
        elif choice==5: 
            break 
     
except Exception as e: 
    print(e) 
finally: 
    client.close()