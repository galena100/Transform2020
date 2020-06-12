/*

--------------------------------------------------
--1. used to export to csv for dataset -  single hole
--------------------------------------------------

--litho
select HOLEID,GEOLFROM, GEOLTO, [VALUE] from 
(
select HOLEID,GEOLFROM, GEOLTO, [VALUE] 
,min(PRIORITY) over(partition by HOLEID,GEOLFROM,GEOLTO) min_prty
,PRIORITY
from GEODETAILS
where HOLEID ='GL1010' and NAME = 'CLLI_Litho_Type' 
) a
where PRIORITY = min_prty
order by HOLEID, GEOLFROM,PRIORITY

--geophys
select -1* DEPTH DEPTH,[VALUE]
from QV_GEOPHYSDETAILS 
where HOLEID = 'GL1010' and NAME = 'GRDE_gapi'
--where HOLEID in ('GL1010','GL1012','GL1015') and NAME IN  ('GRDE_gapi','DENB_g_cc','MC2F_us_f','CADE_mm')

--dictionary
select LOOKUP, [DESCRIPTION] from QV_VS_LOOKUP_RW 
where FIELDNAME = 'CLLI_Litho_Type' and LOOKUP in (select distinct VALUE from GEODETAILS where HOLEID = 'GL1010' and NAME = 'CLLI_Litho_Type')

--------------------------------------------------
--used to export to csv for dataset -  three holes
--------------------------------------------------

--litho2
select case 
        when HOLEID = 'GL1010' THEN 'test001'
        when HOLEID = 'GL1012' THEN 'test002'
        else 'test003'
        end as HOLEID
    ,GEOLFROM
    , GEOLTO
    , [VALUE] 
from 
(
select HOLEID,GEOLFROM, GEOLTO, [VALUE] 
,min(PRIORITY) over(partition by HOLEID,GEOLFROM,GEOLTO) min_prty
,PRIORITY
from GEODETAILS
where HOLEID in ('GL1010','GL1012','GL1015') and NAME = 'CLLI_Litho_Type' 
) a
where PRIORITY = min_prty
order by HOLEID, GEOLFROM,PRIORITY


--geophys2


select * from 
(
select case 
        when HOLEID = 'GL1010' THEN 'test001'
        when HOLEID = 'GL1012' THEN 'test002'
        else 'test003'
        end as HOLEID

, -1 * DEPTH DEPTH,NAME, [VALUE]
from QV_GEOPHYSDETAILS 
--where HOLEID = 'GL1010' and NAME = 'GRDE_gapi'
where HOLEID in ('GL1010','GL1012','GL1015') and NAME IN  ('GRDE_gapi','DENB_g_cc','MC2F_us_f','CADE_mm')
) c
pivot(
        min(VALUE) for NAME in (GRDE_gapi,DENB_g_cc,MC2F_us_f,CADE_mm)
    ) as piv
order by HOLEID, DEPTH desc


--dictionary2

select LOOKUP, [DESCRIPTION] from QV_VS_LOOKUP_RW 
where FIELDNAME = 'CLLI_Litho_Type' and LOOKUP in (select distinct VALUE from GEODETAILS where HOLEID in ('GL1010','GL1012','GL1015') and NAME = 'CLLI_Litho_Type')

-------------------------------------------------------------------------------
--3. used to export to single gamma as filtered csv for dataset -  single hole
-------------------------------------------------------------------------------

select -1* DEPTH DEPTH,[VALUE]
from QV_GEOPHYSDETAILS 
where HOLEID = 'GL1010' and NAME = 'GRDE_gapi' and DEPTH % 0.05 = 0 --the modulus filters out 4/5 of the data.

*/