import pandas as pd
import time
import os


def grid(write_list):
    write_list = [str(x) for x in write_list]
    write_string = " | ".join(write_list)
    write_string = "| " + write_string + " |"
    write_string = write_string + "\n"
    return write_string


def markdown_write_main():
    
    # 删除文件
    try:
        os.remove("./source/info.md")
    except IOError:
        pass

    # 排序
    data = pd.read_excel('./source/job_info.xlsx', index_col=None)

    # 写一个简单的Markdown文档
    with open('source/info.md', 'a', encoding='utf-8') as f:

        # 写上标题
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(round(time.time()*1000))/1000))
        f.writelines(f'## {current_time}\t今日实习信息一览，为您展示上海市的实习：')

        # 写上引用
        f.writelines(f"\n\n> 数据摘自[「Boss直聘」](https://zhipin.com)，每日通知您最新工作资讯，详情请查看附件。\n\n")

        # 写上表格标题 / 写上表格分隔符
        columns = data.columns
        columns = grid(columns)
        plt = ['---' for _ in range(data.shape[1])]
        plt = grid(plt)
        f.writelines(columns)
        f.writelines(plt)
        
        # 写上正文
        cols = 0
        for x in data.values:
            if cols == 10:
                break
            x = grid(x)
            f.writelines(x)
            cols += 1

        # 最后的结尾
        f.writelines("\n### 今天的工作推送到此结束，祝您生活愉快！")

    # 写入一个csv文件
    data.to_csv("./source/info.csv", index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    markdown_write_main()
