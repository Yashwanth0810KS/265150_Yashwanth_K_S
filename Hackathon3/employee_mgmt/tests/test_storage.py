import unittest
import os
import sys
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from storage import Storage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_employee.pkl"
        self.storage = Storage(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save(self):
        data = [{"id": "1", "name": "Yash", "department": "Engineering"}]

        self.storage.save(data)

        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, "rb") as file:
            loaded_data = pickle.load(file)
            self.assertEqual(loaded_data, data)

    def test_load_no_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        loaded_data = self.storage.load()

        self.assertEqual(loaded_data, [])

    def test_load_with_invalid_data(self):
        with open(self.file_path, "wb") as file:
            file.write(b"invalid data")

        loaded_data = self.storage.load()

        self.assertEqual(loaded_data, [])

    def test_load_existing_file(self):
        data = [{"id": "2", "name": "Karna", "department": "Engineering"}]
        self.storage.save(data)

        loaded_data = self.storage.load()

        self.assertEqual(loaded_data, data)


if __name__ == "__main__":
    unittest.main()
