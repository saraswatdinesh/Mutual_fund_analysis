# Mutual_fund_analysis
Compare the Mutual Fund Returns against traditional self-investing in index funds. 

# Is Mutual funds via SIP the best way to accumulate wealth or is it just a marketing strategy to have a regular income for fund houses?

This question prevailed for so long in my head when I saw too many ads over the internet and TV about Mutual funds and SIPs the best way. 
What intrigued me is no one could give us surety of returns and highlight the risks of the market and also while managing the fund take the fees from our pocket. 

So, I went on the journey to validate the claims and check against the data that I could gather and make a simulation out of it.

We downloaded the data about BSE month over month and calculated the returns for the entire history. 

We provided the SIP details regarding the duration of the SIP, the amount of SIP, and returns you can expect in CAGR from a mutual fund. 

What we noticed is that the **BSE index performed better in most of the scenarios unless we make a 12% CAGR** return from a mutual Fund. 

As you notice below is the comparison of the two strategies over 10 year period.

![Returns](https://github.com/user-attachments/assets/6ba05018-c277-47f0-9394-18691c77d262)

# Conclusion-

We can use the Mutual funds to invest indirectly into the market and expect similar growth. However, if the mutual fund has been providing returns less than **12% CAGR** basis annually it is a more viable option to invest in BSE or NIFTY BEES which are the same as index mimicking.

If you can spend some time and invest logically you may tend to grow with the market rate make decent returns and save on mutual fund fees. 

# Note - 
The mutual fund expense ratio was kept at 0.5% which is the industry minimum and the exit load was 1% again the industry minimum. 
Should you increase those percentages, GST, and other taxes the total investment amount and the returns will differ. 


# Approach 

**Data Gathering and Data Preparation**

Scrape the Yahoo finance website for the BSE historical month-on-month details, calculate the return percentage, and build the profile of the historical data. 

Mock up the data with the provided SIP amount, expected rate of return, tenure in months, if planning to increase the SIP, if yes then when and what percentage. 

Once you have the information we create the final data with the help of pandas and calculate the mutual fund value, invested value, and bse returns after every month. 

**Plot the data and conclude**

When we plotted the calculated values from the data gathered and generated, we noticed that it's better to invest directly instead of via mutual fund if the returns by mutual fund house are expected to be less than **14%**. If the mutual fund houses can generate returns of more than 14% in the BSE index funds category then we can consider going with the mutual investment strategy. 


To conclude **can SIP make you rich?**, I tend to side with the caution of **no**. The reasoning is, that if we check the return based on the total investment of 120000 over 10 years, we notice that it becomes almost 1.5 times. So, yes it can help you save your wealth by beating inflation and money depreciation, which traditionally hovers around 6% on average in the past. 

To create wealth or become rich other investment methods need to be explored and SIP and index investing should help you accumulate the wealth and save money you have earned. 

Looking for the feedback and any new different approach.
