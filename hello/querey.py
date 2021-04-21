import cx_Oracle


#this is how to connect to oracle. place this above the calls to execute queries.
cx_Oracle.init_oracle_client(lib_dir=r"C:\\Program Files\\instantclient_19_10")
CONN_INFO = {
            'host': 'oracle.cise.ufl.edu',
            'port': 1521,
            'user': 'fox.nbrian',
            'psw': 'Tga20379',
            'sid': 'orcl'
            }
CONN_STR = '{user}/{psw}@{host}:{port}/{sid}'.format(**CONN_INFO)
con = cx_Oracle.connect(CONN_STR)
cur = con.cursor()
cur.execute("alter session set NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF'")


print("---query 1---")
#What stocks have a volume above x between date1 and date2 that were mentioned in
#y amount of times in Reddit and z amount of times in Twitter?
#input x, date1, date2, y, z

#test values
x = 64000000
date1 = '2018-03-26 23:59:59'
date2 = '2019-03-27 23:59:59'
y = 10
z = 10

for row in cur.execute("select sq.Stock_name from ( select Stock.Stock_name, count(t_mentions.tweet), count(r_mentions.reddit_post) from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on stock.ticker = t_mentions.stock join r_mentions on stock.ticker = r_mentions.stock where stock_volume >  :x and Instance_Date between to_TIMESTAMP(:date1, 'YYYY-MM-DD HH24:MI:SS.FF') AND to_TIMESTAMP(:date2, 'YYYY-MM-DD HH24:MI:SS.FF') group by Stock.Stock_name having count(t_mentions.tweet) >= :y and count(r_mentions.reddit_post) >= :z) sq", [x, date1, date2, y, z]):
    print(row)

print("\n---query 2---")
#What top 10 stocks have lost the most from x date to y date? 
#(decreased in value more than the other stocks in our database)

#test values
x = '2018-03-26 23:59:59'
y = '2019-03-27 23:59:59'

for row in cur.execute("select stock_name, loss from (select Stock.Stock_name, min(Instance1.Stock_Open - Instance2.Stock_Close) Loss from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance  instance1 on instance1.instance_ID = instance_of_stock.stock_instance join stock_instance  instance2 on instance2.instance_ID= instance_of_stock.stock_instance  where instance1.Instance_Date between to_TIMESTAMP(:x, 'YYYY-MM-DD HH24:MI:SS.FF') AND to_TIMESTAMP(:y, 'YYYY-MM-DD HH24:MI:SS.FF') group by stock.stock_name order by Loss) where rownum <= 10", [x,y]):
    print(row)


print("\n---query 3---")
#What was the opening price of a ticker symbol x on this date y and has a mention by z user on twitter.

#test values
x = 'GME'
y = '2015-02-09 00:00:00.00'
z = 'mando2250'

for row in cur.execute("select stock_instance.stock_open from instance_of_stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on instance_of_stock.stock = t_mentions.stock join posts on t_mentions.tweet = posts.tweet where instance_of_stock.stock = :x and stock_instance.instance_date = to_TIMESTAMP(:y, 'YYYY-MM-DD HH24:MI:SS.FF') and posts.twitter_user = :z", [x,y,z]):
    print(row)


print("\n---query 4---")
#What stocks have made at least x% in y amount of time?
#(Did a stock go up 200% in 2 days?)

#test values
x = 200

for row in cur.execute("with indexed_stocks as (select rank () over (partition by instance_of_stock.stock order by stock_instance.instance_date) rankid, instance_of_stock.stock as stockn, stock_instance.instance_date, stock_instance.stock_open, stock_instance.stock_close from instance_of_stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance), stock_change as (select stock1.stockn, (100*(stock2.stock_close - stock1.stock_open)/stock1.stock_open) percentage_change from indexed_stocks stock1 join indexed_stocks stock2 on stock1.rankid = stock2.rankid + 2 and stock1.stockn = stock2.stockn) Select stockn, max(percentage_change) from stock_change where stock_change.percentage_change >= :x group by stockn", [x]):
    print(row)


print("\n---query 5---")
#What are the amounts of Twitter mentions of each stock that had a
#higher closing price than opening price on date z?

#test values
z = '2015-02-09 00:00:00.00'

for row in cur.execute("select instance_of_stock.stock, count(T_Mentions.tweet) number_of_tweets from instance_of_stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on instance_of_stock.stock = t_mentions.stock where stock_instance.instance_date = to_TIMESTAMP(:z, 'YYYY-MM-DD HH24:MI:SS.FF') and (stock_instance.stock_close - stock_instance.stock_open) > 0 group by instance_of_stock.stock order by instance_of_stock.stock", [z]):
    print(row)
    

print("\n---query 6---")
#shows hows all of the stocks that have a certain growth more than x % 
#(gained the most from the other stocks in our database)

#test values
x = 5

for row in cur.execute("select distinct stock.stock_name from  stock  join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on instance_of_stock.stock_instance = stock_instance.instance_id where stock_instance.percent_change > :x order by  stock.stock_name", [x]):
    print(row)


print("\n---query 7---")
#show the twitter tuples

for row in cur.execute("select stock.stock_name, count(t_mentions.tweet) from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on instance_of_stock.stock_instance = stock_instance.instance_id join t_mentions on t_mentions.stock = stock.ticker group by rollup (stock.stock_name) order by stock.stock_name"):
    print(row)
exit(0)
