def read_file(filename):
    print('reading a file')
    try:
        f = open(filename)
        content = f.read()
        f.close()
    finally:
        print('Final')

    return content


def way_better(filename):
    print('reading a file better')
    with open(filename) as f:
        return f.read()


def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)

if __name__ == '__main__':
    # print(read_file('requirements.txt'))
    write_to_file('requirements_2.txt', '\nNew line\n', mode='a')
    print(way_better('requirements_2.txt'))