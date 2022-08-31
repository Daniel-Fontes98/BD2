from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://GrupoBD2:3108112B52@projeto.wzyxukn.mongodb.net/?retryWrites=true&w=majority')
db = client['db_name']