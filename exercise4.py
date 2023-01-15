http_request= int(input("Enter number the request !!"))
# http_status = 789

match http_request:
    case 200 |201:
        print("The status is succes")
    case 404:
        print("The status is page not found")
    case 500:
        print("The status is Bad request (server)")
    case default:
        print("the status Unknown")