import httpx
import pandas as pd
import os

def main():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://www.benzinga.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
        }

    sdate = input('enter start date: ')
    edate = input('enter end date: ')

    url = f'https://api.benzinga.com/api/v2.1/calendar/dividends?token=1c2735820e984715bc4081264135cb90&parameters[date_from]={sdate}&parameters[date_to]={edate}&parameters[date_sort]=ex&pagesize=1000'
    response = httpx.get(url, headers=headers)

    data = response.json()['dividends']

    df = pd.DataFrame(columns=['Ex_date','Ticker','Company','Payment_per_year','Dividend','Yield','Announced','Record','Payable'])
    for obj in data:
        o = {}
        o['Ex_date'] = obj['ex_dividend_date']
        o['Ticker'] = obj['ticker']
        o['Company'] = obj['name']
        o['Payment_per_year'] = obj['frequency']
        o['Dividend'] = float('0'+obj['dividend'])
        o['Yield'] = float('0' + obj['dividend_yield'])
        o['Announced'] = obj['date']
        o['Record'] = obj['record_date']
        o['Payable'] = obj['payable_date']
        new_df =pd.DataFrame(o, index=[0])
        df = pd.concat([df, new_df], axis=0)

    df['Announced'] = pd.to_datetime(df['Announced'])
    df['Ex_date'] = pd.to_datetime(df['Ex_date'])
    df['Payable'] = pd.to_datetime(df['Payable'])
    df['Record'] = pd.to_datetime(df['Record'])

    file_name = input('enter file name: ')
    file_name = 'output/'+file_name
    if os.path.exists(f'{file_name}.csv'):
        df = pd.concat([pd.read_csv(f'{file_name}.csv', parse_dates=['Announced', 'Ex_date', 'Payable', 'Record']), df], axis=0)
        
    df.drop_duplicates().to_csv(f'{file_name}.csv', index=False)

    ##Settings
    start_day_offset = 0
    end_day_offset = 3

    for val in df.Record.unique():
        start_date = (val + pd.Timedelta(days=start_day_offset))
        end_date = (val + pd.Timedelta(days=end_day_offset))
        date = str(val).split('T')[0]
        output_path = 'output/Records/'+date.replace('-', '_')+'.csv'
        output_df = df[(df['Record'] >= start_date) & (df['Record'] <= end_date)]
        if os.path.exists(output_path):
            output_df = pd.concat([pd.read_csv(output_path, parse_dates=['Announced', 'Ex_date', 'Payable', 'Record']), output_df], axis=0)
        
        
        output_df.drop_duplicates().to_csv(output_path, index=False)

if __name__ == '__main__':
    main()