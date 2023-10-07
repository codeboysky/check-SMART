#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging as log
import subprocess
import sys
import time
import tkinter as tk
from tkinter import messagebox

# 日志，暂时输出到控制台
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def obtain_value(exec_path, disk_path):
    """
    用于获取 Media and Data Integrity Errors 和 Available Spare数值
    :param exec_path:smartctl 路径
    :param disk_path:要监控的磁盘
    :return: 返回 Media and Data Integrity Errors 和 去处%号的Available Spare
    """
    cmd = "\"" + exec_path + "\" -A " + disk_path
    try:
        # 执行程序并捕获标准输出
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True, check=True)
        log.debug(result.stdout)
    except subprocess.CalledProcessError as e:
        log.info(f"命令执行失败，返回码：{e.returncode}")
        log.info("标准输出：")
        log.info(e.stdout)
        log.info("标准错误输出：")
        log.info(e.stderr)
        raise e
    lines = result.stdout.split("\n")
    for i in lines:
        line = i
        if line.startswith("Media and Data Integrity Errors:"):
            madie = int(line.split(":")[1].strip())
        if line.startswith("Available Spare:"):
            avs = int(line.split(":")[1].strip().rstrip("%"))
    return madie, avs


def check_smart(madie, avs):
    """
    判断是否出现问题，Media and Data Integrity Errors大于0就有问题
    或者Available Spare小于100说明备份空间被使用了就需要关注下可能会出现问题
    :param madie:Media and Data Integrity Errors大小
    :param avs:Available Spare去除%号的值
    """
    if madie > 0 or avs < 100:
        report_error(madie, avs)


def report_error(madie, avs):
    """
    提示出现故障信息
    :param madie:Media and Data Integrity Errors大小
    :param avs:Available Spare去除%号的值
    """
    msgbox("SMART异常，联系管理员")


def msgbox(msg):
    """
    异常提示
    :param msg:
    """
    root = tk.Tk()
    root.title("SMART异常")
    root.geometry('0x0+999999+0')
    messagebox.showerror("SMART异常", msg)
    root.destroy()


if __name__ == '__main__':
    err_flg = True
    # 监控程序如果连续5次出现异常则提示监控程序可能出问题了，比如参数配置不对、少安装东西
    for i in range(5):
        try:
            exe_path = sys.argv[1]
            disk_path = sys.argv[2]

            madie, avs = obtain_value(exe_path, disk_path)
            check_smart(madie, avs)
            err_flg = False
            break
        except Exception as e:
            log.error(f"发生了异常：{str(e)}", exc_info=True)
            time.sleep(30)
    if err_flg:
        msgbox("SMART检测程序异常，联系管理员")
