from py2neo import Graph, Node, Relationship, NodeMatcher

# 连接图库                            初始化账号密码都是neo4j
from py2neo import Graph, Node, Relationship, NodeMatcher

# 连接图库                            初始化账号密码都是neo4j
graph = Graph('http://127.0.0.1:7474', name="chain", auth=('neo4j', '123456!'))

# 注意使用Python连接neo4j时要首先启动neo4j的服务，否则Python会抛出异常。


# 注意使用Python连接neo4j时要首先启动neo4j的服务，否则Python会抛出异常。

from py2neo import Graph, Node, Relationship, NodeMatcher
graph.delete_all()
# 头实体


# 文中相当于这样一个三元组 <邯郸市，属于，河北省>。当然现实场景头尾实体和关系不是自己指定的，需要进行挖掘的。这里就是举个例子理解下。
