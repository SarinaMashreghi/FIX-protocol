import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
main_url = "https://www.onixs.biz/fix-dictionary/4.2/msgs_by_msg_type.html"
# response = requests.get(url)

# # Create a BeautifulSoup object to parse the HTML content
# soup = BeautifulSoup(response.text, "html.parser")

# # Find the table containing the message types and fields
# table = soup.find("table", {"class": "table"})

# print(table)
# for row in table.find_all("tr")[1:]:
#     # Get the cells in the row
#     cells = row.find_all("td")

#     # Extract the message type and name
#     msg_type = cells[0].text.strip()
#     name = cells[1].text.strip()

#     # Extract the fields (skip the first two cells)
#     fields = [cell.text.strip() for cell in cells[2:]]

#     # Print the message type, name, and fields
#     print(f"Message Type: {msg_type}")
#     print(f"Name: {name}")
#     print("Fields:")
#     for field in fields:
#         print(field)
#     print()

# url = "https://www.onixs.biz/fix-dictionary/4.2/msgs_by_msg_type.html"
# response = requests.get(url)

# # Print the response content
# print(response.text)
types_dict = {
    "String": "string"
}

tags = []
types = []

for i in range(1, 447):
    tag_url = f"https://www.onixs.biz/fix-dictionary/4.2/tagNum_{i}.html"
    response = requests.get(tag_url)
    # print(response)
    
    soup = BeautifulSoup(response.text, "html.parser")
    tag_name = soup.find("h1").text.strip().split()[0]
    data_type = soup.find_all("p")[0].text.strip().split()[1]
    tags.append(tag_name)
    types.append(data_type)
    
d = {"tags": tags, "type":types}
df = pd.DataFrame(d)
    
print(df)
print(types)
