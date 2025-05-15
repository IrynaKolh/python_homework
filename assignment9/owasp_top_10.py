from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")

driver.implicitly_wait(5)

# XPath: Each item is a <li> inside <ol> with ID 'top10-list'
items = driver.find_elements(By.XPATH, "//section[@id='sec-main'] //ul[2] //li")

vulnerabilities = []

for item in items:
    try:
        a_tag = item.find_element(By.TAG_NAME, "a")
        link = a_tag.get_attribute("href")
        title = a_tag.find_element(By.TAG_NAME, "strong").text
        vulnerabilities.append({"Title": title, "Link": link})
    except Exception as e:
        print("Error:", e)

driver.quit()

# Save to CSV
df = pd.DataFrame(vulnerabilities)
df.to_csv("owasp_top_10.csv", index=False)

# Print to verify
print(df)
