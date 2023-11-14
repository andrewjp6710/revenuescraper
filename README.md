# revenuescraper

This software allows you to check revenues for multiple accounts automatically, instead of you having to do it one by one.

The code essentially opens an Excel file (the file must be a .xlsx file and not a .csv or anythign else), and searches the first sheet of the excel sheet for a column with "account_name". It then performs a Google Search Query and looks for the most relevant account on ZoomInfo and returns a revenue by webscraping.
The following instructions allow for installation of the software, its dependencies, and its use. The software relies on ScrapeOps.io's API keys to bypass the bot checks. ScrapeOps.io allows you for free trials, but with a subscription you will be allowed up to 500,000 revenue checks in one month. When using, keep in midn you will have to replace SCRAPEOPS_API_KEY with your own key that ScrapeOps will provide.

How to use:
1. Click code -> "Download Zip"
2. Open the file on your local machine
3. Install pip and python3 on your local machine
4. Use pip install -r requirements.txt
5. Create a copy of the Excel file with all the accounts you wish to revenue check, as the code will write over the Excel file
6. In the terminal, type python3 neo.py
7. Follow directions that terminal presents, including the name of the file with the accounts (in one sheet) and the region of your accounts in the sheet (EG New South Wales, Queensland etc)
8. When you open the file again, your original account with all the details will have been removed with just 2 columns of account_name and revenue.
