import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os, time
import subprocess
# from fake_useragent import UserAgent
from latest_user_agents import get_latest_user_agents, get_random_user_agent

# MUST - the browser from cmd run must match the browser in webdriver, match - incognito, useragent, port
# cmd_custom_session = '"{}" --remote-debugging-port={} --user-data-dir="{}" --user-agent="{}"'.format(dir_exe_chrome,port,dir_file_chrome_profile,self.userAgent)
class BrowserControl:
    dir_root = os.getcwd()
    dir_gecko_exe = dir_root + "/driver" + "/chromedriver.exe"
    # port = 9222
    # ua = UserAgent(verify_ssl=False, use_cache_server=False, cache=False)
    # userAgent = ua.random

    def __init__(self,  useragentspoofing = True, incognito = True, browserprofilemodee = True, dir_exe_chrome=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", port = 9222):
        self.browserprofilemodee = browserprofilemodee
        self.useragentspoofing = useragentspoofing
        self.incognito = incognito
        self.dir_exe_chrome = dir_exe_chrome
        self.port = port
        if self.useragentspoofing:
            self.userAgent = get_random_user_agent()
        pass
        self.integrity_check()

    def integrity_check(self):
        if not (os.path.exists(self.dir_exe_chrome)):
            print("Fatal Error : Invalid browser executable path")
            print("Solution : Pass a valid browser executale path to dir_exe_chrome to argument")
            sys.exit(1)
        if not (os.path.exists(self.dir_gecko_exe)):
            print("Fatal Error : Invalid gecko driver path")
            print("Solution : Download chrome driver from : https://chromedriver.chromium.org/downloads and paste the 'chromedriver.exe' in the 'driver' folder(create folder in necessary)")
            sys.exit(1)

    def halt(self,seconds):
        print("---------------------------------------------------")
        print("Enterning sleep mode for {} seconds".format(seconds))
        for i in range(seconds):
            time.sleep(1)
            print("Time elapsed : {} | Time remaining {}".format(i,seconds-i))
        print("---------------------------------------------------")

    def create_custom_session(self):
        dir_file_chrome_profile = self.dir_root + r"\browser data"

        cmd_dir_profile = '--user-data-dir="{}"'.format(dir_file_chrome_profile)
        cmd_useragent = '--user-agent="{}"'.format(self.userAgent)
        cmd_mode = "--incognito"
        # must maintain serial
        status_mode = [self.browserprofilemodee, self.useragentspoofing, self.incognito]
        status = [cmd_dir_profile, cmd_useragent, cmd_mode]

        cmd_custom_session = '"{}" --remote-debugging-port={}'.format(self.dir_exe_chrome,self.port)

        for i in range(len(status_mode)):
            if status_mode[i]:
                cmd_custom_session += " " + status[i]

        print("\tStarting custom browser")
        print("Running command: {}".format(cmd_custom_session))
        process = subprocess.Popen(cmd_custom_session, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)

    def connect_to_session(self):
        port = self.port    
        service = Service(self.dir_gecko_exe)

        print("\n\tSetting up browser")

        chrome_options = webdriver.ChromeOptions()
        print("Setting port - {}".format(port))
        chrome_options.add_experimental_option("debuggerAddress","localhost:{}".format(port))

        if self.useragentspoofing:
            print("Setting user agent - {}".format(self.userAgent))
            chrome_options.add_argument('--user-agent="{}"'.format(self.userAgent))

        if self.incognito:
            print("Creating session in incognito mode")
            chrome_options.add_argument("--incognito")

        print("\n\tBrowser Capabiliteies:")
        capabilities = chrome_options.to_capabilities()

        for item in capabilities:
            print("{} : {}".format(item,capabilities[item]))
            if type(capabilities[item]) == dict:
                for item1 in capabilities[item]:
                    print("{} : {}".format(item1,capabilities[item][item1]))

        print("\n\tConnect to remote browser:")
        driver = webdriver.Chrome(service=service, options= chrome_options)
        print("Driver connected to remote browser")
        print("Session ID : {}".format(driver.session_id))
        print("User Agent : {}".format(driver.execute_script("return navigator.userAgent")))

        return driver

    def get_driver(self):
        self.create_custom_session()

        print("Waiting for browser to start the extension")
        self.halt(5)

        return self.connect_to_session()