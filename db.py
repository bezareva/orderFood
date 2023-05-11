import json


class DB:

    @classmethod
    def get_categories(cls):
        with open("data/menu.json", "r") as f:
            data = json.loads(f.read())
        return data.keys()

    @classmethod
    def get_items_by_category(cls, category):
        with open("data/menu.json", "r") as f:
            data = json.loads(f.read())
        submenues = data[category]
        return submenues

    @classmethod
    def get_menu(cls):
        with open("data/menu.json", "r") as f:
            data = json.loads(f.read())
        return data


    @classmethod
    def get_item_by_id(cls, item_id):
        with open("data/menu.json", "r") as f:
            data = json.loads(f.read())
        return data



    @classmethod
    def get_current_order(cls):
        with open("data/order.json", "r") as f:
            data = json.loads(f.read())
        return data

    @classmethod
    def update_current_order(cls, data):
        new_order = json.dumps(data, indent=4)
        with open("data/order.json", "w") as f:
            f.write(new_order)
        pass

