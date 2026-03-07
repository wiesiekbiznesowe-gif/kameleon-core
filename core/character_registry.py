import os
import json

CHARACTER_DIR = os.path.join(os.path.dirname(__file__), "characters")


class CharacterRegistry:

    def __init__(self):
        self.characters = {}
        self.load_characters()

    def load_characters(self):

        if not os.path.exists(CHARACTER_DIR):
            return

        for file in os.listdir(CHARACTER_DIR):

            if file.endswith(".json"):

                path = os.path.join(CHARACTER_DIR, file)

                with open(path, "r") as f:

                    data = json.load(f)

                    cid = data["character_id"]

                    self.characters[cid] = data

    def get(self, character_id):

        return self.characters.get(character_id)

    def all(self):

        return list(self.characters.values())
