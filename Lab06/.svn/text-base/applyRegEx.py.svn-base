import re

def getRejectedUsers():
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = []
    for line in lines:
        state = ''
        email = re.search(r'[a-zA-Z0-9._-]+@purdue.com',line)
        poh = re.search(r'(\d{3})\D*(\d{3})\D*(\d{4})',line)
        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if len(ns) > 1:
            state = ns[1]
        if poh is None and email is None and state is '':
            reuser.append(name)
    reuser.sort()
    return reuser

def getUsersWithEmails():
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = {}
    for line in lines:
        email = re.search(r'[a-zA-Z0-9._-]+@purdue.com',line)
        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if email is not None:
            reuser.update({name:email.group()})
    return reuser

def getUsersWithPhones():
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = {}
    for line in lines:
        poh = re.search(r'\d{10}|\d{3}-\d{3}-\d{4}|\d{3}\)\s\d{3}-\d{4}',line)

        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if poh is not None:
            poh = re.search(r'(\d{3})\D*(\d{3})\D*(\d{4})',poh.group())
            reuser.update({name:'('+poh.groups()[0]+') '+poh.groups()[1]+'-'+poh.groups()[2]})
    return reuser

def getUsersWithStates():
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = {}
    for line in lines:
        state = ''
        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if len(ns) > 1:
            state = ns[1]
        if state is not '':
            reuser.update({name:state})
    return reuser

def getUsersWithoutEmails():
    invalid = getRejectedUsers()
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = []
    for line in lines:
        email = re.search(r'[a-zA-Z0-9._-]+@purdue.com',line)
        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if email is None:
            if name not in invalid:
                reuser.append(name)
    reuser.sort()
    return reuser

def getUsersWithoutPhones():
    invalid = getRejectedUsers()
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = []
    for line in lines:
        poh = re.search(r'\d{10}|\d{3}-\d{3}-\d{4}|\d{3}\)\s\d{3}-\d{4}',line)

        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if poh is None:
            if name not in invalid:
                reuser.append(name)
    reuser.sort()
    return reuser

def getUsersWithoutStates():
    invalid = getRejectedUsers()
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = []
    for line in lines:
        state = ''
        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if len(ns) > 1:
            state = ns[1]
        if state is '':
            if name not in invalid:
                reuser.append(name)
    reuser.sort()
    return reuser

def getUsersWithCompleteInfo():
    with open('SiteRegistration.txt','r') as file:
        lines = file.readlines()
    reuser = {}
    for line in lines:
        state = ''
        email = re.search(r'[a-zA-Z0-9._-]+@purdue.com',line)
        poh = re.search(r'\d{10}|\d{3}-\d{3}-\d{4}|\d{3}\)\s\d{3}-\d{4}',line)

        ns = re.findall(r'[A-Z][a-z]+..?[a-zA-z]+',line)
        namem = re.match(r'([A-Z][a-z]+)\D*([A-Z][a-z]+)',ns[0])
        if ',' in ns[0]:
            name = namem.groups()[1]+ " " + namem.groups()[0]
        else:
            name = namem.groups()[0]+ " " + namem.groups()[1]
        if len(ns) > 1:
            state = ns[1]
        if poh is not None and email is not None and state is not '':
            poh = re.search(r'(\d{3})\D*(\d{3})\D*(\d{4})',poh.group())
            reuser.update({name:(email.group(),'('+poh.groups()[0]+') '+poh.groups()[1]+'-'+poh.groups()[2],state)})
    return reuser

if __name__ == '__main__':
    pass
