import json


class Query():

    def __init__(self, file_path='messages.json'):
        """
        Query class, load a json file and api to messages in it
        """
        self.messages = self.load_json_file(file_path)

    def load_json_file(self, file_path):
        """
        Loads json file
        param:
            file_path: string
        """
        d = None
        with open(file_path) as f:
            d = json.load(f)
            return d

    def get_by_tag(self, tag):
        """
        Get messages by tag
        param:
            message: list
            tag: string
        return:
            msgs: list
        """
        msgs = []
        for msg in self.messages:
            if(tag in msg['tags']):
                msgs.append(msg)
        return msgs

    def get_by_priority(self, priority):
        """
        Get messages by priority
        param:
            message: list
            priority: int
        return:
            msgs: list
        """
        msgs = []
        for msg in self.messages:
            if(priority == msg['priority']):
                msgs.append(msg)
        return msgs

    def get_by_tag_priority(self, priority, tag):
        """
        Get messages by priority and tag
        param:
            message: list
            priority: int
            tag: string
        return:
            msgs: list
        """
        msgs = []
        for msg in self.messages:
            if((priority == msg['priority']) and (tag in msg['tags'])):
                msgs.append(msg)
        return msgs

    def get_all(self):
        """
        Get a copy of all messages in json file
        return:
            msgs: list
        """
        return list(self.messages)