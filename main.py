import time
from pymongo import MongoClient
from urllib import quote_plus
import json
from clint.textui import colored

#source = mongodb://app_dev_user:t{;as]N8mUk:27af@54.233.189.15:27017/s2_chat_development
#target = mongodb://app_prod_user:$G32Zf2d7G'j]]>}@54.233.189.15:27017/s2_chat_production

"""
Get collections from source
"""

def import_docs():
    #source
    uri = "mongodb://%s:%s@%s" % (quote_plus("username"), quote_plus("password"), "host")
    source_client = MongoClient(uri)
    source_db = source_client.s2_chat_development
    source_answers = source_db.answers

    #target
    target_db = source_client.s2_chat_production
    target_answers = target_db.answers

    for a in target_answers.find():
        source_answers.insert_one(a)

def export_docs():
    """
    Export to a document
    """
    uri = "mongodb://%s:%s@%s" % (quote_plus("username"), quote_plus("password"), "host")
    source_client = MongoClient(uri)
    source_db = source_client.s2_chat_production
    source_answers = source_db.answers
    
    target_file = open("file_name_init" + time.strftime("%d-%m-%Y") + ".json", "wb")
    backup_string, docs_count = "", 0
    for a in source_answers.find():
        backup_string += str(a)
        docs_count += 1
    target_file.write(backup_string)
    target_file.close()

    print(colored.green("Success!"))
    print("->" + colored.blue(str(docs_count)) + " documents imported")

if __name__ == "__main__":
    export_docs()
