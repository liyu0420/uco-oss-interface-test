from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom
import readConfig
import common.Email as Email
from runCase import AllTest
import runAll

on_off = readConfig.ReadConfig().get_email('on_off')
case_switch = readConfig.ReadConfig().get_cases('caseswitch')


class RunMain:
    def run(self):
        # 判断跑全部的case还是部分的
        if case_switch == 'on':
            AllTest.run()
        else:
            runAll.run()
        # 判断邮件发送的开关
        if on_off == 'on':
            Email.send_mail()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
        # 定时任务
        pythoncom.CoInitialize()
        scheduler = BlockingScheduler()
        scheduler.add_job(RunMain().run, 'cron', day_of_week='1-5', hour=8, minute=30)
        scheduler.start()


if __name__ == '__main__':
    RunMain().run()
