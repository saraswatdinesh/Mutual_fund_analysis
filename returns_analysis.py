from bse_scraper import webScrapper, YahooFinanceData
from mutual_fund_data import MutualFundDataGeneration
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties


pd.options.display.float_format = '{:.2f}'.format


def final_calculations(sip_amount,yearly_rate_of_return,period_in_months,increment_sip_flag,increment_frequency,increment_percentage):
# Build the final dataframe. 
    mfdg_obj = MutualFundDataGeneration()
    mf_data = mfdg_obj.generate_data(sip_amount,yearly_rate_of_return,period_in_months,increment_sip_flag,increment_frequency,increment_percentage)
    
    # Now get the returns data for the number of years of intended period
    url = "https://finance.yahoo.com/quote/%5EBSESN/history/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACAmBcx-zko10K-Q2XBcMk35C4KO6GkkqcoC3RP9v5ra2qcxOjr3IgUNfBhsUgCIC9aN2SLvgRCOQEl3VI9JlDI0e8_iYjWus2rap9plE8WGKcs80R9mrQuIweJQ_Z5TNroINNblLN_EDWo0TaNbuKZKgpoIbzoKkAEWxFzxGtnQ&period1=867728700&period2=1722457285&frequency=1mo"
    scrapper_obj = webScrapper()
    soup = scrapper_obj.scrape_link(url)
    finance_data_obj = YahooFinanceData(soup)
    finance_data = finance_data_obj.parse_table()
    past_returns_data = finance_data_obj.monthly_returns(finance_data)[:period_in_months].sort_values(by ='dates', ascending= True).reset_index(drop=True)
    ## Now get the rows only for the past period

    merged_df = pd.concat([mf_data,past_returns_data], axis = 1 )


    # Now we have the data we can calculate the return 
    fund_values = []
    current_fund_value = 0

    for i in range(len(merged_df)):
        # Update the current fund value based on the return on that month. 
        current_fund_value *= (1 + merged_df.loc[i,'return']/100)

        # Add the SIP amount to the current fund. 
        current_fund_value += merged_df.loc[i,'post_ter_investment_sip']

        fund_values.append(current_fund_value)

    avg_ror_returns = []
    current_fund_value = 0

    for i in range(len(merged_df)):
        current_fund_value *= (1 + merged_df.loc[i,'avg_mnthly_ror']/100)
        current_fund_value += merged_df.loc[i,'post_ter_investment_sip']
        avg_ror_returns.append(current_fund_value)

    merged_df['fund_value'] = fund_values
    merged_df['invested_amount'] = merged_df['sip_amount'].cumsum()
    merged_df['avg_based_fund_value'] = avg_ror_returns
    #print(merged_df)
    return merged_df

def plot_graphs(data,message_1= "", message_2="", message_3 = "", message_4 =  ""):
    data = data 
    sns.set_theme()
    
    sns.lineplot(data= data, x = "months", y = "invested_amount", label="Invested Amount", color = "blue")
    sns.lineplot(data= data, x = "months", y = "fund_value", label="BSE Returns", color = "green")
    sns.lineplot(data= data, x = "months", y = "avg_based_fund_value", label="MF Avg Returns", color = "orange")
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
    plt.text(x=0.5, y=0.9, s=message_1, fontsize=12, ha='center', va='center', transform=plt.gca().transAxes, fontweight = 'semibold')
    plt.text(x=0, y=0.8, s=message_2, fontsize=10, ha='left', va='center', transform=plt.gca().transAxes, fontweight = 'medium')
    plt.text(x=0, y=0.75, s=message_3, fontsize=10, ha='left', va='center', transform=plt.gca().transAxes, fontweight = 'medium')
    plt.text(x=0, y=0.70, s=message_4, fontsize=10, ha='left', va='center', transform=plt.gca().transAxes,fontweight='medium')

    plt.xlabel("Period(in Months)", fontweight = 'semibold')
    plt.ylabel("Value", fontweight ='semibold')
    plt.title("Self Investment vs Mutual Fund Investment", fontweight = 'bold')
    font_properties = FontProperties(weight='bold')
    legend = plt.legend(title = "Legend",loc='lower right')
    legend.get_title().set_fontproperties(font_properties)
    plt.show()

def get_sip_details():
    while True:
        try:
            sip_amount_input = input("Enter the SIP amount (or type 'exit' to quit): ")
            if sip_amount_input.strip().lower() == 'exit':
                print("Exiting the function.")
                return None
            sip_amount = float(sip_amount_input)
            if sip_amount <= 0:
                raise ValueError("SIP amount must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    while True:
        try:
            period_input = input("Enter the investment period in months (or type 'exit' to quit): ")
            if period_input.strip().lower() == 'exit':
                print("Exiting the function.")
                return None
            period_in_months = int(period_input)
            if period_in_months <= 0:
                raise ValueError("Investment period must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    while True:
        try:
            rate_input = input("Enter the yearly average rate of return (in %) (or type 'exit' to quit): ")
            if rate_input.strip().lower() == 'exit':
                print("Exiting the function.")
                return None
            yearly_rate_of_return = float(rate_input)
            if yearly_rate_of_return < 0:
                raise ValueError("Yearly rate of return cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    increment_sip = None
    while increment_sip not in ['Y', 'N']:
        increment_sip = input("Do you want to increment the SIP amount over time? (Y/N) (or type 'exit' to quit): ").strip().upper()
        if increment_sip == 'EXIT':
            print("Exiting the function.")
            return None
        if increment_sip not in ['Y', 'N']:
            print("Invalid input: Please enter 'Y' for Yes or 'N' for No.")

    increment_details = None

    if increment_sip == 'Y':
        while True:
            try:
                increment_period_input = input("Enter the period after which SIP should be incremented (in months) (or type 'exit' to quit): ")
                if increment_period_input.strip().lower() == 'exit':
                    print("Exiting the function.")
                    return None
                increment_period = int(increment_period_input)
                if increment_period <= 0:
                    raise ValueError("Increment period must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                increment_percentage_input = input("Enter the percentage of increase in SIP (or type 'exit' to quit): ")
                if increment_percentage_input.strip().lower() == 'exit':
                    print("Exiting the function.")
                    return None
                increment_percentage = float(increment_percentage_input)
                if increment_percentage <= 0:
                    raise ValueError("Percentage increase must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        increment_details = {
            'increment_period': increment_period,
            'increment_percentage': increment_percentage
        }

    # Return all details as a dictionary
    return {
        'sip_amount': sip_amount,
        'period_in_months': period_in_months,
        'yearly_rate_of_return': yearly_rate_of_return,
        'increment_sip': increment_sip,
        'increment_details': increment_details
    }


def main():
    
    user_inputs= get_sip_details()
    if user_inputs :
        sip_amount = user_inputs.get('sip_amount',1000)
        period_in_months = user_inputs.get('period_in_months',240)
        yearly_rate_of_return = user_inputs.get('yearly_rate_of_return',10)
        increment_sip_flag = user_inputs.get('increment_sip','N')
        increment_frequency = None
        increment_percentage = None
        if increment_sip_flag.strip().upper() =='Y':
            increment_frequency = user_inputs.get('increment_details').get('increment_period',12)
            increment_percentage = user_inputs.get('increment_details').get('increment_percentage',12)
        print(user_inputs)
        
        data = final_calculations(sip_amount,yearly_rate_of_return,period_in_months,increment_sip_flag,increment_frequency,increment_percentage)
        #print(data)


        # Calculate the final Amount after exit load and Expense ration and also deduct the LTCG gain along with it.
        avg_exit_load = (1/100)
        market_final_value = round(data.iloc[-1]['fund_value'],0)
        invested = round(data['sip_amount'].sum(),0)
        mf_final_value = round(data.iloc[-1]['avg_based_fund_value'],0)
        mf_final_after_exit_load = round(mf_final_value*(1-avg_exit_load),0)
        mf_earnings = round((data['sip_amount'].sum() - data['post_ter_investment_sip'].sum()) + (mf_final_value - mf_final_after_exit_load ),0)
        

        print(f"The money invested over_investement period is {int(invested)} ")
        print(f"The mutual fund value after the investement period is {int(mf_final_value)}")
        print(f"The money credit to your account after {period_in_months} months is {int(mf_final_after_exit_load)}")
        print(f"Total money earned by MF institute in different fees is {int(mf_earnings)}")


        if increment_frequency is not None:
            message_1 = f"Invested {int(invested):,} over {period_in_months} months with {int(sip_amount):,} SIP per month and an {increment_percentage}% increase every {increment_frequency} month "
            message_2 = f"Net Value in BSE index self invested : {int(market_final_value):,}"
            message_3 = f"Net Value after MF expected ROR (deducting fees) : {int(mf_final_after_exit_load):,}"
            message_4 = f"MF collected fees : {int(mf_earnings):,}"
            plot_graphs(data,message_1,message_2, message_3, message_4)
        else:
            message_1 = f"Invested {int(invested):,} over {period_in_months} months with {int(sip_amount)} SIP "
            message_2 = f"Net Value in BSE index self invested : {int(market_final_value):,}"
            message_3 = f"Net Value via MF houses post 0.5% expense ratio and exit load of 1% deduction : {int(mf_final_after_exit_load):,}"
            message_4 = f"MF earnings in over the period : {int(mf_earnings):,}"
            plot_graphs(data,message_1,message_2, message_3, message_4)            


    else:
        print("Function exited without any details getting captured")


if __name__ == "__main__":

    main()