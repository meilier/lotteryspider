CREATE TABLE ALLOT_DATA
(
  ID VARCHAR2(32 BYTE) DEFAULT sys_guid() NOT NULL 
, ALLOT_NUMBER NUMBER 
, OUTBOUND_WAREHOUSE VARCHAR2(32 BYTE) 
, INBOUND_WAREHOUSE VARCHAR2(32 BYTE) 
, GAME_CODE NUMBER 
, GAME_NAME VARCHAR2(32 BYTE) 
, ALLOT_CASE_NUMBER NUMBER 
, ALLOT_SCATTERED_PACKAGE NUMBER 
, ALLOT_TOTAL_PACKAGE NUMBER 
, GAME_FACE_VALUE NUMBER 
, ALLOT_TOTAL_MONEY NUMBER 
, MANAGE_DATE VARCHAR2(10 BYTE) 
, CONSTRAINT ALLOT_DATA_PK PRIMARY KEY 
  (
    ID 
  )
  USING INDEX 
  (
      CREATE UNIQUE INDEX ALLOT_DATA_PK ON ALLOT_DATA (ID ASC) 
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
