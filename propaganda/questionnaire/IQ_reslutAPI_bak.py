#!/usr/bin/env python
# encoding:gb2312

'''
@author: GOD_miemie
@file: IQ_reslutAPI.py
@time: 2017/9/3 ����1:25
'''

from collections import deque
from urllib import urlencode

import requests
from lxml import etree

request_urls = deque()
options_list = deque()

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		   'Accept-Encoding': 'gzip, deflate',
		   'Accept-Language': 'zh-CN,zh;q=0.8',
		   'Cache-Control': 'max-age=0',
		   'Connection': 'keep-alive',
		   'Content-Type': 'application/x-www-form-urlencoded',
		   'Cookie': '',
		   'Host': 'www.iqeq.com.cn',
		   'Origin': 'http://www.iqeq.com.cn',
		   'Referer': '',
		   'Upgrade-Insecure-Requests': '1',
		   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


def u_s_change(string):
	if string is not None:
		if isinstance(string, unicode):
			return string.encode("gb2312")
		else:
			return string
	return ""


def IQ_reslut(options):
	options_list.extend(options)
	request_urls.append('http://www.iqeq.com.cn/ti-1.aspx')
	for i in range(2, 7):
		url = 'http://www.iqeq.com.cn/ti%d.aspx' % i
		request_urls.append(url)
	request_urls.append('http://www.iqeq.com.cn/jieguo.aspx')
	request_urls.append('http://www.iqeq.com.cn/chengji.aspx')
	req = requests.get(request_urls.popleft())
	sessionIDKey = req.cookies.get_dict().keys()[0]
	sessionIDValue = req.cookies.get_dict()[sessionIDKey]
	headers['Cookie'] = '%s=%s' % (sessionIDKey, sessionIDValue)
	headers['Referer'] = u_s_change(req.url)
	options_requset(req.text.encode(req.encoding).decode('gb2312'))


# ���õ��ýӿ��Լ��趨cookie


def options_requset(page_souce):
	if len(options_list) > 0:

		# ��ȡѡ����Ϣ
		options_dict = options_list.popleft()

		# ��ȡҳ��hidden��ǩ �������Է�����
		links = way_thinking(page_souce=page_souce)
		if links is not None and len(links) > 0:
			for link in links:
				# ��ȡhidden������ӵ�data��ȥ
				options_dict[link.attrib['name']] = link.attrib['value']
		# ��ȡ�ύ����
		submit_link = submit_crawl(page_souce=page_souce)
		submit_key = submit_link[0].attrib['name']
		submit_value = submit_link[0].attrib['value']
		submit_value = u_s_change(submit_value)

		# ��submit��ǩ�е�������ӵ�data��ȥ
		options_dict[submit_key] = submit_value

		# ��ȡ������url
		next_url = request_urls.popleft()

		# ��������ע��post ��Ҫ����urlת��  ************************* ע�� ע��
		req = requests.post(next_url, urlencode(options_dict), headers=headers)
		headers['Referer'] = u_s_change(req.url)

		# ת��ݹ�
		page_html = req.text.encode(req.encoding).decode('gb2312')
		options_requset(page_html)


	else:
		# �������ȡ�� ���ҷ���
		seltor = etree.HTML(page_souce)
		namelink = seltor.xpath('''//input[@type='hidden']''')
		user_name = namelink[0].tail
		link = seltor.xpath('''//span[@class='hongda']''')

		total_scroe = link[0].text
		left = link[1].text
		right = link[2].text
		comment = link[2].tail

		print 'hi~ %s %s, your left is %s & your rigth is %s & %s' % (user_name, total_scroe, left, right, comment)


def way_thinking(page_souce):
	seletor = etree.HTML(page_souce)
	link = seletor.xpath('''//input[@type='hidden']''')
	return link


def submit_crawl(page_souce):
	seletor = etree.HTML(page_souce)
	links = seletor.xpath('''//input[@type='submit']''')
	return links


if __name__ == '__main__':
	list = deque()
	option_1 = {'TI1': 'V1', 'TI2': 'V1', 'TI3': 'V1', 'TI4': 'V1', 'TI5': 'V1', 'TI6': 'V1', 'TI7': 'V1', 'TI8': 'V1',
				'TI9': 'V1', 'TI10': 'V1'}
	option_2 = {'TI11': 'V1', 'TI12': 'V1', 'TI13': 'V1', 'TI14': 'V1', 'TI15': 'V1', 'TI16': 'V1', 'TI17': 'V1',
				'TI18': 'V1',
				'TI19': 'V1', 'TI20': 'V1'}
	option_3 = {'TI21': 'V1', 'TI22': 'V1', 'TI23': 'V1', 'TI24': 'V1', 'TI25': 'V1', 'TI26': 'V1', 'TI27': 'V1',
				'TI28': 'V1',
				'TI29': 'V1', 'TI30': 'V1'}
	option_4 = {'TI31': 'V1', 'TI32': 'V1', 'TI33': 'V1', 'TI34': 'V1', 'TI35': 'V1', 'TI36': 'V1', 'TI37': 'V1',
				'TI38': 'V1',
				'TI39': 'V1', 'TI40': 'V1'}
	option_5 = {'TI41': 'V1', 'TI42': 'V1', 'TI43': 'V1', 'TI44': 'V1', 'TI45': 'V1', 'TI46': 'V1', 'TI47': 'V1',
				'TI48': 'V1',
				'TI49': 'V1', 'TI50': 'V1'}
	option_6 = {'TI51': 'V1', 'TI52': 'V1', 'TI53': 'V1', 'TI54': 'V1', 'TI55': 'V1', 'TI56': 'V1', 'TI57': 'V1',
				'TI58': 'V1',
				'TI59': 'V1', 'TI60': 'V1'}

	year = 16
	sex = '��'
	name = '����'
	prov = '����'
	cit = '����'
	emailto = 'test@mail.com'

	option_7 = {
		'old': year,
		'sex': sex,
		'name': name,
		'prov': prov,
		'cit': cit,
		'emailto': emailto,
	}
	list.append(option_1)
	list.append(option_2)
	list.append(option_3)
	list.append(option_4)
	list.append(option_5)
	list.append(option_6)
	list.append(option_7)

	IQ_reslut(list)
