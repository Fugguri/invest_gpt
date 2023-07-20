import json 


class Json_worker():
    def __init__(self, path) -> None:
        self.path = path
        
    def get_config(self):
        file = open(self.path, "r")
        data = json.load(file)
        return data

    def get_channels(self):
        file = open(self.path, "r")
        data = json.load(file)
        return data["channels"]
    
    def set_new_channel_for_subscribe(self,group_id,group_name):
        try:
            file = open(self.path, "r")
            data = json.load(file)
            new_data = {group_id: group_name}
            data["channels"].update(new_data)
            with open(self.path, "w") as file:
                json.dump(data, file)
            return True
        except Exception as ex:
            print(ex)
            return False
        
    def delete_channel_for_subscribe(self,group_id):
        try:
            file = open(self.path, "r")
            data = json.load(file)
            data["channels"].pop(group_id)
            with open(self.path, "w") as file:
                json.dump(data, file)
            return True
        except Exception as ex:
            print(ex)
            return False
