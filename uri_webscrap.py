from bs4 import BeautifulSoup 
import csv 

from selenium import webdriver
import time
import sys
import codecs

first = int(sys.argv[1])
last = int(sys.argv[2]) +1
scriptname = sys.argv[0]
filename = "entradas{}-{}.txt".format(first, last-1)
file = codecs.open(filename, "w", "utf-8")
token = scriptname
browser = webdriver.Chrome()
for x in range(first, last):
    print("baixando problema " + str(x))
    URL = "https://www.urionlinejudge.com.br/judge/pt/problems/view/{}".format(x)
    try:
        browser.get(URL)

        problemClass = browser.find_element_by_class_name("place-view").text
        problemPageUrl = browser.find_element_by_id("description").find_element_by_id("description-html").get_attribute("src")
        browser.get(problemPageUrl)
        pDescription = browser.find_element_by_class_name("description").text
        pInput = browser.find_element_by_class_name("input").text
        pOutput = browser.find_element_by_class_name("output").text

        file.write('\n')
        file.write(token + " problema=" + str(x))
        file.write('\n')
        file.write(token + " classe=")
        file.write(problemClass)
        file.write('\n')
        file.write(token + "  DESCR")
        file.write('\n')
        file.write(pDescription)
        file.write('\n')
        file.write(token + "  FIMDESCR")
        file.write('\n')
        file.write(token + "  ENTRADA")
        file.write('\n')
        file.write(pInput)
        file.write('\n')
        file.write(token + "  FIMENTRADA")
        file.write('\n')
        file.write(token + "  SAIDA")
        file.write('\n')
        file.write(pOutput)
        file.write('\n')
        file.write(token + "  FIMSAIDA")
        file.write('\n')
    except:
        print("erro baixando o problema " + str(x))