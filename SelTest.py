from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Get login credentials
login = "83451:241289"
password = "Lunch4bl35"

# Go to sagemember.com
driver = webdriver.Firefox()
driver.get("https://www.sagemember.com/sgadmin.exe/Settings?Pg=WEShowrooms&UID=241289")
assert "SAGEmember.com" in driver.title

wait = WebDriverWait(driver, 10)
add_values = ['TruTeam','TrueTeam Commercial Services','Advantage Glass','Aladdin Insulation of Missouri','All Seasons Insulation','Allied','American Building Products','American Hungerford Building Products','American National Insulation','American National Insulation & Sealants','Austin Contractor Services','BSI Building Products & Services','Builders Insulation & Bldg Prods','C&S Supply','Capital Insulation Services of Maryland','Capitol Insulators & Building Products','Cary Insulation','Cellpak','Center of Excellence','Central Valley Insulation','City Wide Insulation','CJ Insulation','Coast Building Products','Coastal Insulation','Collins & Co','Contractor Services of Georgia','Contractor Services of Iowa',"D's Insulation",'Dale Insulation','Dale Insulation of Knoxville','Davenport Commercial','Davenport Insulation','Davis Insulation','DeepSouth Insulation','Duke Contractor Services','E&B Insulation','Eastern Insulation','EcoFoam Insulutions','EE Bentley','Energy Sense','Environments For Living','Fairfield Insulation','Fiberfoil Insulation','G&B Insulation','Gale Building Products','Gale Contractor Services','Gale Insulation','Gale Insulation & Specialties','Gallatin Insulation','Gede Insulation','Gutter King','Hansen All Seasons Insulation','Insulation Contractors','Insulpro Projects','Jansen & Sons','Johnson Insulation','Jones Boys Insulation',"Kent's Insulating",'Mato','McPherson Insulation','Michiana Insulation','More Insulation','Nebraska Building Products','New England Building Products','Pender & Pettus','Penguin Insulation','Quality Insulation of Maine','Quality Building Products','Quality Insulation','Quality Insulation & Building Products','Quality Insulation of Eastern CT','Quality Insulation of Lexington','Quality Insulation of Meredith','Quality Insulation of Portsmouth','Red Lion Insulation','Renn Building Products','Rice Insulation & Glass','Sacramento Building Products','Santa Rosa','Sexton Insulation & Gutters','Sparling Gale Insulation & Specialties','Superior Insulation Products','Synergy Insulation','TopBuild','TopBuild Home Services','Tri City Insulation & Building Products','Tri City Insulation & Bldg Prods of Fayetteville','Tri City Insulation of Raleigh','Tri State Insulation','TruTeam of California','Tulsa Energy Control','Verns Insulation','Western Cary Building Products','Western Insulation','Williams Contractor Services','Williams Fireplaces & Gutters','Williams Insulation']

# Fill in and submit login credentials
elem = driver.find_element_by_class_name("form-control")
elem.send_keys(login)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

# Waits for iframe to load and switches to it
wait.until(EC.frame_to_be_available_and_switch_to_it('ContentFrame'))

# Go to products list
driver.implicitly_wait(10)
products = driver.find_elements_by_xpath("/html/body/div[3]/table/tbody/tr[19]/td[9]/button[3]")
products[0].click()

# Waits for page to load
driver.implicitly_wait(5)

# Grabbing number of products in showroom
products = driver.find_elements_by_xpath('//tbody/tr')
products_length = len(products)

# Loops through list of products
for i in range(products_length):
    # Click to edit product
    driver.find_elements_by_name('Edit')[i].click()
    driver.implicitly_wait(10)

    # Adds name to custom options
    driver.find_element(By.XPATH, '//a[text()="Item Options"]').click()
    driver.implicitly_wait(2)
    name_field = driver.find_element_by_name('CustomFld4Name')
    value_field = driver.find_element_by_name('CF4NameAdd')
    name_field.send_keys('Logo')

    # Loops to add values for drop downs
    for value in add_values:
        value_field.send_keys(value)
        driver.find_element(By.XPATH, '/html/body/form/div/div[1]/div[4]/table/tbody/tr/td[2]/div[4]/div[3]/div[2]/input').click()

    # Saves
    value_field.send_keys(Keys.RETURN)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/table/tbody/tr[4]/td[8]/input[1]')))
