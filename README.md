# 概要 A03210348
利用py2neo与neo4j进行连接，创建关于python课程的知识图谱
## main.py A03210348
主函数，即起到与neo4j连接的作用
## data.json A03210348
数据源
## fix.py A03210348
防止data.json的id不是自增1，即检查文件格式
## http://localhost:7474
在此网站输入 
`MATCH(n) RETURN(n)` 
即可查看最终效果
