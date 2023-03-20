from selenium import webdriver
from selenium.webdriver.common.by import By


def getAnswer():
    questionLabels = []
    questionChoices = []
    
    
    questionLabels.append(driver.find_element(By.TAG_NAME, 'strong').text)
    questionHolder = driver.find_element(By.CLASS_NAME, "_vq37gq").find_elements(By.CLASS_NAME, "paragraph")
    sumbitButton = driver.find_element(By.CLASS_NAME,"_1pyeoxjt")

    for i in range(len(questionHolder)):
        if questionHolder[i].text != "":
            questionChoices.append(questionHolder[i].text)
            questionChoices = [*set(questionChoices)]
    for i in range(len(questionChoices)):
        # try:
            try:
                answer = correctAnswers[questionLabels[0]]
                click = driver.find_element(By.XPATH,f"//*[contains(text(), '{answer}')]")
                input("Found correct")
                click.click()
                sumbitButton.click()
                return 0
            except Exception:
                print("Havent found answer yet.")
            clickOn = driver.find_element(By.XPATH, f"//*[contains(text(), '{questionChoices[0]}')]")
            driver.execute_script("arguments[0].click();", clickOn)
            # webdriver.ActionChains(driver).move_to_element(clickOn).click(clickOn).perform()
            # while clickOn.accessible_name != "button":
            #     try:
            #         print(clickOn.get_property("tagName"))
            #         clickOn = clickOn.find_element(By.XPATH, "..")
            #     except Exception:
            #         ...
            questionChoices.pop(0)
            sumbitButton.click()
            input()
            try:
                correct = driver.find_element(By.XPATH,"//*[contains(text(), 'Correct (selected)')]").find_element(By.XPATH, "..").find_elements(By.CLASS_NAME, "paragraph")
                for i in range(len(correct)):
                    if correct != "":
                        correctAnswers[questionLabels[0]] = correct
                        sumbitButton.click()
                        return 0
            except Exception:
                ...
        # except Exception:
score = 0 
correctAnswers = {}
driver = webdriver.Chrome("C:\\Users\\jrmar\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.khanacademy.org/login")

input("Ready?")
while score != 100:
    getAnswer()

    #questions class : _vq37gq
    # answer choices tag : _1i12ty58
    # correct answer : _eplbrxf
    # class : paragraph
    # class for labels : strong