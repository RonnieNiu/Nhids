一、NIDS 关联 HIDS 项目说明：
====
在一定时间间隔内，分别取NIDS和HIDS告警事件，比如取15分钟（此值在conf/setting.py下配置）
进行资产关联，关联逻辑如下：
1.取hids的datasrcip,即源IP，与NIDS的srcip比较，看是否相等，如果相等说明此源ip至少在hids和nids分别产生了告警，认为这是一个可以关联的事件；
2.如果1不满足，则判断hids agentip 是否与nids srcip相等，如果相等，说明此agent不但在hids层面产生了告警 ，同时作为srcip 在nids
层面发起了攻击，常见如自己被沦陷，然后作为跳板横向渗透，认为是一个可关联的告警；
3.如果1和2都不满足，则判断hids agentip 是否与nids destip
是否相等，如果相等，说明此agent受到了不同源ip的攻击，也可以作为一个可关联的告警；

以上告警还需要对级别进行定级，方面运营

