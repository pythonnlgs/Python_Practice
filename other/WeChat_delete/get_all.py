import os

def listDir(path, list_name):
    """
    :param path: 路径
    :param list_name: path下所有文件的绝对路径名的列表
    :return:
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listDir(file_path, list_name)
        else:
            list_name.append(file_path)
