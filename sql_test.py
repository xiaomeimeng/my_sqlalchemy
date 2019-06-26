import pymysql
from infomation import current_app


class MysqlHelper(object):

    @staticmethod
    def open(cursor):
        # 从当前的app中的配置文件中去获取连接池
        POOL = current_app.config["PYMYSQL_POOL"]
        # 链接
        conn = POOL.connection()
        cursor = conn.cursor(cursor=cursor)
        return conn, cursor


    @staticmethod
    def close(conn, cursor):
        """
        关闭数据库连接
        :return:
        """
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    # 处理查找一个的功能，定义成类方法，
    def fetch_one(cls, sql, args=None, cursor=pymysql.cursors.DictCursor):
        conn, cursor = cls.open(cursor)
        if args is None:
            args = []
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        cls.close(conn, cursor)
        return obj

    @classmethod
    def select_multi(cls, args, params=None, cursor=pymysql.cursors.DictCursor):
        """
        查询语句，可以执行多条查询
        :param args:
        :param params:
        :return: 返回元祖res：结果，num查询出行数
        """
        conn, cursor = cls.open(cursor)
        if params is None:
            params = []
        i = 1
        res = {}
        for sql in args:
            num = cursor.execute(sql, params)
            sql_results = cursor.fetchall()
            res['result%s' % i] = sql_results
            res['effect%s' % i] = num
            i += 1
        cls.close(conn, cursor)
        return res



