import sys, os, subprocess
from concurrent.futures import ThreadPoolExecutor

def RcloneLink(path):
    link = subprocess.run([
        "rclone", 
        "link", 
        path], 
        encoding='utf-8',
        stdout=subprocess.PIPE)
    return link.stdout
def RcloneList(path):
    filelist = subprocess.run([
        "rclone",
        "lsf",
        path],
        encoding='utf-8',
        stdout=subprocess.PIPE)
    return filelist.stdout.strip().split("\n")

path = " ".join(sys.argv[1:])
files = RcloneList(path)

links = []

files = [os.path.join(path,fl) for fl in files]
with ThreadPoolExecutor() as executor:
    results = executor.map(RcloneLink, files)
    for result in results:
        links.append(result.strip())

print("\n".join(links))
