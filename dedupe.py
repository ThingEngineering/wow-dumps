import hashlib
import os
import os.path
import sys
import time


BUFFER_SIZE = 64 * 1024
LANGUAGES = ['deDE', 'esES', 'esMX', 'frFR', 'itIT', 'koKR', 'ptBR', 'ptPT', 'ruRU', 'zhCN', 'zhTW']


def main():
    start = time.time()

    hashes = {}
    total_bytes = 0
    for filename in os.listdir('enUS'):
        sha1, bytes_read = hash_file(os.path.join('enUS', filename))
        hashes[filename] = sha1
        total_bytes += bytes_read

    end = time.time()

    print(f'enUS: hashed {total_bytes / 1024 / 1024:,.1f}MiB in {end - start:.3f}s')

    for dirname in LANGUAGES:
        start = time.time()
        dupe_bytes = 0
        total_bytes = 0

        for filename in os.listdir(dirname):
            filepath = os.path.join(dirname, filename)
            sha1, bytes_read = hash_file(filepath)
            total_bytes += bytes_read

            if filename in hashes:
                if sha1 == hashes[filename]:
                    dupe_bytes += bytes_read
                    os.remove(filepath)
            else:
                print(f'{dirname}: file "{filename}" not in enUS')

        end = time.time()

        print(f'{dirname}: hashed {total_bytes / 1024 / 1024:,.1f}MiB in {end - start:.3f}s, {dupe_bytes / 1024 / 1024:,.1f}MiB of duplicates')

def hash_file(filename):
    bytes_read = 0
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break

            sha1.update(data)
            bytes_read += len(data)
    
    return sha1.hexdigest(), bytes_read


if __name__ == '__main__':
    main()
