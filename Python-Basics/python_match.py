# match statement compares a value to serveral different conditions until one is met
#alternative to if else statement

http_status = 200

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 501: #or statement
        print("Server Error")
        print("Internal Server Error")
    case _: #default:
        print("Unknown Status")