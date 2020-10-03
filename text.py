



def connect(method):
    def getCategory ():
        return 5

    def getProduct ():
        return 3

    api = {
        "getCategory": getCategory(),
        "getProduct": getProduct(),
    }

    return api[method]
    
print(connect("getCategory"))

x = {
    "a": connect,
    "b": 2,
}

