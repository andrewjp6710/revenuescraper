Web Revenue Scraper using ScrapeOps.io

This software automates revenue checks for multiple accounts, eliminating the need for manual inspection. It leverages ScrapeOps.io's API keys to bypass bot checks, offering free trials and subscriptions for up to 500,000 monthly revenue checks.

Installation:

1. Download the code by clicking on "Code" -> "Download Zip."
2. Use a Code Editor (e.g., VS Code) to open the unzipped folder.
3. Install Python3 on your machine (from the [Python site](https://www.python.org/downloads/) or Microsoft Web Store).
4. Open a terminal, navigate to the folder, and run `pip install -r requirements.txt`.

Usage:

1. Create a copy of the Excel file with the accounts for revenue checks (as the code will overwrite it).
2. Rename the Excel file to ".xlsx" for easy typing in the terminal.
3. In the terminal, type `python3 neo.py`.
4. Follow the terminal prompts, including the filename and region of your accounts.
5. Close the Excel file while the program runs, as it needs to overwrite the file at the end.
6. Reopen the file to find account details reduced to two columns: account_name and revenue.

Note:

Replace `SCRAPEOPS_API_KEY` with the key provided by ScrapeOps.

For detailed instructions on setting up VS Code, refer to the [VS Code setup guide](https://code.visualstudio.com/docs/setup/windows).
