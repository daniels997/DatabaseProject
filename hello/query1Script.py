import cx_Oracle

def query1Script(x, date1, date2, y, z):

    date1 = str(date1) + ' 23:59:59'
    date2 = str(date2) + ' 23:59:59'

    for row in cur.execute("select sq.Stock_name from ( select Stock.Stock_name, count(t_mentions.tweet), count(r_mentions.reddit_post) from stock join instance_of_stock on stock.ticker = instance_of_stock.stock join stock_instance on stock_instance.instance_ID = instance_of_stock.stock_instance join t_mentions on stock.ticker = t_mentions.stock join r_mentions on stock.ticker = r_mentions.stock where stock_volume >  :x and Instance_Date between to_TIMESTAMP(:date1, 'YYYY-MM-DD HH24:MI:SS.FF') AND to_TIMESTAMP(:date2, 'YYYY-MM-DD HH24:MI:SS.FF') group by Stock.Stock_name having count(t_mentions.tweet) >= :y and count(r_mentions.reddit_post) >= :z) sq", [x, date1, date2, y, z]):
        print(row)

    print(x, ' ', date1, ' ', date2, ' ', y, ' ', z)
    #query database with these things
    #display data
