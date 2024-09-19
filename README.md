# Mutual Fund vs. Index Fund: A Data-Driven Comparison

![DALL·E 2024-09-19 15 56 04 - A split road leading toward a financial goal, with two paths_ one representing mutual funds and the other index funds  The mutual fund path has symbol](https://github.com/user-attachments/assets/f2ef1710-9bc4-48cf-99ac-a55681acb7ed)



## Introduction
For years, the debate has persisted: is investing in mutual funds through a Systematic Investment Plan (SIP) the best strategy for wealth accumulation, or is it simply a marketing tactic by fund houses to ensure regular inflows of capital? Advertisements frequently position SIPs as a secure and promising method of growing wealth, but these claims often overlook the risks of the market and the management fees deducted from the investor's pocket.

This motivated me to dig deeper into the data and test the claims against traditional self-investing approaches like index funds. I wanted to answer: _Are mutual funds via SIP the best wealth-building strategy compared to self-investing in index funds?_

## Methodology and Approach

### Data Collection and Preparation
The backbone of this analysis lies in historical data of the **Bombay Stock Exchange (BSE)**. I scraped month-on-month BSE data from Yahoo Finance and computed the historical returns of the BSE index to simulate its performance.

Next, I mocked up SIP data, where the following parameters were considered:

**Duration of SIP:** Ten years (120 months)
**SIP Amount:** Fixed monthly investments
**Expected CAGR Return from Mutual Funds:** A range of returns was tested to compare performance against the BSE index.

I also incorporated key costs such as:

**Expense Ratio:** 0.5% (industry minimum)
**Exit Load:** 1% (industry minimum)

These represent fees charged by mutual funds, which are essential in understanding their impact on overall returns.

### Strategy Simulation

The analysis compared two approaches:

**Investing via Mutual Funds:** SIP in a mutual fund with a hypothetical range of Compound Annual Growth Rates (CAGR) returns, varying from 10% to 14%.
**Investing Directly in the BSE Index:** The performance of the BSE index over the same period.
For both strategies, we evaluated the **final corpus** at the end of the ten-year period, the **total invested amount**, and the **returns after expenses**.

## Results and Findings
Through the comparison, a crucial insight emerged: **the BSE index outperformed mutual funds in most scenarios unless the mutual fund achieved at least a 12% CAGR**.

### Key Observations:

When the mutual fund generated a **CAGR of less than 12%**, direct investment in the BSE index consistently produced better results.
If mutual funds yielded a **CAGR above 12%**, they began to match or surpass the returns of index investing. This threshold further increased when we accounted for taxes, expense ratios, and exit loads.
The attached graph (see below) illustrates the comparative returns between the two strategies over a ten-year period. You can clearly observe how the index fund consistently outperformed mutual funds with lower returns.
![Returns](https://github.com/user-attachments/assets/9bcf08bc-e32a-452c-9cf5-37a241838fe9)


### Conclusion
Based on the data, **SIP in mutual funds is not the best approach for wealth accumulation unless the fund consistently generates a return of more than 12% CAGR**. When mutual funds achieve lower returns, it's more prudent to invest directly in index funds like **BSE or NIFTY BEES** that track the broader market with minimal fees.

If you're willing to spend some time researching and making logical decisions, you can:

**Grow with the market** and make decent returns.
**Save on management fees** charged by mutual funds.

#### Practical Implications:

**Expense Ratios & Fees Matter:** In our simulations, the mutual fund's expense ratio was set at the minimum industry standard of 0.5%, and the exit load at 1%. Even these modest costs can substantially erode returns over time.
**The Impact of Higher Costs:** If the expense ratio or exit load is higher, as is common with many actively managed funds, the potential returns would further diminish, reinforcing the advantage of direct index investing.

# Can SIP Make You Rich?
In my analysis, the answer is, proceed with caution. If we examine a typical SIP investment of ₹120,000 over ten years, it grows to about 1.5 times the investment. While this provides protection against inflation (which averages 6%), it doesn’t make you _wealthy_ in real terms.

SIP and index investing should be viewed as **wealth preservation tools** that help your money grow at a reasonable rate, protecting it from inflation and depreciation. To truly create wealth, you may need to explore other investment strategies beyond traditional SIPs.

## Final Thoughts
While mutual funds and SIPs offer a convenient and low-effort investment approach, the decision to rely on them heavily depends on the expected returns. If your chosen mutual fund consistently delivers above 12% CAGR, it could be worth considering. Otherwise, index funds offer a more reliable and cost-effective path for wealth accumulation.

## Technical Resources Used
To accomplish this analysis, the following technical tools and libraries were employed:

1. **Data Scraping:**
`BeautifulSoup` and `Requests`: Used to scrape historical month-on-month data from Yahoo Finance.
2. **Data Processing:**
`Pandas`: Employed for data cleaning, preparation, and calculations, such as generating returns from the BSE index and SIP investments.
3. **Visualization:**
`Seaborn` and `Matplotlib`: Used to plot the results, providing clear visuals of the comparison between mutual fund returns and BSE index performance.

## Next Steps
I welcome any feedback or suggestions on different approaches that could be explored. Additionally, further testing with varying parameters such as **increasing SIP contributions over time, different exit points**, or **incorporating dividends** could provide more insight into the optimal strategy for individual investors.
