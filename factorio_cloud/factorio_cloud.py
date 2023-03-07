"""
本程序用于更正异星工厂（Factorio）steam云存档配置信息的问题

QuainK
2023.02.22

需求：
remotecache.vdf里含有每个存档的信息，
但是有时因为网络问题，云同步失败，导致存档变化了，这个配置信息还留在这里，形成“幽灵存档配置”，
时间久了，就会有成百上千条无效的存档信息。
尝试过直接修改删除存档信息，但是steam云同步又恢复出来。

解决：
1. 启动游戏
2. 在游戏内随便新建一个正常的存档，以此作为模板
3. 读取云存档配置信息里的存档文件名（路径名）
4. 从正常的存档复制，用这些文件名保存到steam云存档目录
5. 退出游戏
6. 让steam云同步，刷新这些存档信息，从而将“幽灵存档配置”变成“正常存档配置”
7. 进游戏再删除这些存档
8. 退出游戏，刷新云存档配置信息，大功告成
"""

import os

if __name__ == '__main__':
    # 实际路径
    # file_path = "C:/Games/Steam/userdata/415824425/427520/remotecache.vdf"
    # 程序本地路径
    file_path = "./remotecache.vdf"
    # 不管操作哪个文件，都要记得最后执行close方法
    # 以字符串只读方式，打开云存档配置信息文件
    config_file = open(file_path, mode='r', encoding='utf-8')
    try:
        # 获取字符串流
        file_txt = config_file.read()
        # 移除行首tab和空格
        formatted_str = file_txt.expandtabs(0)
        # 按行转换成列表
        str_arr = formatted_str.splitlines()

        # 初始化目标文件名列表
        result_arr = []
        # 遍历云存档配置信息列表
        for str_item in str_arr:
            # 找到含有路径/文件名的那个元素
            if str_item.find('\"Factorio/saves/') > -1:
                # 移除目录只保留文件名
                # 移除首尾多余的双引号
                # 得到的结果放进目标文件名列表
                result_arr.append(str_item.lstrip('\"Factorio/saves/').rstrip('\"'))

        # 遍历目标文件名列表
        for result_item in result_arr:
            # 实际路径
            # directory = 'C:/Users/QuainK/AppData/Roaming/Factorio/saves/'
            # 程序本地路径
            directory = './saves/'
            # 如果程序本地路径没有这个文件夹，则创建，否则直接使用
            if os.path.exists(directory) is False:
                os.mkdir('./saves')

            # 目标文件的保存路径
            path = directory + result_item
            # 正常存档模板路径
            game_save_template_path = './game_save_template.zip'
            # 打开正常存档模板
            game_save_template = open(game_save_template_path, mode='rb')
            # 打开目标文件，准备复制写入
            new_file = open(path, mode='wb+')
            try:
                # 写入
                new_file.write(game_save_template.read())
            finally:
                # 关闭目标文件
                if new_file:
                    new_file.close()
                # 关闭正常存档模板
                if game_save_template:
                    game_save_template.close()

    finally:
        # 关闭云存档配置信息文件
        if config_file:
            config_file.close()
