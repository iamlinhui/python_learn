# 读取Properties 文件类
class PropertiesUtils:
    fileName = ''

    def __init__(self, fileName):
        self.fileName = fileName

    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'r', encoding='utf-8')
            properties = {}
            for line in pro_file:
                if line.find('=') > 0:
                    string = line.replace('\n', '').split('=')
                    properties[string[0]] = string[1]
        except Exception as e:
            raise e
        else:
            pro_file.close()
        return properties
