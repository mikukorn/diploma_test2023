import json

class Scenario:
    def __int__(self, name, description, steps, status):
        self.scanario_id = id
        self.name = name
        self.description = description
        self.steps = steps
        self.status = status
        self.success_message

    def success_message(self):
        print(f'Кейс {self.name} создан')

    @classmethod
    def form_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
