from itertools import chain
import requests
import demjson
import os

from tqdm import tqdm

folder_list_init = [{'qx06x59kla5m8': 'MEDIAFIRE\\01. Phan mem ve ebook cho Windows', '398bwis9gg32l': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao', 'uxtkt4bhtscx4': 'MEDIAFIRE\\03. Truyen Ngon Tinh', 'hy0ahzytfb29b': 'MEDIAFIRE\\04. ebook Van Hoc, Xa Hoi, Tinh Cam', 'ccmdfx7e1sirs': 'MEDIAFIRE\\05. Sac Tinh Convert', '29cnqpdubiyag': 'MEDIAFIRE\\10.000 ebook epub', '135rr15eybcpg': 'MEDIAFIRE\\Bookworms Wordwise'}, {'3w2ofdo28thsz': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\01. Truyen Hoan Thanh', 'awasrv4y0tths': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\02. Truyen Dang Dich', 'g3d6d9c222evu': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\03. Truyen Kiem Hiep Co Dien', '3a3kfg3fnp6bv': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\04. Truyen Convert', 'i6n6fta1akt44': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\Truyen Convert hoan 2020-2021', '7g3bybib2af34': 'MEDIAFIRE\\03. Truyen Ngon Tinh\\2018', 'zaf1dour2swvf': 'MEDIAFIRE\\03. Truyen Ngon Tinh\\Top Ngon Tinh TQ', '9j9n7topc2r86': 'MEDIAFIRE\\04. ebook Van Hoc, Xa Hoi, Tinh Cam\\New', 'n1b1684mlisbx': 'MEDIAFIRE\\04. ebook Van Hoc, Xa Hoi, Tinh Cam\\Thai sản, Thai giáo, dạy trẻ', 'z0fivflf6z9gz': 'MEDIAFIRE\\05. Sac Tinh Convert\\2020-2021', 'a97ao3shz9n2h': 'MEDIAFIRE\\05. Sac Tinh Convert\\Chon loc (sắc nặng có nội dung)'}, {'nt2ro28wo23eb': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\01. Truyen Hoan Thanh\\Chon loc (theo danh gia ca nhan)', 'bib8p013qwpdy': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\01. Truyen Hoan Thanh\\ebooks by Hoa Lan', '5gpf3f1hjzbdt': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\01. Truyen Hoan Thanh\\pdf', 'dso6ysa5a25dt': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\03. Truyen Kiem Hiep Co Dien\\Co Long', '9q990ecysqub6': 'MEDIAFIRE\\04. ebook Van Hoc, Xa Hoi, Tinh Cam\\Thai sản, Thai giáo, dạy trẻ\\White noise'}, {'bd2sg36meufc4': 'MEDIAFIRE\\02. Truyen Tien Hiep, Kiem Hiep, Huyen Ao\\01. Truyen Hoan Thanh\\Chon loc (theo danh gia ca nhan)\\Hạng 1 (độc đáo, sáng tạo, ko giống truyện khác)'}, {}]
BASE_FOLDER = "C:\\Users\\AFVN\\Desktop\\"



all = {}
for i in range (0, len(folder_list_init)):
    all.update(folder_list_init[i])
print(all)


for i in all.values():
    print(os.path.join(BASE_FOLDER, i))
    if not os.path.exists(os.path.join(BASE_FOLDER, i)):
        os.mkdir(os.path.join(BASE_FOLDER, i))

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
        list_file[all[i] + "\\" + a['response']['folder_content']['files'][j]['filename']] = a['response']['folder_content']['files'][j]['links']['normal_download']

print(list_file)