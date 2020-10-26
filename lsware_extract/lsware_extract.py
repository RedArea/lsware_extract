"""
    1. input parameter options
    2. parameter option validity check
        - Required Option : 
            - type : all, part, partial
            - in
            - media : image, video, audio, mobile
            - log
        - Conditionally required option : "type = all -> out"
    3. if do not exist log file, create it
    4. random time sleep and 
    5. if type is all
        - if media is image
            - in의 filename에 .dna 붙인 dna 파일 생성
        - if media is video
            - in의 filename의 dna 파일 생성
    6. if type is part
        - cubrid query 
    7. write log


컨텐츠를 input으로 받아서 database랑 비교
 -> 결과값을 log에 저장

컨텐츠 특징정보 db save
all = [yyyy-mm-dd hh:mm:ss(starttime), input_file_path, yyyy-mm-dd hh:mm:ss(endtime), errmsg]
-type all -media video -in "e:\pes\test\video\V380\369552.avi" -log "E:\pes_run\PES-2017-FF-089\log\PES-2017-FF-089_V_X3350.log" -out "E:\pes_run\PES-2017-FF-089\DNA"
-type all -media image -in "D:\PES_TEST\SRC\image\641145" -log "D:\PES_TEST\PES-2013-FF-045\LOG\PES-2013-FF-045_I_X350.log" -out "D:\PES_TEST\PES-2013-FF-045\DNA\image"
    -> 641145.dna 로 출력

part= [yyyy-mm-dd hh:mm:ss(starttime), input_file_path, yyyy-mm-dd hh:mm:ss(querytime), return_value, endtime, errmsg]
-type part -media video -in "e:\pes\test\video\V380\369552.avi" -log "E:\pes_run\PES-2017-FF-089\log\PES-2017-FF-089_V_X3310.log"

wget https://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-release-2-1.el6.ius.noarch.rpm
yum install -y ./ius-release-2-1.el6.ius.noarch.rpm 
yum install –y python36u python36u–libs python36u–devel python36u–pip
which python
ln -s python3.6 python
python --version

yum install -y gcc 

tar xvfz cubrid-python-src-8.4.0.0001.tar.gz
cd cubrid-python-src
python setup.py build
python setup.py install
"""

…or create a new repository on the command line
echo "# lsware_extract" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/RedArea/lsware_extract.git
git push -u origin main
