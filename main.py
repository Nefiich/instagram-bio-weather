from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


username = input("Input your Instagram username : ")
password = input("Input your Instagram password : ")
city_name = input("Input your City name : ")
api_key = input("Input your OpenWeatherMap API key : ")
bio = input("Input your bio : ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(f"https://www.instagram.com/{username}/")
time.sleep(10)
print("I'm about to click the element -> login start!")
login = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
login.click()

time.sleep(5)

print("I'm about to click the element -> input the username!")
username_input = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input')
username_input.send_keys(username)

time.sleep(3)

print("I'm about to click the element -> input the password!")
password_input = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input')
password_input.send_keys(password)

time.sleep(3)

print("I'm about to click the element -> loging in!")
login.final = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
login.final.click()

time.sleep(10)

print("I'm about to click the element -> profile image!")
profile_click = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
profile_click.click()

time.sleep(2)

print("I'm about to click the element -> profile open!")
profile_open = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
profile_open.click()

time.sleep(5)

print("I'm about to click the element -> edit profile button!")
edit_profile = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/a')
edit_profile.click()

time.sleep(5)

JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """


for i in range(100000):

    print("Editing bio!")
    bio_edit = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea')
    bio_edit.send_keys(Keys.CONTROL + "a")
    bio_edit.send_keys(Keys.BACKSPACE)

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    data = response.json()
    temp_kelvin = data["main"]["temp"]
    temp = temp_kelvin - 273.15

    t = time.localtime()
    curr_time = time.strftime("%H:%M:%S", t)

    print("Times done : " + str(i) + ", current temp. : " + str(round(temp,2)) + "°, with the current time : " + curr_time)

    time.sleep(3)

    # -----------------------------------------------------------------

    text = f"Current temperature in {city_name} : " + str(round(temp,2)) + "°"

    driver.execute_script(JS_ADD_TEXT_TO_INPUT, bio_edit, text)
    bio_edit.send_keys(Keys.ENTER)

    time.sleep(1)
    # -----------------------------------------------------------------

    driver.execute_script(JS_ADD_TEXT_TO_INPUT, bio_edit, bio)
    bio_edit.send_keys(Keys.ENTER)

    time.sleep(1)

    print("Submiting bio!")
    submit_bio = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button')
    submit_bio.click()
    time.sleep(1300)
