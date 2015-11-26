# -*-coding:utf-8 -*-
# coding=UTF-8


__author__ = 'klein'


def mbean_mail_title(mbean_name):

    mail_title = u'[Dealbean] {0} 開團成功通知'.format(mbean_name)

    return mail_title.encode('utf-8')

def mbean_mail_content(user, mbean_name, link):

    mail_content = u'{0} 您好 <br /><br />'.format(user)
    mail_content += u'會收到這封信是因為您在 <a href="https://dealbeanapp.herokuapp.com/"> Dealbean </a> 進行開團，<br />'
    mail_content += u'開團的名稱為：「<a href="http://dealbean.herokuapp.com/suborder/{0}/">{1} </a>」。<br />'.format(link, mbean_name)
    mail_content += u'非常感謝您的使用，希望您能開團成功。 <br /><br /><br />'
    mail_content += u'希望您有美好的一天！ <br />'
    mail_content += u'Best regard <br />'
    mail_content += u'DealBean 團隊敬上 <br />'

    return mail_content
