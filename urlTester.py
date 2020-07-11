import requests as r 
import sys

url = sys.argv[1]
filename = sys.argv[2]

def url_tester(url, filename):
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        url_verifier = "{}{}".format(url, line.rstrip("\n"))
        response = r.get(url_verifier)
        if response.status_code != 404:
            print("{} | {}".format(url_verifier, response.status_code))

if __name__ == "__main__":
    url_tester(url, filename)


