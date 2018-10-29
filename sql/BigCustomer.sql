-- Create table
create table SD_T_BIGCUSTOMER
(
  id           VARCHAR2(32) default sys_guid() not null,
  code         VARCHAR2(10),
  name         VARCHAR2(50),
  send_pattern VARCHAR2(20),
  type         VARCHAR2(10),
  linkman      VARCHAR2(8),
  phone        NUMBER,
  address      VARCHAR2(300),
  ems_code     VARCHAR2(10),
  states       VARCHAR2(10),
  manage_date  VARCHAR2(10),
  region_code  VARCHAR2(20),
  region_name  VARCHAR2(20)
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
comment on table SD_T_BIGCUSTOMER
  is '山东 渠道管理 - 大客户 门店资料';
-- Add comments to the columns 
comment on column SD_T_BIGCUSTOMER.code
  is '大客户编码';
comment on column SD_T_BIGCUSTOMER.name
  is '大客户名称';
comment on column SD_T_BIGCUSTOMER.send_pattern
  is '分发模式';
comment on column SD_T_BIGCUSTOMER.type
  is '渠道类型';
comment on column SD_T_BIGCUSTOMER.linkman
  is '联系人';
comment on column SD_T_BIGCUSTOMER.phone
  is '联系电话';
comment on column SD_T_BIGCUSTOMER.address
  is '联系地址';
comment on column SD_T_BIGCUSTOMER.ems_code
  is '邮政编码';
comment on column SD_T_BIGCUSTOMER.states
  is '状态';
comment on column SD_T_BIGCUSTOMER.manage_date
  is '日期';
comment on column SD_T_BIGCUSTOMER.region_code
  is '地区编码';
comment on column SD_T_BIGCUSTOMER.region_name
  is '地区名称';
-- Create/Recreate primary, unique and foreign key constraints 
alter table SD_T_BIGCUSTOMER
  add constraint SD_T_BIGCUSTOMER_PK primary key (ID)
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
