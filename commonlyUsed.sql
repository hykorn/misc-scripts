select * from elementlevel;
select * from element where elementname like '%CELL_NUMBER%';
select * from element where elementid='405503';
select * from element where levelid='-1' AND categorynumber='12';
select count(*) from element where categorynumber=5;
select * from element where elementname like '%\_1900' ESCAPE '\' and levelid=-1;
select * from attribute where attributename = 'OutputPower';
select * from formatgroup where formatgroupid=9;
select * from attribute where lower(attributename) like lower('%DTGPEHMissingNBR%');
select * from attribute where isrelational = '1';
select * from attribute where attributeid='90801';
select * from attribute where attributename='SAC';
select * from continuousattribute where attributeid=133;
select * from continuousvalues where attributeid='74102' and elementid='405373';
select * from continuousvalues where elementid='405156' and validfrom='25-Nov-13';
select * from continuousvalues where validfrom='04-Sep-13';
select * from attributelevels where attributeid>='73700';
select * from calculatedattribute where attributeid='92034';
select * from calculatedattributedefinitions where attributeid='92034';
select * from thresholdattribute where attributeid='92202';
select * from discretevalues where attributeid like '74102%'  and elementid='405373';
select * from discretevalues where validitydate like '25-NOV-13%';
select * from discretevalues_freq where attributeid like '736%' and doublevalue!=0;
select * from continuousvalues where attributeid='133';
select * from taskcauseactions;
SELECT * FROM taskproblem order by problemid desc;
SELECT * FROM taskcause where causeid >= 0;
SELECT * FROM taskaction where actionid >= 0;
Select * from dbadmin_version_hist;
select count(*) from qt_layer3msg;
select a1.attributename, c1.consolidateddefinition from attribute a1 left join calculatedattribute c1 on a1.attributeid = c1.attributeid 
where a1.attributetype = 2 and  c1.consolidateddefinition is null;
SELECT * FROM V$VERSION;
SELECT Machine, OSUser, Username Schema
FROM gv$session
WHERE Username LIKE '%OWNER%'
ORDER BY 3,2,1;

select * from datasource;
select * from datasourcename;
exec loading.purgedatasource(56);

BEGIN
--v_AttributeName := 'OutputPower';
--Config.AddContinuousAttribute(p_AttributeName => 'OutputPower',	
--                              p_DataType => Common.DataTypeDouble,
--                              p_LevelName => 'Sector',	p_Protected => TRUE	);
--Config.SetAttributeFormatGroup(p_AttributeName => 'OutputPower',
--                                   p_FormatGroupName => 'Long');
--Config.LinkAttributeToGroup(p_AttributeName=>'OutputPower', p_GroupName => 'Core');

Config.AddContinuousAttribute(p_AttributeName => 'PilotPower',	
                              p_DataType => Common.DataTypeDouble,
                              p_LevelName => 'Sector',	p_Protected => TRUE	);
Config.SetAttributeFormatGroup(p_AttributeName => 'PilotPower',
                               p_FormatGroupName => 'Transmit Power');
								   
Config.SetAttributeDescription(p_AttributeName => 'PilotPower', 
                               p_Description => 'Primary Common Pilot Channel (P-CPICH) Power [dBm]');

Config.LinkAttributeToGroup(p_AttributeName => 'PilotPower', p_GroupName => 'Core');

--COMMIT;
END;

DECLARE
v_AttributeName Attribute.AttributeName%TYPE;
BEGIN
v_AttributeName := 'OutputPower';
Config.UnLinkAttributeFromGroup(p_AttributeName=>v_AttributeName, p_GroupName => 'Core');
END;

DECLARE
v_AttributeName Attribute.AttributeName%TYPE;

BEGIN
v_AttributeName := 'PM_2G_DROP_TCH_ERICSSON';
Config.UnlinkAttribute_Level_Cat(p_AttributeName => v_AttributeName, p_CategoryName =>'WCDMA', p_levelName =>'Sector');
Config.DeleteAttribute(p_AttributeName => v_AttributeName);

v_AttributeName := 'PM_2G_DROP_TCH_ERICSSON';
Config.AddKPIAttribute(p_AttributeName => v_AttributeName, p_Type => Common.AttributeTypeCalculated, p_Definition => 'ROUND((100 * (CELTCHF_TFNDROP + CELTCHF_TFNDROPSUB + CELTCHH_THNDROP + CELTCHH_THNDROPSUB) / NULLIF(((CELTCHF_TFCASSALL + CELTCHF_TFCASSALLSUB + CELTCHH_THCASSALL + CELTCHH_TFCASSALLSUB + (NCELLREL_SUMOHOSUCC-NICELASS_SUMIHOSUCBCL-NICELASS_SUMIHOSUCWCL) - (NECELLREL_SUMEOHSUCC-NECELASS_SUMEHOSUCBCL-NECELASS_SUMEHOSUCWCL))),0)),4)');
Config.LinkAttribute_Level_Cat(p_AttributeName => v_AttributeName, p_CategoryName =>'GSM', p_levelName =>'Sector');

commit;
END;

BEGIN
CONFIG.AddTaskType(p_TaskTypeName => 'Availability', p_TaskCodeDefinition => 'Availability');
COMMIT;
END;

