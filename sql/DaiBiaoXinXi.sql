-- Create table
create table SD_T_DAIBIAOXINXI
(
  id                             VARCHAR2(32) default sys_guid() not null,
  code                           VARCHAR2(10),
  name                           VARCHAR2(50),
  fullname                       VARCHAR2(50),
  pro_name                       VARCHAR2(10),
  city_name                      VARCHAR2(10),
  county_name                    VARCHAR2(10),
  city_division                  VARCHAR2(20),
  county_division                VARCHAR2(20),
  relationship                   VARCHAR2(20),
  sr_states                      VARCHAR2(8),
  person_name                    VARCHAR2(50),
  person_id                      VARCHAR2(20),
  address                        VARCHAR2(300),
  ems_code                       VARCHAR2(30),
  phone                          VARCHAR2(100),
  send_pattern                   VARCHAR2(20),
  out_min_money                  NUMBER,
  transfer_min_money             NUMBER,
  auto_collection                VARCHAR2(10),
  channel_1                      VARCHAR2(20),
  channel_2                      VARCHAR2(20),
  channel_3                      VARCHAR2(20),
  distribution_1                 VARCHAR2(20),
  distribution_2                 VARCHAR2(20),
  distribution_3                 VARCHAR2(20),
  order_warehouse                VARCHAR2(20),
  refund_ticket_permit           VARCHAR2(10),
  submit_order_permit            VARCHAR2(10),
  order_automatic_permit         VARCHAR2(10),
  sale_commission_proportion     NUMBER,
  sale_commission_modul          VARCHAR2(20),
  sale_commission_pay            VARCHAR2(10),
  duijiang_commission_proportion NUMBER,
  duijiang_commission_modul      VARCHAR2(20),
  duijiang_commission_way        VARCHAR2(10),
  duijiang_commission_pay        VARCHAR2(20),
  manage_commission_proportion   NUMBER,
  manage_commission_modul        VARCHAR2(20),
  manage_commission_way          VARCHAR2(10),
  manage_commission_pay          VARCHAR2(20),
  duijiang_max_money             NUMBER,
  duijiang_min_money             NUMBER,
  duijiang_pay_sure_money        NUMBER,
  cycle                          NUMBER,
  duijiang_times                 NUMBER,
  clock_time                     VARCHAR2(10),
  transfer_out_permit            VARCHAR2(10),
  transfer_in_permit             VARCHAR2(10),
  receive_person                 VARCHAR2(50),
  receive_address                VARCHAR2(300),
  receive_phone                  VARCHAR2(100),
  manage_date                    VARCHAR2(10)
)
tablespace SPORTS_LOTTERY_DATA
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
-- Add comments to the table 
comment on table SD_T_DAIBIAOXINXI
  is '山东 渠道管理 - 销售代表信息 门店资料';
-- Add comments to the columns 
comment on column SD_T_DAIBIAOXINXI.code
  is 'SR编号';
comment on column SD_T_DAIBIAOXINXI.name
  is 'SR名称';
comment on column SD_T_DAIBIAOXINXI.fullname
  is 'SR全称';
comment on column SD_T_DAIBIAOXINXI.pro_name
  is '省中心';
comment on column SD_T_DAIBIAOXINXI.city_name
  is '市中心';
comment on column SD_T_DAIBIAOXINXI.county_name
  is '县中心';
comment on column SD_T_DAIBIAOXINXI.city_division
  is '市区划';
comment on column SD_T_DAIBIAOXINXI.county_division
  is '县区划';
comment on column SD_T_DAIBIAOXINXI.relationship
  is '竞争关系';
comment on column SD_T_DAIBIAOXINXI.sr_states
  is 'SR状态';
comment on column SD_T_DAIBIAOXINXI.person_name
  is '业主姓名';
comment on column SD_T_DAIBIAOXINXI.person_id
  is '业主证件号';
comment on column SD_T_DAIBIAOXINXI.address
  is '联系地址';
comment on column SD_T_DAIBIAOXINXI.ems_code
  is '邮政编码';
comment on column SD_T_DAIBIAOXINXI.phone
  is '联系方式';
comment on column SD_T_DAIBIAOXINXI.send_pattern
  is '分发模式';
comment on column SD_T_DAIBIAOXINXI.out_min_money
  is '转出保底金额';
comment on column SD_T_DAIBIAOXINXI.transfer_min_money
  is '转账保底金额';
comment on column SD_T_DAIBIAOXINXI.auto_collection
  is '自动归集';
comment on column SD_T_DAIBIAOXINXI.channel_1
  is '销售渠道1';
comment on column SD_T_DAIBIAOXINXI.channel_2
  is '销售渠道2';
comment on column SD_T_DAIBIAOXINXI.channel_3
  is '销售渠道3';
comment on column SD_T_DAIBIAOXINXI.distribution_1
  is '配送SR1';
comment on column SD_T_DAIBIAOXINXI.distribution_2
  is '配送SR2';
comment on column SD_T_DAIBIAOXINXI.distribution_3
  is '配送SR3';
comment on column SD_T_DAIBIAOXINXI.order_warehouse
  is '订货仓库';
comment on column SD_T_DAIBIAOXINXI.refund_ticket_permit
  is '领退票许可';
comment on column SD_T_DAIBIAOXINXI.submit_order_permit
  is '订单提交许可';
comment on column SD_T_DAIBIAOXINXI.order_automatic_permit
  is '订单自动接收许可';
comment on column SD_T_DAIBIAOXINXI.sale_commission_proportion
  is '销售佣金比例';
comment on column SD_T_DAIBIAOXINXI.sale_commission_modul
  is '销售佣金模式';
comment on column SD_T_DAIBIAOXINXI.sale_commission_pay
  is '销售佣金值支付方式';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_proportion
  is '兑奖佣金比例';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_modul
  is '兑奖佣金模式';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_way
  is '兑奖佣金结算规则';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_pay
  is '兑奖佣金支付方式';
comment on column SD_T_DAIBIAOXINXI.manage_commission_proportion
  is '管理佣金比例';
comment on column SD_T_DAIBIAOXINXI.manage_commission_modul
  is '管理佣金模式';
comment on column SD_T_DAIBIAOXINXI.manage_commission_way
  is '管理佣金结算规则';
comment on column SD_T_DAIBIAOXINXI.manage_commission_pay
  is '管理佣金制度方式';
comment on column SD_T_DAIBIAOXINXI.duijiang_max_money
  is '兑奖最高限额';
comment on column SD_T_DAIBIAOXINXI.duijiang_min_money
  is '兑奖最低限额';
comment on column SD_T_DAIBIAOXINXI.duijiang_pay_sure_money
  is '兑奖支付确认金额';
comment on column SD_T_DAIBIAOXINXI.cycle
  is '周期';
comment on column SD_T_DAIBIAOXINXI.duijiang_times
  is '兑奖次数';
comment on column SD_T_DAIBIAOXINXI.clock_time
  is '锁定时长';
comment on column SD_T_DAIBIAOXINXI.transfer_out_permit
  is '转账转出许可';
comment on column SD_T_DAIBIAOXINXI.transfer_in_permit
  is '转账转入许可';
comment on column SD_T_DAIBIAOXINXI.receive_person
  is '配送收货人';
comment on column SD_T_DAIBIAOXINXI.receive_address
  is '配送收货地址';
comment on column SD_T_DAIBIAOXINXI.receive_phone
  is '配送电话（收货人电话）';
comment on column SD_T_DAIBIAOXINXI.manage_date
  is '日期';
-- Create/Recreate primary, unique and foreign key constraints 
alter table SD_T_DAIBIAOXINXI
  add constraint SD_T_DAIBIAOXINXI_PK primary key (ID)
  using index 
  tablespace SPORTS_LOTTERY_DATA
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
