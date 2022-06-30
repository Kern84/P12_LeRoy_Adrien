from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def test_user_experience_chrome():
    """
    Function to test the user experience.
    Go to the Django-admin page;
    Try to log in with a correct email and a wrong password;
    Log in with a correct email and password;
    Click on the link to go to the clients page;
    Click on the add client link and create a new client;
    Click on the link to go to the contracts page;
    Go to the add contract page and create a new contract;
    Click on the link to go to the events page;
    Click on the ID link of an event to view the details;
    Logout.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/admin/login/")
    WebDriverWait(driver, timeout=1).until(EC.title_contains("Log in"))
    assert "Log in | Django site admin" in driver.title

    driver.find_element(By.NAME, "username").send_keys("adrien@email.fr")
    driver.find_element(By.NAME, "password").send_keys("WrongP4ssword" + Keys.RETURN)
    WebDriverWait(driver, timeout=1).until(EC.title_contains("Log in"))
    assert "Please enter the correct email" in driver.page_source

    driver.find_element(By.NAME, "password").send_keys("S3cret!1" + Keys.RETURN)
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Site administration | Django site admin")
    )
    assert "Welcome" in driver.page_source

    clients_link = driver.find_element(By.LINK_TEXT, "Clients")
    clients_link.click()
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Select client to change | Django site admin")
    )
    assert "Select client to change" in driver.title

    add_client_link = driver.find_element(By.CLASS_NAME, "addlink")
    add_client_link.click()
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Add client | Django site admin")
    )
    assert "Add client" in driver.title

    driver.find_element(By.NAME, "first_name").send_keys("Michel")
    driver.find_element(By.NAME, "last_name").send_keys("Jourdan")
    driver.find_element(By.NAME, "email").send_keys("michel@email.fr")
    driver.find_element(By.NAME, "phone").send_keys("01234561542")
    driver.find_element(By.NAME, "mobile").send_keys("0687546743")
    driver.find_element(By.NAME, "compagny_name").send_keys("NBA" + Keys.RETURN)
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Select client to change | Django site admin")
    )
    assert "The client" in driver.page_source

    contract_page_link = driver.find_element(By.LINK_TEXT, "Contracts")
    contract_page_link.click()
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Select contract to change | Django site admin")
    )
    assert "Select contract to change" in driver.title

    driver.get("http://127.0.0.1:8000/admin/app/contract/add/")
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Add contract | Django site admin")
    )
    assert "Add contract" in driver.title

    select_sale_contact = driver.find_element(By.NAME, "sale_contact")
    select_object = Select(select_sale_contact)
    select_object.select_by_value("38")
    select_client = driver.find_element(By.NAME, "client")
    select_element = Select(select_client)
    select_element.select_by_value("1")
    driver.find_element(By.NAME, "status").click()
    driver.find_element(By.NAME, "amount").send_keys("1234")
    driver.find_element(By.NAME, "payment_due").send_keys("2023-10-20" + Keys.RETURN)
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Select contract to change | Django site admin")
    )
    assert "The contract" in driver.page_source

    event_page_link = driver.find_element(By.LINK_TEXT, "Events")
    event_page_link.click()
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Select event to change | Django site admin")
    )
    assert "Select event to change" in driver.title

    event_link = driver.find_element(By.LINK_TEXT, "2")
    event_link.click()
    WebDriverWait(driver, timeout=1).until(
        EC.title_contains("Event object (2) | Change event | Django site admin")
    )
    assert "Event object (2)" in driver.title

    driver.quit()
