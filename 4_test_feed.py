from config import API_TOKEN
from lib import wrap_api


if __name__ == '__main__':
    device_info = {'device_id': "66762742687",
                   'install_id': "66088143957",
                   'openudid': '3275465180871399',
                   'uuid': '187604370269819'}

    # 获取首页feed
    print(wrap_api("v1/feed",
                   {'count': 6, 'type': 0, 'max_cursor': 0, 'min_cursor': -1, 'pull_type': 2},
                   device_info=device_info,
                   token=API_TOKEN))
