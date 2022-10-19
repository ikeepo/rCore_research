"""create files for daily record

Usage
-----
    cd path/to/scripts && python create_daily_files.py
"""
import os
from mdutils.mdutils import MdUtils
import datetime
import argparse
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
TODAY = datetime.date.today().strftime("%Y%m%d")
DP_WORKSPACE = Path().absolute().as_posix()

def create_md_date(fp):
    """
    mdutils只支持 level 1 之后只能是 level 2
    """
    mdFile = MdUtils(file_name=fp,title=f'Daily Record {dt}')
    mdFile.new_header(level=2, title='流水', add_table_of_contents="n")
    mdFile.new_line("\n")
    mdFile.new_header(level=2, title='知识点', add_table_of_contents="n")
    mdFile.new_line("\n")
    mdFile.new_header(level=2, title='总结', add_table_of_contents="n")
    mdFile.new_line("\n")
    mdFile.new_header(level=2, title='下次学习入口', add_table_of_contents="n")
    mdFile.new_line("\n")
    mdFile.create_md_file()


def create_md(fp, head):
    mdFile = MdUtils(file_name=fp,title=head)
    mdFile.create_md_file()

def update_index(dt):
    fp_index = f"{DP_WORKSPACE}/record/daily/index.md"
    mdFile = MdUtils(file_name=fp_index)
    data = mdFile.read_md_file(fp_index)
    dt_ls = data.split("\n")
    dts_info = [i for i in dt_ls if i != ""]
    dts = [i.split("[")[1][:8] for i in dts_info[1:]]
    if dt in dts:
        logging.warning(f"{dt} is already append to {fp_index}")
    else:
        last_id = dt_ls[-2].split(".")[0]
        dt_ls.append(f"{int(last_id)+1}. [{dt}]({dt}/{dt}.md)")
        dt_ls.append("")
        data_new = "\n".join(dt_ls)
        # 创建新index
        mdFile_new = MdUtils(file_name=fp_index)
        mdFile_new.write(data_new)
        mdFile_new.create_md_file()
        logging.info(f"{dt} append to {fp_index}")


def create_daily_record_template(dt, n):
    dp = f"{DP_WORKSPACE}/record/daily/{dt}"
    os.makedirs(dp, exist_ok=True) 
    fp_date = f"{dp}/{dt}.md"
    create_md_date(fp_date)
    logging.info(f"create {fp_date}")
    for i in range(n):
        fp_knowledge = f"{dp}/Understand_Something_{i}.md"
        create_md(fp_knowledge, "Understand Something")
        logging.info(f"create {fp_knowledge}")
    update_index(dt)

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dt", default=TODAY)
    parser.add_argument("-n", default=2)
    args = parser.parse_args()
    dt = args.dt
    n = args.n


    create_daily_record_template(dt, n)