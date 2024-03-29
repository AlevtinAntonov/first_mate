query_child = """ 
SELECT 
    PERSON.LAST_NAME, 
    PERSON.FIRST_NAME, 
    PERSON.PATRONYMIC, 
    PERSON.DATE_OF_BIRTH, 
    DOCUMENT.DOCUMENT_SERIES, 
    DOCUMENT.DOCUMENT_NUMBER, 
    DOCUMENT.DOCUMENT_ISSUED_BY, 
    DOCUMENT.DOCUMENT_DATE_OF_ISSUE,
    DOCUMENT.PLACE_OF_BIRTH, 
    GENDER.GENDER_NAME,
    FOCUS.FOCUS_NAME, 
    MOVEMENT.STATEMENT_NUMBER,
    MOVEMENT.STATEMENT_DATE, 
    MOVEMENT.CONTRACT_BEGIN_DATE,
    MOVEMENT.CONTRACT_NUMBER,
    MOVEMENT.CONTRACT_DATE,
    MOVEMENT.CONTRACT_BEGIN_DATE,
    FOCUS.PROGRAM_NAME,
    VALIDITY.VALIDITY_NAME,
    VALIDITY.VALIDITY_INT,
    MODE.MODE_NAME,
    TEAM.TEAM_NAME,
    PARENTAL_FEE.ORDER_NUMBER,
    PARENTAL_FEE.ORDER_DATE,
    PARENTAL_FEE.ORDER_NAME,
    PARENTAL_FEE.PARENTAL_FEE_rate,
    DOCUMENT.DOCUMENT_ASSEMBLY_RECORD 
FROM REFERRAL
    JOIN CHILD ON REFERRAL.CHILD_ID = CHILD.CHILD_ID
    JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID
    JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID
    JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
    JOIN FOCUS ON REFERRAL.FOCUS_ID = FOCUS.FOCUS_ID
    JOIN MOVEMENT ON REFERRAL.REFERRAL_ID = MOVEMENT.REFERRAL_ID
    JOIN AGE ON REFERRAL.AGE_ID = AGE.AGE_ID
    JOIN VALIDITY ON AGE.VALIDITY_ID = VALIDITY.VALIDITY_ID
    JOIN MODE ON REFERRAL.MODE_ID = MODE.MODE_ID
    JOIN TEAM ON CHILD.TEAM_ID = TEAM.TEAM_ID
    JOIN PARENTAL_FEE ON TEAM.PARENTAL_FEE_ID = PARENTAL_FEE.PARENTAL_FEE_ID
WHERE REFERRAL.REFERRAL_ID = ?
ORDER BY MOVEMENT.MOVEMENT_ID DESC;
"""

query_organization = """
SELECT
    ORGANIZATION.FULL_NAME,
    ORGANIZATION.SHORT_NAME,
    ORGANIZATION.LEGAL_ADDRESS,
    ORGANIZATION.POST_ADDRESS,
    ORGANIZATION.phone,
    ORGANIZATION.email,
    ORGANIZATION.OKPO,
    ORGANIZATION.OGRN,
    ORGANIZATION.OKOGU,
    ORGANIZATION.INN,
    ORGANIZATION.KPP,
    ORGANIZATION.POSITION_NAME,
    ORGANIZATION.BOSS_LAST_NAME,
    ORGANIZATION.BOSS_FIRST_NAME,
    ORGANIZATION.BOSS_PATRONYMIC,
    ORGANIZATION.BENEFICIARY,
    ORGANIZATION.BANK_NAME,
    ORGANIZATION.BIC,
    ORGANIZATION.COR_ACCOUNT,
    ORGANIZATION.ACCOUNT,
    ORGANIZATION.INITIALS,
    GENDER.GENDER_NAME,
    ORGANIZATION.LICENSE_NUMBER,
    ORGANIZATION.LICENSE_DATE,
    ORGANIZATION.REGION_NAME
FROM REFERRAL
    JOIN building ON REFERRAL.building_id = building.building_id
    join organization on building.organization_id = organization.organization_id
    join gender on organization.boss_gender_id = gender.gender_id
WHERE REFERRAL.REFERRAL_ID = ?;
"""

query_parent = """ 
SELECT 
    PERSON.LAST_NAME, 
    PERSON.FIRST_NAME, 
    PERSON.PATRONYMIC, 
    PERSON.DATE_OF_BIRTH, 
    DOCUMENT.DOCUMENT_SERIES, 
    DOCUMENT.DOCUMENT_NUMBER, 
    DOCUMENT.DOCUMENT_ISSUED_BY, 
    DOCUMENT.DOCUMENT_DATE_OF_ISSUE,
    GENDER.GENDER_NAME,
    PHONE.PHONE_NUMBER,
    EMAIL.EMAIL_NAME,
    PERSON.INITIALS,
    CITIZENSHIP.CITIZENSHIP_FULL_NAME,
    PARENTS.SVO_PARTICIPANT,
    STATUS.STATUS_NAME
FROM PERSON
    JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID
    JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
    JOIN CITIZENSHIP ON PERSON.CITIZENSHIP_ID = CITIZENSHIP.CITIZENSHIP_ID
    JOIN PARENTS ON PERSON.PERSON_ID = PARENTS.PERSON_ID
    JOIN STATUS ON PARENTS.STATUS_ID = STATUS.STATUS_ID
    JOIN PHONE ON PARENTS.PARENTS_ID = PHONE.PARENTS_ID
    JOIN EMAIL ON PARENTS.PARENTS_ID = EMAIL.PARENTS_ID
WHERE 
    PERSON.PERSON_ID = ?
    AND PERSON.IS_VISIBLE = TRUE;
        """

query_address = """
SELECT 
    ADDRESS.ZIPCODE,
    ADDRESS.REGION,
    REGION_TYPE.REGION_TYPE_NAME_SHORT,
    ADDRESS.DISTRICT,
    ADDRESS.TOWN,
    TOWN_TYPE.TOWN_TYPE_NAME_SHORT,
    ADDRESS.LOCALITY,
    LOCALITY_TYPE.LOCALITY_TYPE_NAME_SHORT,
    ADDRESS.STREET,
    STREET_TYPE.STREET_TYPE_NAME_SHORT,
    ADDRESS.HOUSE,
    ADDRESS.HOUSE_BODY,
    ADDRESS.HOUSE_LITER,
    ADDRESS.HOUSE_BUILDING,
    ADDRESS.FLAT,
    TOWN_DISTRICT.TOWN_DISTRICT_NAME
FROM 
    %s
    JOIN PERSON_ADDRESS ON %s = PERSON_ADDRESS.PERSON_ID
    JOIN ADDRESS ON PERSON_ADDRESS.ADDRESS_ID = ADDRESS.ADDRESS_ID
    JOIN REGION_TYPE ON ADDRESS.region_type_id = REGION_TYPE.region_type_id
    JOIN TOWN_TYPE ON ADDRESS.town_type_id = TOWN_TYPE.TOWN_TYPE_ID
    JOIN LOCALITY_TYPE ON ADDRESS.LOCALITY_TYPE_id = LOCALITY_TYPE.LOCALITY_TYPE_ID
    JOIN STREET_TYPE ON ADDRESS.STREET_TYPE_id = STREET_TYPE.STREET_TYPE_ID
    JOIN TOWN_DISTRICT ON ADDRESS.TOWN_DISTRICT_id = TOWN_DISTRICT.TOWN_DISTRICT_ID
WHERE 
    %s = ?
    AND %s = TRUE
    AND ADDRESS.IS_VISIBLE = TRUE;
"""

query_compensation = """
SELECT 
    COMPENSATION_STATEMENT.COMPENSATION_STATEMENT_NUMBER,
    COMPENSATION_STATEMENT.COMPENSATION_STATEMENT_DATE,
    COMPENSATION_STATEMENT.COMPENSATION_STATEMENT_START_DATE,
    COMPENSATION.COMPENSATION_SIZE
    
FROM PERSON
    JOIN COMPENSATION_STATEMENT ON PERSON.PERSON_ID = COMPENSATION_STATEMENT.PERSON_ID
    JOIN COMPENSATION ON COMPENSATION_STATEMENT.COMPENSATION_ID = COMPENSATION.COMPENSATION_ID
WHERE 
    PERSON.PERSON_ID = ?
    AND PERSON.IS_VISIBLE = TRUE;
"""

query_add_docs = """
SELECT 
    compensation_add_document.add_document_name,
    compensation_add_document.add_document_data
FROM PERSON
    join compensation_statement on person.person_id = compensation_statement.person_id
    join compensation_add_document on compensation_statement.compensation_statement_id = compensation_add_document.compensation_statement_id
WHERE 
    PERSON.PERSON_ID = ?
    AND PERSON.IS_VISIBLE = TRUE;
"""

query_svo = """
SELECT
    PERSON.LAST_NAME, 
    PERSON.FIRST_NAME, 
    PERSON.PATRONYMIC, 
    PERSON.DATE_OF_BIRTH, 
    DOCUMENT.DOCUMENT_SERIES, 
    DOCUMENT.DOCUMENT_NUMBER,
    PERSON.SNIILS, 
    GENDER.GENDER_NAME,
    STATUS.STATUS_NAME

FROM CHILD
    JOIN FAMILY ON CHILD.CHILD_ID = FAMILY.CHILD_ID
    JOIN PARENTS ON FAMILY.PARENTS_ID = PARENTS.PARENTS_ID
    JOIN STATUS ON PARENTS.STATUS_ID = STATUS.STATUS_ID
    JOIN PERSON ON PARENTS.PERSON_ID = PERSON.PERSON_ID
    JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID
    JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
WHERE CHILD.CHILD_ID = ?
    AND PARENTS.SVO_PARTICIPANT = TRUE
    AND PARENTS.IS_VISIBLE = TRUE;
"""

query_find_parental_fee_id = """
SELECT
    PARENTAL_FEE.PARENTAL_FEE_ID
FROM CHILD
    JOIN TEAM ON CHILD.TEAM_ID = TEAM.TEAM_ID
    JOIN PARENTAL_FEE ON TEAM.PARENTAL_FEE_ID = PARENTAL_FEE.PARENTAL_FEE_ID
WHERE CHILD.CHILD_ID = ?;
"""
