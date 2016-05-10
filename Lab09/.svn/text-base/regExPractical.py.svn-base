import re

def getAddress(sentence):
    result = re.search(r'([a-zA-z]{1}[0-9]{1}[-:]|[0-9]{1}[a-zA-z]{1}[-:]|[0-9]{2}[-:]){5}([a-zA-z]{1}[0-9]{1}|[0-9]{1}[a-zA-z]{1}|[0-9]{2})',sentence)
    if result:
        return result.group()
    else:
        return None
def getElements(url):
    if 'http' == url[0:4]:
        result = re.findall(r'[/]([\w.]+)',url)
        if len(result) != 3:
            return None
        else:
            if '.' not in result[1] and '.' not in result[2] and '_' not in result[1] and '_' not in result[2]:
                return tuple(result)
            else:
                return None
    else:
        return None

def getSwitches(line):
    result = re.findall(r'[\\+]([a-z])\s+([\w/:.]+)',line)
    if result is not None:
        result.sort()
        return result
    else:
        return None