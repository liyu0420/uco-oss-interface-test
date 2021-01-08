import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import readConfig
import os
import getpathInfo

read_conf = readConfig.ReadConfig()
path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')


def send_mail():
    # 邮箱的服务地址
    gserver = read_conf.get_email('gserver')  # 从配置文件中读取，邮件主题
    gport = int(read_conf.get_email('gport'))
    username = read_conf.get_email('username')
    password = read_conf.get_email('password')

    filename = os.path.join(report_path, "report.html")

    f = open(filename, 'rb')
    mail_body = f.read()
    f.close()

    # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEMultipart()
    # 邮件正文
    msg.attach(MIMEText(mail_body, _subtype='html', _charset='utf-8'))
    # 添加附件
    att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="%s"' % 'report.html'
    msg.attach(att1)

    msg['from'] = read_conf.get_email('mailfrom')
    msg['to'] = ','.join(read_conf.get_email('mailto').split(','))
    # 抄送
    msg['Cc'] = read_conf.get_email('mailcc')
    msg['Reply-To'] = read_conf.get_email('mailfrom')
    msg['Subject'] = read_conf.get_email('subject')

    try:
        smtp = smtplib.SMTP(gserver, gport)
        smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(read_conf.get_email('mailfrom'), read_conf.get_email('mailto').split(','), msg.as_string())
        smtp.quit()
        smtp.close()
        print("邮件发送成功")
    except Exception as err:
        print("Send mail failed. ", err)


if __name__ == "__main__":
    send_mail()
