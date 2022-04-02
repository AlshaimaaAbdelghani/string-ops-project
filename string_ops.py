
def repeated_substring(s):
    try:
        lst = []
        for i in s:
            if i not in lst:
                lst.append(i)
        r_str = "".join(lst)
        #print(r_str)
        l = len(r_str)
        counter = 0
        for i in range(0, len(s), l):
            if s[i] == r_str[0]:
                counter += 1
            else:
                r_str = s
        tup = (r_str, counter)
        return tup
    except Exception as e:
        print("In repeated substring, there´s an error called: {}, please Handle it!".format(e))


#simple string matching
def solve(a, b):
    try:
        a = a.lower()
        b = b.lower()
        if a == b:
            return True
        elif '*' in a:
            count = 0
            while '*' in a:
                count += 1
                if count > 1:
                    return False
                else: break
            x = a.find('*')
            if a.replace('*', '') == b:
                return True
            else:
                lst = []
                for i in b:
                    if i not in a:
                        lst.append(i)
                if lst == []:
                    for i in range(x, len(b)):
                        if b[i] != a:
                            lst.append(b[i])
                #print(lst)
                a = a.replace('*', ''.join(lst))
                #print(a)
                if a == b:
                    return True
                else:
                    return False
        else:
            return False
    except Exception as e:
        print("In simple string matching, there´s an error called: {}, please Handle it!".format(e))


def is_palindrome(s):
    try:
        s = s.lower()
        if len(s) == 1:
            return True
        elif len(s) % 2 == 0:
            ind = int((len(s) / 2))
            # print(ind)
            x = s[:ind]
            # print(x)
            y = s[ind:]
            # print(y)
            if x == y[::-1]:
                return True
            else:
                return False
        elif len(s) % 2 != 0:
            ind = int((len(s) / 2))
            # print(ind)
            x = s[:ind]
            # print(x)
            y = s[ind + 1:]
            # print(y)
            if x == y[::-1]:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print("In is_palindrom function, there´s an error called: {}, please Handle it!".format(e))


def find_nth_occurrence(substring, string, occurrence=1):
    try:
        count = 0
        for i in range(len(string)):
            if string[i: i+len(substring)] == substring:
                count += 1
                if count == occurrence:
                    return i
        else:
            return -1
    except Exception as e:
        print("in find_nth_occurrence function, there´s an error called: {}, please Handle it!".format(e))
