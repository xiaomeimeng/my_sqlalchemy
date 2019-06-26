from flask import Flask, request

from DBUtils.PooledDB import PooledDB
import pymysql

class Config(object):
    """配置文件的加载"""

    # 配置秘钥：项目中的CSRF和session需要用到，还有一些其他的签名算法也要用到
    SECRET_KEY = 'q7pBNcWPgmF6BqB6b5VICF7z7pI+90o0O4CaJsFGjzRsYiya9SEgUDytXvzFsIaR'

    # 开启调试模式
    DEBUG = True


    PYMYSQL_POOL = PooledDB(
        creator=pymysql,  # 使用链接数据库的模块
        maxconnections=6,
        closeable=False,
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='information',  # 链接的数据库的名字
        charset='utf8'
    )

current_app = Flask(__name__)
current_app.config.from_object(Config)


from sql_test import MysqlHelper


@current_app.route('/', methods=['GET', 'POST'])
def index():
    obj = MysqlHelper.fetch_one("select id,name from users where name=%s", "zhangan")
    return obj



if __name__ == '__main__':
    current_app.run(debug=True)



