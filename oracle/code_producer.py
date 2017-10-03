import datetime

start_time = input('请输入开始日期\n')
x = input('请输入需要计算的天数\n')
time_clac = datetime.datetime.strptime(start_time, '%Y-%m-%d')
with open('data.sql', 'w') as f:
    for i in range(int(x)):
        delta = datetime.timedelta(days=1)
        time_clac_next = delta + time_clac
        time_demo_pre = str(time_clac.strftime('%Y-%m-%d'))
        time_demo_next = str(time_clac_next.strftime('%Y-%m-%d'))
        start_code = '''select a.shibiao,a.YHBH,a.TQBH,a.GDJBH,b.zxzygdn - a.zxzygdn YDL from (select shibiao,YHBH,TQBH,GDJBH,zxzygdn from RDJ_TB  where SHIBIAO = TO_DATE(\'%s\','YYYY-MM-DD') ) a,(select shibiao,YHBH,TQBH,GDJBH,zxzygdn from RDJ_TB  where SHIBIAO = TO_DATE(\'%s\','YYYY-MM-DD') ) b where a.yhbh = b.yhbh and a.TQBH = B.TQBH AND a.gdjbh = b.gdjbh;\n''' %(time_demo_pre, time_demo_next)
        time_clac += delta
        #print(time_demo)
        f.write(start_code)