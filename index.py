from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from urllib.parse import urlparse

from datetime import datetime, timedelta


def calculate_previous_date(time_interval):
    # Split the time interval into number and unit
    parts = time_interval.split()
    if len(parts) != 3 or parts[2] != 'ago':
        raise ValueError("Invalid time interval format. Please use 'X unit ago' format.")
    
    try:
        num = None
        unit = None
        # 1 year(s) ago
        if (parts[1] == "year" or parts[1] == "years"):
            num = int(parts[0]) * 52.143
            unit = "week"
        elif (parts[1] == "month" or parts[1] == "months"):
            num = int(parts[0]) * 4.345
            unit = "week"
        else:
            num = int(parts[0]) 
            unit = parts[1]

    except ValueError:
        raise ValueError("Invalid number format in time interval.")
    
    # Define the mapping of units to timedelta parameters
    unit_map = {
        'week': 'weeks',
        'day': 'days',
        'hour': 'hours',
        'weeks': 'weeks',
        'days': 'days',
        'hours': 'hours'
    }
    
    if unit not in list(unit_map.keys()) + ["year", "years", "month", "months"] :
        raise ValueError("Unsupported time unit. Supported units are: year, month, week, day, hour.")
    
    # Calculate the timedelta
    delta_args = {unit_map[unit]: num}
    delta = timedelta(**delta_args)
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the previous date
    previous_date = current_date - delta
    
    return previous_date.strftime("%d-%m-%Y")  # Format the date as DD-MM-YYYY


def getJobDetailsFromLinkedIn(link):
    
    job_detail = dict()

    options = Options()
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    driver.get(link)

    #extract job title
    job_title = driver.find_element(by=By.CSS_SELECTOR, value="h1.top-card-layout__title")
    job_detail["job_title"] = job_title.get_attribute('innerText')

    #extract location
    job_location = driver.find_elements(by=By.CSS_SELECTOR, value="span.topcard__flavor")[1]
    job_detail["location"] = job_location.get_attribute("innerText")

    #extract experience level
    experience_level = driver.find_elements(by=By.CSS_SELECTOR, value="ul.description__job-criteria-list li span")[0]
    job_detail["experience_level"] = experience_level.get_attribute("innerText")

    #extract job type
    job_type = driver.find_elements(by=By.CSS_SELECTOR, value="ul.description__job-criteria-list li span")[1]
    job_detail["job_type"] = job_type.get_attribute("innerText")

    #extract date posted
    job_date_posted = driver.find_element(by = By.CSS_SELECTOR, value=".posted-time-ago__text")
    job_detail["job_date_posted"] = calculate_previous_date( job_date_posted.get_attribute("innerText") )

    #extract apply link
    job_detail["apply_link"] = link

    #extract job portal
    job_detail["job_portal"] = urlparse(link).netloc

    driver.quit()

    
    return job_detail


# go to linked in; extract job links
def extractJobLinksFromLinkedIn(title, location):
    SEARCH_QUERY = f"{title} job in {location} linkedin"

    options = Options()
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(options= options)
    # driver = webdriver.Chrome()

    # go to google homepage
    driver.get("https://www.google.com/")

    # extract search box
    search_box_textarea = driver.find_elements(by=By.CSS_SELECTOR, value="textarea")[0]

    # enter search query in search box
    search_box_textarea.send_keys(SEARCH_QUERY)

    # Hit enter
    search_box_textarea.send_keys(Keys.ENTER)

    # extract first search result
    driver.implicitly_wait(5)  # seconds
    search_result = driver.find_elements(by=By.CSS_SELECTOR, value="h3")[0]
    

    # click on first search result
    search_result.click()

    # extract anchor tags for jobs in linkedin
    job_anchor_tags =  driver.find_elements(by=By.CSS_SELECTOR, value="a.base-card__full-link")

    print(f"{ len(job_anchor_tags) } jobs extracted")
    JOB_LINKS = []


    # extract job links from anchor tags and fill JOB_LINKS[]
    job_anchor_tags = job_anchor_tags[0: 10]
    for anchor_tag in job_anchor_tags:
        href = anchor_tag.get_attribute("href")
        JOB_LINKS.append(href)


    JOB_DETAILS = []

    for link in JOB_LINKS:
        try:
            job_detail = getJobDetailsFromLinkedIn(link)
            JOB_DETAILS.append(job_detail)
        except Exception:
            print("error in getJobDetailsFromLinkedIn(link)")

    for job_detail in JOB_DETAILS:
        print(job_detail)
        print()

    # quit browser
    driver.quit()
    


extractJobLinksFromLinkedIn("java", "Pune")


# new code is here