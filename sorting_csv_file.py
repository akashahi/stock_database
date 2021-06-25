import pandas as pd


def formatting_date_and_time():
    # this function changes the date and time in one format i.e date/month/year 24hrs
    for i in range(len(csv_file)):
        data = csv_file.date[i]
        # This removes the - and replaces it with / in date
        if '-' in data:
            data = data.replace('-', '/')
        # This removes the am if it is present in time.
        if 'am' in data:
            data = data.replace('am', '')
        # This removes the pm
        if 'pm' in data:
            data = data.replace('pm', '')
            time = data.split(" ")[1]
            if '12:' in time:
                pass
            # Here time which is greater than 12 is replaced to 24 hrs format. i.e 1 pm to 13:00
            else:
                new_time = time.replace(time.split(':')[0], str(12 + int(time.split(':')[0])), 1)
                data = data.replace(time, new_time)
        time = data.split(" ")[1]
        hours = time.split(':')[0]
        # Here if hours is less than 10 and does not contain a preceding zero, then it is added.
        if int(hours) < 10 and '0' not in hours:
            new_time = time.replace(hours, f'0{hours}')
            data = data.replace(time, new_time)
        csv_file.date[i] = data


def sort_the_data():
    # Here data is sorted in asc order based on stock name and then in descending order based on their time.
    csv_file.sort_values(["symbol", 'date'], axis=0,  ascending=[True, False], inplace=True)


def get_first_occurrence():
    try:
        # This functions returns a list containing the first entry of all the stocks.
        list1 = []
        for i in range(len(csv_file) - 1):
            if csv_file.values[i][1] != csv_file.values[i+1][1]:
                list1.append(csv_file.values[i])
        list1.append(csv_file.values[-1])
        return list1
    except Exception as e:
        print(e)


def write_to_excel():
    # This function takes the list and converts it into excel file.
    data_to_write = get_first_occurrence()
    df = pd.DataFrame(data_to_write)
    excel_file = pd.ExcelWriter('sorted_stock_data.xlsx')  # if needed change the result excel file name here.
    df.to_excel(excel_file)
    excel_file.save()


def call_all_function():
    formatting_date_and_time()
    sort_the_data()
    get_first_occurrence()
    write_to_excel()


if __name__ == "__main__":
    # Input file name needs to be changed here.
    csv_file = pd.read_csv('Backtest Copy - Hilega Milega Long, Technical Analysis Scanner (6) (copy).csv')
    call_all_function()
