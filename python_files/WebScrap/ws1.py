from bs4 import BeautifulSoup

f = open(r"C:\Users\sgast\CODING\html\test.html",'r').read()

soup = BeautifulSoup(f,'html.parser')

print(soup.prettify())