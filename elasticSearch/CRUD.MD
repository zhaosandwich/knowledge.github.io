#elasticsearch
##Index
- 创建   
    curl -X PUT 'localhost:9200/weather'        
    创建  
    ```
    Index=weather 
    ```          
    返回      
    ```
    {
      "acknowledged":true,
      "shards_acknowledged":true
    }
    ```
    
             
- 删除   
    curl -X DELETE 'localhost:9200/weather' 
    
##Document
- 创建
```
curl -X PUT 'localhost:9200/accounts' -d '
{
  "mappings": {
    "person": {
      "properties": {
        "user": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "title": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "desc": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        }
      }
    }
  }
}
'
index=accounts,Type=person,Type里面有三个字段user、title、desc,字段类型是text
```

- 新增记录          
```
curl -X PUT 'localhost:9200/accounts/person/1'-d '
  {
    "user": "张三",
    "title": "工程师",
    "desc": "数据库管理"
  }' 

返回
{
  "_index":"accounts",
  "_type":"person",
  "_id":"1",
  "_version":1,
  "result":"created",
  "_shards":{"total":2,"successful":1,"failed":0},
  "created":true
}
地址中account是index,person是document，1是id
```         

如果不指定id，新增数据请求method=post
```
curl -X POST 'localhost:9200/accounts/person' -d '
{
  "user": "李四",
  "title": "工程师",
  "desc": "系统管理"
}'
```

- 查询记录(id)          
```
curl 'localhost:9200/accounts/person/1'
{
  "_index" : "accounts",
  "_type" : "person",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理"
  }
}

```

- 查询所有记录
```
    curl 'localhost:9200/accounts/person/_search'               
    /Index/Type/_search,就返回document全部记录
```

- 删除记录          

```
    curl -X DELETE 'localhost:9200/accounts/person/1'
```
- 更新记录
```
    curl -X PUT 'localhost:9200/accounts/person/1' -d '
    {
        "user" : "张三",
        "title" : "工程师",
        "desc" : "数据库管理，软件开发"
    }'
```
- 全文搜索
```
curl 'localhost:9200/accounts/person/_search' -d '
{
    "query":{"match":{"desc":"软件"}}
}'

* ES默认是一次返回10条结果，可以通过size改变设置
curl 'localhost:9200/accounts/person/_search' -d '
{
    "query":{"match":{"desc":"软件"}}，
    “size”:1
}'

* 分页位移(默认位置从0开始)
curl 'localhost:9200/accounts/person/_search' -d '
{
  "query" : { "match" : { "desc" : "管理" }},
  "from": 1,
  "size": 1
}'

* 逻辑运算
** or 软件或系统
curl 'localhost:9200/accounts/person/_search' -d '
{
  "query" : { "match" : { "desc" : "软件 系统" }}
}'

** and 必须使用布尔查询多个关键词
curl 'localhost:9200/accounts/person/_search' -d '
{
    "query":{
        "bool":{
            "must":[
                { "match":{"desc":"软件"}}，
                { “match”:{"desc":"系统"}}
            ]
        }
    }
}'

```


    

    
    

        

      
 

 