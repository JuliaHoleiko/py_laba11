import re
from zipfile import ZipFile
with ZipFile("access_log_Jul95.zip") as zip:
    zip.extractall()

logs_file = open("access_log_Jul95.txt", "r")
logs_list = logs_file.readlines()

# task was - 08/Mar/2004:05:10:27 до 12/Mar/2004:16:21:50
# but my file is from Jul 1995
# so I decided to use requests from 08/Jul/1995:05:10:27 до 12/Jul/1995:16:21:50

regex_for_right_date_and_unsuccessful_req = re.compile(".*(\\[08/Jul/1995:(05:10:2[7-9]|0[6-9]:[0-5][0-9]|1[0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9])|"
                                                       "(\\[09/Jul/1995:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])|"
                                                       "(\\[1[0-1]/Jul/1995:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9])|"
                                                       "(\\[12/Jul/1995:(0[0-9]:[0-5][0-9]:[0-5][0-9]|1[0-5]:[0-5][0-9]:[0-5][0-9]|16:([0-1][0-9]:[0-5][0-9]|20:[0-5][0-9]|21:[0-4]:[0-9]|21:50)))).*\"\\s[4-5]\\d{2}.*")
regex_for_machine_name = ' - - \\[| '

result = {}
for i in logs_list:
    request_matches = re.match(regex_for_right_date_and_unsuccessful_req, i)
    if request_matches:
        machine_name = re.split(regex_for_machine_name, request_matches.group())[0]
        result[machine_name] = result.get(machine_name, 0) + 1


for keys, values in result.items():
    print(f"{keys} - {values}")
