import json
import requests
import humanfriendly
import time

units = {"B": 1, "KB": 10 ** 3, "MB": 10 ** 6, "GB": 10 ** 9, "TB": 10 ** 12}


def parseSize(size):
    number, unit = [string.strip() for string in size.split()]
    return int(float(number) * units[unit])


def percentage(part, whole):
    return 100 * float(part) / float(whole)


url = "https://api.64clouds.com/v1/getServiceInfo?veid=1493802&api_key=private_OCAqy9mhEUvgiCtMGTAz2lt5"
json_data = requests.get(url)
data = json_data.json()
monthly_data_plan = humanfriendly.format_size(data.get("plan_monthly_data"))
monthly_data_used = humanfriendly.format_size(data.get("data_counter"))
reset_date = time.gmtime(data.get("data_next_reset"))
# reset_date = time.asctime(time.localtime(data.get('data_next_reset')))
reset_date = time.strftime("%Y-%b-%d %a", reset_date)
print("VPS Location:", data.get("node_datacenter"))
ip_str = "".join(data.get("ip_addresses"))
print("IP:", ip_str)
print(
    "Monthly_data_Plan: ",
    monthly_data_plan,
    "\nMonthly_data_Used: ",
    monthly_data_used,
    "\nData Usage:",
    "%" + "%.1f" % percentage(data.get("data_counter"), data.get("plan_monthly_data")),
)
print("reset date:", reset_date)
