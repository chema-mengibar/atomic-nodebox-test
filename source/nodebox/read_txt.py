

def load(filename):
    data = ""
    with open(filename, 'r') as myfile:
      data=myfile.read().replace('\n', '')

    return data


def save(filename,content):
    with open(filename, "w") as text_file:
        text_file.write(content)
