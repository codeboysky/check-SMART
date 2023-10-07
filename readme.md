# 监控nvme硬盘是否存在故障
> 该程序利用smart用于监控nvme固态硬盘的
>Media and Data Integrity Errors(0E) 和 Available Spare(03)

## 安装
1. 安装[smartctl](https://sourceforge.net/projects/smartmontools/files/)
2. 安装[Python 3.7+](https://www.python.org/)

## 运行
1. 打开任务计划程序
2. 创建任务
3. 添加触发条件等
4. 添加执行程序 pythonw.exe "d:\check_smart.py" smartctl c:

## 参数说明
| 参数序号 | 说明 | 示例 |
| --- | --- | --- |
| 1 | smartctl路径 | smartctl.exe | 
| 2 | 磁盘路径 | linux - /dev/nvme0 <br/> windows - c:  |
