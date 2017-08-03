import pymysql

db = pymysql.connect(host = "localhost", port = 8701, user = "root", db = 'job_record')
cursor = db.cursor()
cursor.execute("Drop TABLE IF EXISTS jobs")
sql = """ create table jobs (
          day date,
          xuke float default 0.0,
          Angelia float default 0.0,
          haowang float default 0.0,
          lixiang float default 0.0,
          mc float default 0.0,
          nll float default 0.0,
          wangziqi float default 0.0,
          yfy float default 0.0,
          zxs_miao float default 0.0,
          chaijun float default 0.0,
          hjn float default 0.0,
          Liyuhao float default 0.0,
          mff float default 0.0,
          qsy float default 0.0,
          www float default 0.0,
          zhb float default 0.0,
          CMPG_LAB float default 0.0,
          hqf float default 0.0,
          lzz float default 0.0,
          mql float default 0.0,
          rqy float default 0.0,
          Wangjun float default 0.0,
          zsw float default 0.0,
          hunter_killer float default 0.0 )"""
cursor.execute(sql)
db.close()

