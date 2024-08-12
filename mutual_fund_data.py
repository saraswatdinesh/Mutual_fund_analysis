import pandas as pd

class MutualFundDataGeneration:
    def __init__(self):
        self.monthly_sip_amount = 1000
        self.avg_rate_of_return = 12
        self.time_period_fund = 240
        self.sip_increase_pct = 10
        self.frequency_of_increase_flag = 'N'
        self.frequency_of_increase = 12
        self.expense_ratio = (0.5/100)
    
    def generate_data(self, monthly_sip_amount=None, avg_rate_of_return=None, time_period_fund=None, 
                    frequency_of_increase_flag=None, sip_increase_pct=None, frequency_of_increase=None ):
        # Use instance variables if parameters are not provided
        monthly_sip_amount = monthly_sip_amount if monthly_sip_amount is not None else self.monthly_sip_amount
        avg_rate_of_return = avg_rate_of_return if avg_rate_of_return is not None else self.avg_rate_of_return
        time_period_fund = time_period_fund if time_period_fund is not None else self.time_period_fund
        sip_increase_pct = sip_increase_pct if sip_increase_pct is not None else self.sip_increase_pct
        frequency_of_increase_flag = frequency_of_increase_flag if frequency_of_increase_flag is not None else self.frequency_of_increase_flag
        frequency_of_increase = frequency_of_increase if frequency_of_increase is not None else self.frequency_of_increase
        expense_ratio = self.expense_ratio

        months = [i for i in range(1, time_period_fund + 1)]
        sip_amount = []
        current_sip_amount = monthly_sip_amount
        period_interval = frequency_of_increase
        increment_pct = sip_increase_pct

        if frequency_of_increase_flag == 'Y':
            for period in range(time_period_fund):
                sip_amount.append(current_sip_amount)

                if (period + 1) % period_interval == 0:
                    current_sip_amount += current_sip_amount * (increment_pct / 100)
        else:
            sip_amount = [current_sip_amount for _ in range(time_period_fund)]

        # Handle potential mismatch in lengths
        if len(sip_amount) < len(months):
            sip_amount += [sip_amount[-1]] * (len(months) - len(sip_amount))
        elif len(sip_amount) > len(months):
            sip_amount = sip_amount[:len(months)]


        #Calculate the final invested SIP amount after deducting the TER 
        post_ter_investment_sip = []
        for i in range(len(sip_amount)):
            post_ter_investment_sip.append(sip_amount[i]*(1-expense_ratio))
        # Calculate the avg_mnthly_ror 

        avg_mnthly_ror = (((1+(avg_rate_of_return/100))**(1/12)) - 1)*100
        #avg_mnthly_ror = avg_rate_of_return/12
        mutual_fund_df = pd.DataFrame({
            'months': months,
            'sip_amount': sip_amount,
            'post_ter_investment_sip': post_ter_investment_sip,
            'avg_mnthly_ror': [avg_mnthly_ror]*len(months)
        })

        return mutual_fund_df


def main():
    monthly_sip_amount = 2000
    avg_rate_of_return = 12
    time_period_fund = 240   # in months
    sip_increase_pct = 10
    frequency_of_increase_flag = 'N'
    frequency_of_increase = 12   # monthly only, like each year or every two years, etc.
    
    data_obj = MutualFundDataGeneration()
    data = data_obj.generate_data()
    print(data)

if __name__ == "__main__":
    main()
