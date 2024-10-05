import requests

# URL से इमेज डाउनलोड करें
url = "https://gurpreetsingh.aliens.school/whatsapp.png"
response = requests.get(url)

# इमेज को लोकल फाइल में सेव करें
with open("whatsapp.png", "wb") as file:  # 'wb' mode binary write के लिए है
    file.write(response.content)

print("Image successfully downloaded and saved as whatsapp.png")
