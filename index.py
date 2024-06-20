from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from urllib.parse import urlparse

def getJobDetailsFromLinkedIn(link):

    job_detail = dict()

    options = Options()
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=options)

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
        job_detail = getJobDetailsFromLinkedIn(link)
        JOB_DETAILS.append(job_detail)

    for job_detail in JOB_DETAILS:
        print(job_detail)
        print()

    # quit browser
    driver.quit()
    


extractJobLinksFromLinkedIn("C++", "Banglore")


