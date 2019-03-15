from config import ROUTE_GEN_TOKEN
from lib import api_service


def gen_api_token():
    try:
        data = api_service(route=ROUTE_GEN_TOKEN, method="get")
        return data['token']
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    api_token = gen_api_token()
    print("api_token:{}".format(api_token))
