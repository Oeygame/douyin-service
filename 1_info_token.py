from config import ROUTE_INFO_TOKEN
from lib import api_service




def get_token_info(token):
    try:
        data = api_service(route=ROUTE_INFO_TOKEN, method="get", token=token)
        return data
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    print(get_token_info("08338ef0b578ef208dfacbce2a9db2e0"))
