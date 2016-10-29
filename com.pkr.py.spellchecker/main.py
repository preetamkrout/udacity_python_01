import urllib.request
import urllib.parse

def read_text():
    input_file = open("./input_file.txt")
    content = input_file.read()
    input_file.close()
    check_profanity(content)

def check_profanity(text_test):
    profanity_checker_url = "http://www.purgomalum.com/service/containsprofanity?text="
    query = profanity_checker_url + urllib.parse.quote(text_test.encode("utf8"))
    print(query)
    req = urllib.request.Request(query)
    with urllib.request.urlopen(req) as response:
        isCurse = response.read()
        print(isCurse)
    # print(conn)
    # isCurse = conn.read()
    # print(isCurse)
    # conn.close()


read_text()
