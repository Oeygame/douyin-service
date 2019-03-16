## 抖音在线签名服务

>最新算法基于抖音19年初的android 2.9.0~3.9.0版本，请使用豌豆荚下载指定版本

> 任何疑问请发邮件到：[vsdouyin@yandex.com](vsdouyin@yandex.com)

### 第一步
创建一个私有的授权token，用于以后的所有操作

+ 点击 [http://sign.vsdouyin.com/api/token/gen/](http://sign.vsdouyin.com/api/token/gen/) 直接创建
+ 粘贴 token到文件`config.py` 的`API_TOKEN`配置项
+ 使用命令`python3 1_info_token.py` 查看token的剩余可用次数 

### 第二步
+ 使用命令`python3 2_gen_device.py` 生成设备值

### 第三步
+ 使用命令`python3 3_test_as_cp_mas.py`测试as\cp\mas签名

## 第四步
+ 使用其他python文件测试具体功能

