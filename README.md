# AnomScrapper
Parse information from high security websites and even automate the process

## Installation

Pip installation

	pip install -r requirements.txt

**This application only supports chromium based browsers**. Open your browser and check the version. Download the matching chromedriver from [here] [https://chromedriver.chromium.org/downloads] and replace the chromedriver.exe in ''driver" folder. 

## Features

* Anonymous web scrapping
* Unique user-agent
* Fully customizable scapper (Do need to know basic JS)
* Fully customizable remote browser. 
* Can be automated
* Interactive parsing

## Usage

Open the 'main.ipynb' and run the first cell.

	BrowserControl Parameters

	useragentspoofing: bool, default = True
		Generates a fake user-agent for the browser. This increases anonymity.
		
	incognito: bool, default = True
		Opens the browser in incognito mode 
		
	browserprofilemodee: bool, default = True  
		Uses a custom profile for the remote browser. This is recommended if you want to use custom 
		browser extensions.
		
	dir_exe_chrome: str, default =r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",  
	The location of the broweser executable.
	
	port: int, default == 9222
		The port the remote browsers uses

#### Browsers

Brave is highly suggested for anonymity. But any chromium-based browser will work.

**Anonymity is essential because websites with high security will block bots like this. So, customize the browser and make it as anonymous as possible.**

To check the security and blocking capabilities of your browser, use : https://coveryourtracks.eff.org/

Using browser extension like ad-blocker and VPN also helps.

If you want to customize the remote browser, run the second cell. It will open up the remote browser. Now add or remove extension or customize it however you like. Use extensions that can auto start itself when the browser opens. So you don't have to manually start it every time.

*Note : The browser customization won't change anything in your actual browser if you are using a custom profile. Which is activated by default*


#### Scrapping

The cell no 3-5 of 'main.ipynb' are custom codes I have used that fully automates scrapping reviews from Amazon. But you don't have to use that. 

You just have to run the code below after you already ran the first two cells.

	driver.get(r"your URL")

Then add your own JS code that parses information from your desired website

	driver.execute_script('''

	//your JS code goes here

    ''')

*Note: driver.execute_script function can return the output of your JS code. But to return the output, you have to use return in your JS code. (follow my example from cell: 3 method: parse_review_page)* 

Since this in Jupyter notebook. The application won't close if you made mistakes in your code. With a few trails and error, you can easily automate parsing for your website.
