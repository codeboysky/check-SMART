# 监控nvme硬盘是否存在故障
> 该程序利用smart用于监控nvme固态硬盘的
>Media and Data Integrity Errors(0E) 和 Available Spare(03)

## 安装
1. 安装[smartctl](https://sourceforge.net/projects/smartmontools/files/)
2. 安装[Python 3.7+](https://www.python.org/)

## 运行
1. 打开任务计划程序
2. 创建任务
3. 填写计划名称
<br/><img src="https://github.com/codeboysky/check-SMART/blob/master/resource/1.png" width="450em"></img>
5. 创建触发器,当前示例是每天每8小时检查一次，其中8小时是**手动输入**的
<br/><img src="https://github.com/codeboysky/check-SMART/blob/master/resource/2.png" width="450em"></img>
6. 创建操作，执行程序选择pythonw可以无黑框运行，参数分别是脚本路径、smartctl路径、待检磁盘
<br/><img src="https://github.com/codeboysky/check-SMART/blob/master/resource/3.png" width="400em"></img>
7. 修改条件和设置
<br/><img src="https://github.com/codeboysky/check-SMART/blob/master/resource/4.png" width="400em"></img>
<br/><img src="https://github.com/codeboysky/check-SMART/blob/master/resource/5.png" width="400em"></img>

## 命令说明
**示例**：pythonw.exe "d:\check_smart.py" smartctl c:

| 序号 | 参数 | 说明 |
| --- | --- | --- |
| 1 | pythonw.exe | pythonw 无黑框运行 |
| 2 | "d:\check_smart.py" | 脚本路径 |
| 3 | smartctl | smartctl路径,示例中smartctl使用了环境变量，所以不是全路径 |
| 4 | c: |磁盘路径 <br/> linux - /dev/nvme0 <br/> windows - c:  |
