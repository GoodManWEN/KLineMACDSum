import baostock as bs
import datetime

def cut_time(ktime:str, mode , radio):
    ktime = datetime.datetime.strptime(ktime, "%H:%M") # 
    morning = datetime.datetime.strptime('09:30', "%H:%M")
    noon = datetime.datetime.strptime('13:00', "%H:%M")
    noon0 = datetime.datetime.strptime('11:30', "%H:%M")
    evening = datetime.datetime.strptime('15:00', "%H:%M")

    assert (morning <= ktime <= noon0) or (noon <= ktime <= evening) 

    if mode=="st":
        if ktime >= noon:
            delta = ktime - noon + datetime.timedelta(seconds=7200)
        else:
            delta = ktime - morning
    elif mode == 'ed':
        if ktime <= noon0:
            delta = noon0 - ktime + datetime.timedelta(seconds=7200)
        else:
            delta = evening - ktime

    total_seconds = delta.total_seconds()
    div = int(total_seconds // (int(radio) * 60))
    if mode == 'st':
        return div
    else:
        return -div

def get_baostock_data(stocknum , radio , sttime , edtime , stdate , eddate):
    forw_table = {
        '5': 11,
        '15': 11,
        '30': 22,
        '60': 45,
        'd': 180,
        'w': 1000,
        'm': 3000,
    }

    try:
        assert radio in forw_table.keys()

        if int(stocknum) >= 600000:
            stocknum = f"sh.{stocknum}"
        else:
            stocknum = f"sz.{stocknum}"

        start_date = datetime.datetime.strptime(stdate, "%Y-%m-%d") + datetime.timedelta(days= -forw_table[radio])
        start_date = datetime.datetime.strftime(start_date , "%Y-%m-%d")
        end_date = eddate

        assert datetime.datetime.strptime(end_date, "%Y-%m-%d") >= datetime.datetime.strptime(start_date, "%Y-%m-%d")

        lg = bs.login()
        assert lg.error_code == '0'
        rs = bs.query_history_k_data_plus(stocknum,
                                          "date,code,close",
                                          start_date=start_date, 
                                          end_date=end_date, 
                                          frequency=radio, 
                                          adjustflag="3",)
        assert rs.error_code == '0'

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        bs.logout()
        if radio in ['d','w','m']:
            return data_list
        # else
        if sttime == '09:30' and edtime == '15:00':
            return data_list

        # else
        # cutting will be done in final return after compute
        return data_list
    except:
        return False

def compute_macd(data_list):
    last_close = float(data_list[0][-1])
    ema_12 = [last_close,] 
    ema_26 = [last_close,]
    diff = [0,]
    dea = [0,]
    bar = [0,]

    ema_12_last = last_close
    ema_26_last = last_close
    diff_last = 0
    dea_last = 0
    bar_last = 0

    for new_row in data_list[1:]:
        new_last_close = float(new_row[-1])
        # compute
        ema_12_last = ema_12_last * 11 / 13 + new_last_close * 2 / 13
        ema_26_last = ema_26_last * 25 / 27 + new_last_close * 2 / 27
        diff_last = ema_12_last - ema_26_last
        dea_last = dea_last * 8 / 10 + diff_last * 2 / 10
        bar_last = 2 * (diff_last - dea_last)
        # append
        ema_12.append(ema_12_last)
        ema_26.append(ema_26_last)
        diff.append(diff_last)
        dea.append(dea_last)
        bar.append(bar_last)
        #
        last_close = new_last_close

    return bar

def cutting(stocknum , radio , sttime , edtime , stdate , eddate , data_list , bar):
    for index , item in enumerate(data_list):
        if item[0] == stdate:
            break
    bar = bar[index:]
    if radio in ['d','w','m']:
        return bar

    # else
    front = cut_time(sttime, 'st' , radio)
    back = cut_time(edtime, 'ed' , radio)
    if back != 0:
        bar = bar[front:back]
    else:
        bar = bar[front:]
    return bar

def statics(final_list):
    red = 0
    green = 0
    for i in final_list:
        if i >= 0:
            red += i
        else:
            green += i 
    sum_ = red + green
    return round(red,3) , round(green,3) , round(sum_,3)

async def wrapmain(loop , pool ,*args):
    try:
        data_list = await loop.run_in_executor(pool , get_baostock_data , *args)
        assert data_list
        bar = compute_macd(data_list)
        args_1 = list(args)
        args_1.append(data_list)
        args_1.append(bar)
        final_list = cutting(*args_1)
        return statics(final_list)
    except:
        return False

if __name__ == "__main__":
    pass