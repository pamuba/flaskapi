from flask import Flask, request
import uuid
from db import items, stores

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores":list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id":store_id}
    stores[store_id] = store
    return store, 201

# adding more than one item
@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        # raise KeyError("Store does not exist.")
        return {"message":"Store Not Found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id] = item

    return item, 201

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[store_id]
    except KeyError:
        return {"message":"Item Not Found"}

@app.get('/item')
def get_all_items():
    return {"items":list(item.values())}


@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message":"Store Not Found"}


# delete
# update 



