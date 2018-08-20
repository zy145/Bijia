

import requests
url = 'https://search.smzdm.com/?c=home&s=%E6%89%8B%E6%9C%BA'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'https://www.smzdm.com/',
    'Cookie': '__ckguid=u8C5g3yfw5Xtv6TiW5UX3U5; device_id=30857790141534582747656167270b7e2e306e69f1ee075002b422ac4a; __jsluid=e4f08d2de2a72a296455fabce6576d26; s_his=%E6%89%8B%E6%9C%BA; ss_ab=ss43; zdm_qd=%7B%7D; smzdm_user_view=42E6B5333296022453E97C12A1E62DEC; smzdm_user_source=C18A4244F28CA8D71329D1BC6F626662; wt3_eid=%3B999768690672041%7C2153458303100994721%232153458303100283481; _ga=GA1.2.2592511.1534583090; _gid=GA1.2.120998831.1534583090; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1534582596,1534646307; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1534646316; amvid=ae3cc6f74f8f5de7ca1c866057c57042'

}

resp = requests.get(url, headers=headers)


print(resp.content)