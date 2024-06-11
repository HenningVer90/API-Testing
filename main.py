import tkinter as tk
import requests

# Function to make API calls
def call_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to retrieve data: {response.status_code}"}

# Function to handle button click events
def button_click(api):
    if api == "Population":
        result = call_api("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
        if "error" in result:
            result_label.config(text=result["error"])
        else:
            result_label.config(text=f"Population: {result['data'][0]['Population']}")
    elif api == "My IP Address":
        result = call_api("https://api.ipify.org/?format=json")
        if "error" in result:
            result_label.config(text=result["error"])
        else:
            result_label.config(text=f"Your IP address: {result['ip']}")
    elif api == "My IP-Related Info":
        result = call_api("https://ipinfo.io/161.185.160.93/geo")
        if "error" in result:
            result_label.config(text=result["error"])
        else:
            result_label.config(text=f"IP related info: {result}")

# Create the main window
root = tk.Tk()
root.title("API Selector")

# Create buttons for each API
population_button = tk.Button(root, text="Population", command=lambda: button_click("Population"))
population_button.pack(pady=5)

ip_button = tk.Button(root, text="My IP Address", command=lambda: button_click("My IP Address"))
ip_button.pack(pady=5)

ip_info_button = tk.Button(root, text="My IP-Related Info", command=lambda: button_click("My IP-Related Info"))
ip_info_button.pack(pady=5)

# Create a label to display the API response
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
