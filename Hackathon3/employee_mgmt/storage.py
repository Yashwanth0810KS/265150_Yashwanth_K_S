import pickle
import os

class Storage:

    def __init__(self, file_path="employee.pkl"):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, "wb") as file:
            pickle.dump(data, file)

    def load(self):
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "rb") as file:
                return pickle.load(file)
        except ValueError:
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
