from config import ROUTE_INFO_TOKEN
from lib import api_service




def get_token_info(token):
    try:
        data = api_service(route=ROUTE_INFO_TOKEN, method="get", token=token)
        return data
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    print(get_token_info("cb6ad0353d850dc420624de472b58940"))
