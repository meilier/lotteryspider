-- Create table
create table SD_T_MENDIANXINXI
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
  business_type                  VARCHAR2(20),
  site_states                    VARCHAR2(8),
  person_name                    VARCHAR2(50),
  person_id                      VARCHAR2(20),
  address                        VARCHAR2(300),
  phone                          VARCHAR2(100),
  ems_code                       VARCHAR2(30),
  out_min_money                  NUMBER,
  transfer_min_money             NUMBER,
  relationship                   VARCHAR2(20),
  site_level                     VARCHAR2(10),
  channel_1                      VARCHAR2(20),
  channel_2                      VARCHAR2(20),
  channel_3                      VARCHAR2(20),
  send_pattern                   VARCHAR2(20),
  manage_sr                      VARCHAR2(50),
  move_sr1                       VARCHAR2(20),
  move_sr2                       VARCHAR2(20),
  move_sr3                       VARCHAR2(20),
  distribution_1                 VARCHAR2(20),
  distribution_2                 VARCHAR2(20),
  distribution_3                 VARCHAR2(20),
  order_warehouse                VARCHAR2(20),
  refund_ticket_permit           VARCHAR2(10),
  submit_order_permit            VARCHAR2(10),
  sure_active_mony               VARCHAR2(10),
  manual_activation_permit       VARCHAR2(10),
  order_automatic_permit         VARCHAR2(10),
  sale_commission_proportion     NUMBER,
  sale_commission_modul          VARCHAR2(20),
  sale_commission_way            VARCHAR2(10),
  sale_commission_pay            VARCHAR2(20),
  duijiang_commission_proportion NUMBER,
  duijiang_commission_modul      VARCHAR2(20),
  duijiang_commission_way        VARCHAR2(10),
  duijiang_commission_pay        VARCHAR2(20),
  duijiang_max_money             NUMBER,
  duijiang_min_money             NUMBER,
  duijiang_pay_sure_money        NUMBER,
  cycle                          NUMBER,
  duijiang_times                 NUMBER,
  clock_time                     VARCHAR2(10),
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
comment on table SD_T_MENDIANXINXI
  is '山东 渠道管理 - 门店信息 门店资料';
-- Add comments to the columns 
comment on column SD_T_MENDIANXINXI.code
  is '门店编号';
comment on column SD_T_MENDIANXINXI.name
  is '门店名称';
comment on column SD_T_MENDIANXINXI.fullname
  is '门店全称';
comment on column SD_T_MENDIANXINXI.pro_name
  is '省中心';
comment on column SD_T_MENDIANXINXI.city_name
  is '市中心';
comment on column SD_T_MENDIANXINXI.county_name
  is '县中心';
comment on column SD_T_MENDIANXINXI.city_division
  is '市区划';
comment on column SD_T_MENDIANXINXI.county_division
  is '县区划';
comment on column SD_T_MENDIANXINXI.business_type
  is '业务类型';
comment on column SD_T_MENDIANXINXI.site_states
  is '门店状态';
comment on column SD_T_MENDIANXINXI.person_name
  is '业主姓名';
comment on column SD_T_MENDIANXINXI.person_id
  is '业主证件号';
comment on column SD_T_MENDIANXINXI.address
  is '联系地址';
comment on column SD_T_MENDIANXINXI.phone
  is '联系方式';
comment on column SD_T_MENDIANXINXI.ems_code
  is '邮政编码';
comment on column SD_T_MENDIANXINXI.out_min_money
  is '转出保底金额';
comment on column SD_T_MENDIANXINXI.transfer_min_money
  is '转账保底金额';
comment on column SD_T_MENDIANXINXI.relationship
  is '门店竞争关系';
comment on column SD_T_MENDIANXINXI.site_level
  is '门店级别分类';
comment on column SD_T_MENDIANXINXI.channel_1
  is '销售渠道1';
comment on column SD_T_MENDIANXINXI.channel_2
  is '销售渠道2';
comment on column SD_T_MENDIANXINXI.channel_3
  is '销售渠道3';
comment on column SD_T_MENDIANXINXI.send_pattern
  is '分发模式';
comment on column SD_T_MENDIANXINXI.manage_sr
  is '管理-SR';
comment on column SD_T_MENDIANXINXI.move_sr1
  is '转移SR1';
comment on column SD_T_MENDIANXINXI.move_sr2
  is '转移SR2';
comment on column SD_T_MENDIANXINXI.move_sr3
  is '转移SR3';
comment on column SD_T_MENDIANXINXI.distribution_1
  is '配送SR1';
comment on column SD_T_MENDIANXINXI.distribution_2
  is '配送SR2';
comment on column SD_T_MENDIANXINXI.distribution_3
  is '配送SR3';
comment on column SD_T_MENDIANXINXI.order_warehouse
  is '订货仓库';
comment on column SD_T_MENDIANXINXI.refund_ticket_permit
  is '领退票许可';
comment on column SD_T_MENDIANXINXI.submit_order_permit
  is '订单提交许可';
comment on column SD_T_MENDIANXINXI.sure_active_mony
  is '激活确认许可';
comment on column SD_T_MENDIANXINXI.manual_activation_permit
  is '手工激活许可';
comment on column SD_T_MENDIANXINXI.order_automatic_permit
  is '订单自动接收许可';
comment on column SD_T_MENDIANXINXI.sale_commission_proportion
  is '销售佣金比例';
comment on column SD_T_MENDIANXINXI.sale_commission_modul
  is '销售佣金模式';
comment on column SD_T_MENDIANXINXI.sale_commission_way
  is '销售佣金结算规则';
comment on column SD_T_MENDIANXINXI.sale_commission_pay
  is '销售佣金支付方式';
comment on column SD_T_MENDIANXINXI.duijiang_commission_proportion
  is '兑奖佣金比例';
comment on column SD_T_MENDIANXINXI.duijiang_commission_modul
  is '兑奖佣金模式';
comment on column SD_T_MENDIANXINXI.duijiang_commission_way
  is '兑奖佣金结算规则';
comment on column SD_T_MENDIANXINXI.duijiang_commission_pay
  is '兑奖佣金支付方式';
comment on column SD_T_MENDIANXINXI.duijiang_max_money
  is '兑奖佣金最高限额';
comment on column SD_T_MENDIANXINXI.duijiang_min_money
  is '兑奖佣金最低限额';
comment on column SD_T_MENDIANXINXI.duijiang_pay_sure_money
  is '兑奖支付确认金额';
comment on column SD_T_MENDIANXINXI.cycle
  is '周期';
comment on column SD_T_MENDIANXINXI.duijiang_times
  is '兑奖次数';
comment on column SD_T_MENDIANXINXI.clock_time
  is '锁定时长';
comment on column SD_T_MENDIANXINXI.receive_person
  is '配送收货人';
comment on column SD_T_MENDIANXINXI.receive_address
  is '配送收货地址';
comment on column SD_T_MENDIANXINXI.receive_phone
  is '配送电话（收货人电话）';
comment on column SD_T_MENDIANXINXI.manage_date
  is '日期';
-- Create/Recreate primary, unique and foreign key constraints 
alter table SD_T_MENDIANXINXI
  add constraint SD_T_MENDIANXINXI_PK primary key (ID)
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
