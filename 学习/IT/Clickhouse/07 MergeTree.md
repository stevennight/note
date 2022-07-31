# 07 MergeTree

## 表引擎

表引擎决定：

1. 数据存储方式以及位置
2. 数据的查询支持以及支持方式
3. 并发数据访问
4. 索引使用
5. 是否可以执行多线程请求
6. 数据复制参数

4类表引擎：

1. MergeTree（系列） 【核心】
    1. *MergeTree
    2. 通用以及功能强大
    3. 快速插入并且进行后续处理（OLAP）
    4. 支持数据复制、数据分片，以Replicated作为前缀命名的引擎
2. 日志
    1. *Log
    2. 快速插入并整体读取
3. 集成引擎
    1. Kafka, MySQL, ODBC, JDBC, HDFS
4. 其他特定功能引擎
    1. Distributed, MaterializedView, Dictonary, Merge, File, Null, Set, Join, URL, View, Memory, Buffer…

### 虚拟列

尽量不要使用

```sql
select x+y from t_null;
```

## MergeTree

创建：Order By必须，其他的包括主键都是可选的

```sql
# 示例
create table t_stock (
	id UInt32,
	sku_id String,
	total_amount Decimal(16,2),
	create_time Datetime
) engine=MergeTree()
partition by toYYYYMMDD(create_time)
primary key (id)
order by (id,sku_id);
```

### partition by分区键

默认不填，则不分区。

存储在对应目录下，文件命名示例：

```sql
# 分区命名
20200601_1_1_0
<分区名>_<最小块>_<最大块>_<合并次数>

# 分区数据文件
data.bin # 实际存储数据（压缩，高效，得益于列式存储）
primary.idx # 主键索引
data.mrk3 # 索引文件与数据文件的连接
minmax_create_time.idx # 根据分区键，建立的最大最小值索引
column.txt # 列信息
count.txt # 计数信息
```

查询数据时，也是按分区分好（官方客户端）。

### Merge操作

数据结构：类似LSM树

插入数据的时候，不会直接写入硬盘，而是写入到内存中（一棵新的树）；内存写入硬盘的操作，Merge操作。

合并的操作：后台会在一定时间间隔后进行一次合并。也可以手动合并，手动合并指令

```sql
optimize table t_stock final;
```

### Order By

通过min, max查找分区，需要有序

### Primary Key

不是必须的，也不是唯一的 不同于MySQL等数据库的主键

对排序键做索引

稀疏索引，按照索引粒度（index granularity）划分分区，官方默认值：8192

<span style="color: gold">
待确定：在一级索引下，建立 跳数索引（跳跃表），可进一步加快
</span>

### 二级索引

```sql
index secondIndex total_amount TYPE minmax GRANULARITY 5
```

### TTL

作用与：字段、表

字段过期了，将设置为默认值；列在整个表中的所有值都过期了，将删除整列

TTL不能作用与主键

### Sample By 数据抽样

```sql
# 表中指定列
sample by intHash32(UserID)
# 查询指定采样率
select Title, count(*) AS PageViews From hits_v1
sample 0.1 # 采样10%的数据，或者可以设置具体条数
...
```