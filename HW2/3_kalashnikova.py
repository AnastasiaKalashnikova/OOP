class TextFile:
    def __init__(self, filename):
        self.filename = filename
        self.content = ""
    
    def write(self, data):
        self.content = data
        return f"Данные записаны в файл {self.filename}"
    
    def read(self):
        return f"Содержимое файла {self.filename}: {self.content}"

class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.records = []
    
    def write(self, data):
        self.records.append(data)
        return f"Данные добавлены в БД {self.dbname}"
    
    def read(self):
        return f"Данные из БД {self.dbname}: {self.records}"

class NetworkResource:
    def __init__(self, url):
        self.url = url
        self.response = ""
    
    def write(self, data):
        self.response = f"Отправлено на {self.url}: {data}"
        return self.response
    
    def read(self):
        return f"Ответ от {self.url}: {self.response}"

#DON'T TOUCH UNDER THE LINE
#______________________________________________________________
def process_data(data_source, data=None):
    if data:
        data_source.write(data)
    return data_source.read()

text_file = TextFile("document.txt")
database = Database("users.db")
network = NetworkResource("http://example.com/api")

print(process_data(text_file, "Новый текст"))
print(process_data(database, {"name": "Иван", "age": 25}))
print(process_data(network, "POST data"))