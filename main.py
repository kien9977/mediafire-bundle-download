import requests
import demjson
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from itertools import chain

BASE_FOLDER = "C:\\Users\\AFVN\\Desktop"

def get_folder_list(folder_name, folder_key):
    url = "https://www.mediafire.com/api/1.4/folder/get_content.php?r=dsqq&content_type=folders&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=" + folder_key + "&response_format=json"
    print(folder_key)
    payload = {}
    headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Cookie': '__cf_bm=Fxawl2gOtjgtBHDg.zL4MINBh1T7qRaCK3w6BtjK93s-1638632409-0-Ad7mL4yMmk85QaFOEFS/XxPw9MZvVpV4W/XbwjXwJg5YvPW6iR4xuH60fURS350t7RN+KROC8reNyY6l7G588Pw=; conv_tracking_data-2=%7B%22mf_source%22%3A%22regular_download-34%22%2C%22mf_content%22%3A%22Free%22%2C%22mf_medium%22%3A%22windows%5C%2FChrome%22%2C%22mf_campaign%22%3A%22eznzzn1xe32c3pd%22%2C%22mf_term%22%3A%2284b82b95f6c5895e8d1a3ee150cbe5ce%22%7D; ukey=r0q66c68r1gauzduebqauyiw610dj1cv'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    a = demjson.decode(response.text)

    print(a)

    list_folder = {}
    for i in range(0, len(a['response']['folder_content']['folders']), 1):
        list_folder[a['response']['folder_content']['folders'][i]['folderkey']] = folder_name+"\\"+a['response']['folder_content']['folders'][i]['name']
    return list_folder




# url = "https://www.mediafire.com/api/1.4/folder/get_content.php?r=uewo&content_type=folders&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=ymjifn3k3qx4o&response_format=json"
#
# payload={}
# headers = {
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
#     'Accept': '*/*',
#     'Cache-Control': 'no-cache',
#     'X-Requested-With': 'XMLHttpRequest',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
#     'Cookie': '__cf_bm=UDRL6_C4VNXs08WhFLIZJy1NXL4chfLox3cIBDsZzkc-1638631091-0-AT0Tx0fk6rZfLwUbmVb5sCq/HnJ2NANfJC3fsZoYhoIhwetiKsmmlA5J/WKE5sIfsf3o3pj5wg6bSn+MrZ0BSKY=; conv_tracking_data-2=%7B%22mf_source%22%3A%22regular_download-34%22%2C%22mf_content%22%3A%22Free%22%2C%22mf_medium%22%3A%22windows%5C%2FChrome%22%2C%22mf_campaign%22%3A%22eznzzn1xe32c3pd%22%2C%22mf_term%22%3A%2284b82b95f6c5895e8d1a3ee150cbe5ce%22%7D; ukey=r0q66c68r1gauzduebqauyiw610dj1cv'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# a = demjson.decode(response.text)
#
#
#
# i = 0
# while a['response']['folder_content']['folders'][i]:
#     print(a['response']['folder_content']['folders'][i]['name'])
#
#     folder_arr = []
#     if not os.path.exists(BASE_FOLDER+"/"+a['response']['folder_content']['folders'][i]['name']):
#         os.mkdir(BASE_FOLDER+"/"+a['response']['folder_content']['folders'][i]['name'])
#
#     b = get_folder_list(a['response']['folder_content']['folders'][i]['folderkey'])
#
#     if(len(b) == 0):
#
#
#     i += 1


key_init = "ymjifn3k3qx4o"
folder_list_init = []
i = 0

folder_list_init.append({})
folder_list_init[i] = get_folder_list("MEDIAFIRE", key_init)


siz = len(folder_list_init[i])
temp = folder_list_init[i]
while True:

    if(siz > 0):
        print("Cap: "+str(i))
        i += 1
        folder_list_init.append({})
        for j in range(0, siz):
            t = get_folder_list(temp.get(list(temp)[j]), list(temp)[j])

            print(list(temp)[j])
            if(len(folder_list_init[i]) == 0):
                folder_list_init[i] = t
            else:
                folder_list_init[i].update(t)
        # update head
        siz = len(folder_list_init[i])
        temp = folder_list_init[i]
    else:
        break
print(folder_list_init)


# create folder
all = {}
for i in range (0, len(folder_list_init)):
    all.update(folder_list_init[i])

print(all)

for i in all.values():
    print(os.path.join(BASE_FOLDER, i))
    if not os.path.exists(os.path.join(BASE_FOLDER, i)):
        os.mkdir(os.path.join(BASE_FOLDER, i))

# get link
list_file = {}
for i in all.keys():
    url = "https://www.mediafire.com/api/1.4/folder/get_content.php?r=ozhn&content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=" + i + "&response_format=json"

    payload = {}
    headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Cookie': '__cf_bm=OUqZcROJZjEQIaGJ3cRz1utfiHCVG3XQEGSeoY._JB8-1638638408-0-AVbUS8tMBEtEm7Wn8Dp0x3F90WY2WV4HVPTcb2fXoSFd2/jKCRauCbhLkB3qKl59tlZJreSftbqjl2Ogt2ZXoK0=; conv_tracking_data-2=%7B%22mf_source%22%3A%22regular_download-34%22%2C%22mf_content%22%3A%22Free%22%2C%22mf_medium%22%3A%22windows%5C%2FChrome%22%2C%22mf_campaign%22%3A%22eznzzn1xe32c3pd%22%2C%22mf_term%22%3A%2284b82b95f6c5895e8d1a3ee150cbe5ce%22%7D; ukey=r0q66c68r1gauzduebqauyiw610dj1cv'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    a = demjson.decode(response.text)

    print(a)


    for j in tqdm(range(0, len(a['response']['folder_content']['files']), 1)):
        list_file[a['response']['folder_content']['files'][j]['filename']] = all[i] + "\\" + a['response']['folder_content']['files'][j]['links']['normal_download']

print(list_file)



list_download_able = {}
for i in tqdm(list_file.keys()):
    payload = {}
    headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Cookie': '__cf_bm=Fxawl2gOtjgtBHDg.zL4MINBh1T7qRaCK3w6BtjK93s-1638632409-0-Ad7mL4yMmk85QaFOEFS/XxPw9MZvVpV4W/XbwjXwJg5YvPW6iR4xuH60fURS350t7RN+KROC8reNyY6l7G588Pw=; conv_tracking_data-2=%7B%22mf_source%22%3A%22regular_download-34%22%2C%22mf_content%22%3A%22Free%22%2C%22mf_medium%22%3A%22windows%5C%2FChrome%22%2C%22mf_campaign%22%3A%22eznzzn1xe32c3pd%22%2C%22mf_term%22%3A%2284b82b95f6c5895e8d1a3ee150cbe5ce%22%7D; ukey=r0q66c68r1gauzduebqauyiw610dj1cv'
    }

    req = requests.request("GET", list_file[i], headers=headers, data=payload)

    # print(req.text)
    soup = BeautifulSoup(req.text, "html.parser")
    dom = etree.HTML(str(soup))
    # print(dom.xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/form/div/a[2]/@href')[0])

    link = ""

    try:
        link = dom.xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/form/div/a[2]/@href')[0]

        urllib.request.urlretrieve(link, BASE_FOLDER + "\\" + i)

        print(link + " downloaded to: " + BASE_FOLDER + "\\" + i)
    except:
        link = ""

    list_download_able[i] = link


print(list_download_able)