import os.path
import os
import shutil
import hashlib
import logging
import argparse


parser = argparse.ArgumentParser(description='Script to sync folders.')


parser.add_argument("--source", required=True, type=str)
parser.add_argument("--replica", required=True, type=str)


args = parser.parse_args()

if args.replica.endswith('/'):
    replica = args.replica
else:
    replica = f"{args.replica}/"

if args.source.endswith('/'):
    source = args.source
else:
    source = f"{args.source}/"


logging.basicConfig(filename='sync.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


def get_files_list(folder):
    files = []
    for _, _, file in os.walk(folder):
        files.append(file)
    return files


def sync(source_files, replica_files):
    for s_file in source_files:
        if s_file and s_file not in replica_files:
            logging.info(f"{s_file[0]} not in {replica}. Copying...")
            shutil.copyfile(source+s_file[0], replica+s_file[0])
    for r_file in replica_files:
        if r_file and r_file not in source_files:
            # Delete replica file
            logging.info(f"Deleting {r_file[0]} from {replica}...")
            os.remove(replica + r_file[0])
        else:
            logging.info(f"{r_file[0]} found in both folders. Calculating checksum.")
            s_checksum = md5(source+r_file[0])
            r_checksum = md5(replica+r_file[0])
            if s_checksum != r_checksum:
                logging.info(f"Checksum inequal. Replacing replica file {r_file[0]}")
                os.remove(replica+r_file[0])
                shutil.copyfile(source + r_file[0], replica + r_file[0])
            else:
                logging.info(f"Checksums are the same. Passing.")


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.info(f"Starting sync...")
    a = get_files_list(source)
    b = get_files_list(replica)
    sync(a, b)
