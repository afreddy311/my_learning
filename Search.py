
import os
import fnmatch

def search(file_name, location):
    for root, dirs, files in os.walk(location):
        if n in files:
            print(root)
            print(os.path.join(root, file_name))


def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):

        if name in files:
            result.append(os.path.join(root, name))
    return result


def find3(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


#search('python.exe', 'C:\\')
find_all('python.exe', 'C:\\')

