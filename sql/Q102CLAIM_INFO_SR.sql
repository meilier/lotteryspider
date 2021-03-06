CREATE TABLE CLAIM_PRIZE_INFO_SR 
(
  ID VARCHAR2(32 BYTE) DEFAULT sys_guid() NOT NULL 
, PROVINCE_CODE NUMBER 
, PROVINCE_NAME VARCHAR2(20 BYTE) 
, CITY_CODE NUMBER 
, CITY_NAME VARCHAR2(20 BYTE) 
, COUNTRY_CODE NUMBER 
, COUNTRY_NAME VARCHAR2(20 BYTE) 
, ORGANIZATION_TYPE VARCHAR2(2 BYTE) 
, ORGANIZATION_CODE NUMBER 
, ORGANIZATION_NAME VARCHAR2(32 BYTE) 
, CLAIM_DATE VARCHAR2(10 BYTE)
, GAME_CODE NUMBER 
, GAME_NAME VARCHAR2(32 BYTE) 
, TERMINAL_CODE NUMBER 
, FACE_VALUE NUMBER 
, PACKAGE_NUMBER NUMBER 
, TICKET_NUMBER NUMBER 
, PRIZE_CLASS NUMBER 
, PRIZE_MONEY NUMBER 
, STORE_CODE NUMBER 
, ACTIVE_TIME VARCHAR2(10 BYTE) 
, PACKAGE_STATE VARCHAR2(8 BYTE)  
, MANAGE_DATE VARCHAR2(10 BYTE) 
, CONSTRAINT CLAIM_PRIZE_INFO_SR_PK PRIMARY KEY 
  (
    ID 
  )
  USING INDEX 
  (
      CREATE UNIQUE INDEX CLAIM_PRIZE_INFO_SR_PK ON CLAIM_PRIZE_INFO_SR (ID ASC) 
      LOGGING 
      TABLESPACE SPORTS_LOTTERY_DATA 
      PCTFREE 10 
      INITRANS 2 
      STORAGE 
      ( 
        BUFFER_POOL DEFAULT 
      ) 
      NOPARALLEL 
  )
  ENABLE 
) 
LOGGING 
TABLESPACE SPORTS_LOTTERY_DATA 
PCTFREE 10 
INITRANS 1 
STORAGE 
( 
  BUFFER_POOL DEFAULT 
) 
NOCOMPRESS 
NOPARALLEL;
