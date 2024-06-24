def http_status(status):
    match status:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        
        # this is the default go-to
        # if other cases don't match
        case _:
            return "Not Implemented Yet"

four_oh_four = http_status(404)
print(four_oh_four)

err = http_status(203)
print(err)