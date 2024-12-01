import pickle
from src.dto.staff_public_dto import StaffPublicDTO
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import OneHotEncoder
from typing import List


class NearestNeighborsModel:
    def __init__(self, data: List[StaffPublicDTO], n_neighbors=10) -> None:
        self.data = data
        self.n_neighbors = n_neighbors
        self.encoder = OneHotEncoder(handle_unknown='ignore')
        self.nn = NearestNeighbors(n_neighbors=self.n_neighbors, metric='euclidean')
        self.encoded_data = None
        self.columns = self.get_columns()


    def get_columns(self) -> list:
        return [field.name for field in StaffPublicDTO.__dataclass_fields__.values()]


    def fit(self) -> None:
        data_matrix = [[getattr(row, col) for col in self.columns] for row in self.data]
        self.encoded_data = self.encoder.fit_transform(data_matrix).toarray()
        self.nn.fit(self.encoded_data)


    def find_nearest_neighbors(self, input_data: StaffPublicDTO) -> list:
        input_data = [getattr(input_data, col, 'None') for col in self.columns]
        encoded_input_data = self.encoder.transform([input_data]).toarray()
        _, indices = self.nn.kneighbors(encoded_input_data)
        nearest_neighbors = [self.data[idx] for idx in indices[0]]
        return nearest_neighbors


    def add_data(self, new_data: List[StaffPublicDTO]) -> None:
        self.data.extend(new_data)
        self.fit()


    def save_model(self, file_path) -> None:
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)


    @staticmethod
    def load_model(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)


# model = NearestNeighborsModel(data)
# model.fit()

# model.save_model('model.pkl')
# loaded_model = NearestNeighborsModel.load_model('model.pkl')
# nearest_neighbors = loaded_model.find_nearest_neighbors(input_data)