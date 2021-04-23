from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = "C:/Users/pramod deshmukh/Desktop/DMWMiniProject/chromedriver.exe"
driver=""


def login():
	driver.get("http://127.0.0.1:8000")
	time.sleep(2)
	driver.find_element_by_id("login").click()

	username=input("Enter The Username\n")
	password=input("Enter the password\n")

	usernameElement=driver.find_element_by_name("username")
	usernameElement.send_keys(username)
	time.sleep(1)

	passwordElement=driver.find_element_by_name("password")
	passwordElement.send_keys(password)
	time.sleep(2)

	driver.find_element_by_name("login").click()


def clustering():
	driver.get("http://127.0.0.1:8000/home/dashboard")
	clustering=driver.find_element_by_id("sidebarClustering")
	clustering.send_keys(Keys.RETURN)

def apropri_on_clusters():
	driver.get("http://127.0.0.1:8000/home/dashboard")
	clustering=driver.find_element_by_id("sidebarAprOnClustering")
	clustering.send_keys(Keys.RETURN)
	time.sleep(5)
	driver.find_element_by_id("clusterButton").click()
	time.sleep(2)
	clusterNo=input("Enter the Cluster Number you want to select")
	option=driver.find_element_by_id(clusterNo)
	action = ActionChains(driver)
	action.click(on_element =option)
	action.perform()


	minimumSupportElement=driver.find_element_by_id("minSupportInput")
	minimumSupportElement.clear()
	minimumSupport=input("Enter The Minimum Support Value")
	minimumSupportElement.send_keys(minimumSupport)
	minimumSupportElement.send_keys(Keys.RETURN)
	time.sleep(1)



	minConfidenceElement=driver.find_element_by_id("minConfidenceInput")
	minConfidenceElement.clear()
	minConfidenceInput=input("Enter The Minimum Support Value")
	minConfidenceElement.send_keys(minConfidenceInput)
	minConfidenceElement.send_keys(Keys.RETURN)
	time.sleep(1)

	minLiftElement=driver.find_element_by_id("minLiftInput")
	minLiftElement.clear()
	minLiftInput=input("Enter The Minimum Support Value")
	minLiftElement.send_keys(minLiftInput)
	minLiftElement.send_keys(Keys.RETURN)
	time.sleep(3)

	driver.find_element_by_id("fetchButton").click()
	



def recommendation():
	driver.get("http://127.0.0.1:8000/home/dashboard")
	driver.find_element_by_id("sidebarRecommendations").click()
	time.sleep(3)
	driver.find_element_by_id("ageRangeButton").click()
	time.sleep(3)
	ageRange=input("Enter The Age Range")
	ageRange=driver.find_element_by_id(ageRange)
	action = ActionChains(driver)
	action.click(on_element =ageRange)
	action.perform()
	time.sleep(10)
	driver.find_element_by_id("custDropDownBtn").click()
	time.sleep(3)
	driver.find_element_by_id("Whole Wheat Pasta, Pancakes").click()
	time.sleep(3)
	print("The following is the Result reflected on the website ")
	print(driver.find_element_by_id("recommArea").text)
	# driver.close()


while True:
	choice=int(input("1.Login\n2.Clustering\n3.Apropri on Clusters\n4.Recommendation\n5.Close Browser\n6.Quit\n\n"))
	print(choice)
	if choice==1:
		driver = webdriver.Chrome(PATH)
		print("inside login")
		login()
	elif choice==2:
		driver = webdriver.Chrome(PATH)
		clustering()
	elif choice==3:
		driver = webdriver.Chrome(PATH)
		apropri_on_clusters()
	elif choice==4:
		driver = webdriver.Chrome(PATH)
		recommendation()
	elif choice==5:
		driver.close()
	elif choice==6:
		break;