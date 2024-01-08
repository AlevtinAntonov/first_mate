import os
from datetime import datetime
from docxtpl import DocxTemplate
from number_to_string import get_string_by_number

from app_model.db.db_connect import db
from app_view_model.functions.format_address import format_address
from app_view_model.print_forms.functions.db_queries import query_child, query_organization, query_address, \
    query_parent, query_compensation, query_add_docs, query_svo
from app_view_model.print_forms.functions.print_functions import declension_full_name, decline_organization, \
    decline_position, decline_region


def print_all_forms(child_id, referral_id, person_id, result: dict):
    print(child_id, referral_id, person_id, result)
    with db as cur:
        current_year = datetime.now().year
        applicant_registration_country = child_registration_country = 'Российская Федерация'

        row_child = cur.execute(query_child, (referral_id,)).fetchone()

        birth_certificate_series = row_child[4] if row_child else ''
        birth_certificate_number = row_child[5] if row_child else ''
        birth_certificate_issued_by = row_child[6] if row_child else ''
        birth_certificate_issued_date = row_child[7].strftime('%d.%m.%Y') if row_child else ''
        child_place_of_birth = row_child[8] if row_child else ''
        child_gender = row_child[9] if row_child else ''
        reg_number = row_child[11] if row_child else ''
        reg_date = row_child[12].strftime('%d.%m.%Y') if row_child else ''
        start_date = row_child[13].strftime('%d.%m.%Y') if row_child else ''
        child_type = 'сына' if row_child and child_gender == 'мужской' else 'дочь'

        child_last_name = row_child[0] if row_child else ''
        child_first_name = row_child[1] if row_child else ''
        child_patronymic = row_child[2] if row_child else ''
        child_full_name = ' '.join((child_last_name, child_first_name, child_patronymic)) if row_child else ''
        child_full_name_genitive = declension_full_name(child_full_name,
                                                        'родительный', child_gender) if child_full_name else ''
        child_full_name_accusative = declension_full_name(child_full_name,
                                                          'винительный', child_gender) if child_full_name else ''
        child_birth_date = row_child[3].strftime('%d.%m.%Y') if row_child else ''

        focus_name = row_child[10] if row_child else ''
        agreement_number = row_child[14] if row_child else ''
        agreement_date = row_child[15].strftime('%d.%m.%Y') if row_child else ''
        ending_naming_child = 'ой' if row_child and child_gender == 'женский' else 'ого'
        program_name = row_child[17] if row_child else ''
        validity_name = row_child[18] if row_child else ''
        mode_name = row_child[20] if row_child else ''

        order_number = row_child[22] if row_child else ''
        order_date = row_child[23].strftime('%d.%m.%Y') if row_child else ''
        order_name = row_child[24] if row_child else ''
        parental_fee_rate = row_child[25] if row_child else ''
        parental_fee_rate_in_words = get_string_by_number(parental_fee_rate) if parental_fee_rate else ''

        agreement_start_date = row_child[16].strftime('%d.%m.%Y') if row_child else ''
        calculate_end_date = datetime(datetime.now().year, 8, 31)
        validity_years = row_child[19] if row_child else '1'
        agreement_end_date = calculate_end_date.replace(year=datetime.now().year + int(validity_years)).strftime(
            '%d.%m.%Y')
        team_name = row_child[21] if row_child else ''
        birth_certificate_record_number = row_child[26] if row_child else ''

        row_org = cur.execute(query_organization, (referral_id,)).fetchone()
        organization_full_name = row_org[0] if row_org else ''
        license_date = row_org[23].strftime('%d.%m.%Y') if row_org else ''
        license_number = row_org[22] if row_org else ''
        position_name = row_org[11] if row_org else ''
        position_name_capital = position_name.capitalize() if position_name else ''
        position_name_genitive = decline_position(position_name, 'родительный')
        position_name_dative = decline_position(position_name, 'дательный')
        director_full_name = ' '.join((row_org[12], row_org[13], row_org[14])) if row_org else ''
        director_full_name_genitive = declension_full_name(director_full_name, 'родительный',
                                                           row_org[21]) if director_full_name else ''
        organization_full_name_genitive = decline_organization(organization_full_name,
                                                               'родительный') if organization_full_name else ''
        ending_acting = 'ий' if row_org else ''
        organization_short_name = row_org[1] if row_org else ''
        organization_full_reg_address = row_org[2] if row_org else ''
        organization_phone = row_org[4] if row_org else ''
        okpo_number = row_org[6] if row_org else ''
        okogu_number = row_org[8] if row_org else ''
        ogrn_number = row_org[7] if row_org else ''
        inn_number = row_org[9] if row_org else ''
        region_name = row_org[24] if row_org else ''
        region_name_genitive = decline_region(region_name, 'родительный') if region_name else ''
        kpp_number = row_org[10] if row_org else ''
        director_short_name = ' '.join((row_org[20], row_org[12])) if row_org else ''
        director_full_name_dative = declension_full_name(director_full_name, 'дательный',
                                                         row_org[21]) if director_full_name else ''

        row_parent = cur.execute(query_parent, (person_id,)).fetchone()
        parent_last_name = row_parent[0] if row_parent else ''
        parent_first_name = row_parent[1] if row_parent else ''
        parent_patronymic = row_parent[2] if row_parent else ''
        parent_gender = row_parent[8] if row_parent else ''

        parent_full_name = ' '.join((parent_last_name, parent_first_name, parent_patronymic)) if row_parent else ''
        parent_full_name_genitive = declension_full_name(parent_full_name, 'родительный',
                                                         parent_gender) if parent_full_name else ''
        passport_series = row_parent[4] if row_parent else ''
        passport_number = row_parent[5] if row_parent else ''
        passport_date_of_issue = row_parent[7].strftime('%d.%m.%Y') if row_parent else ''
        passport_issued_by = row_parent[6] if row_parent else ''

        phone_number = row_parent[9] if row_parent else ''
        parent_email = row_parent[10] if row_parent else ''
        ending_female = 'а' if row_parent and parent_gender == 'женский' else ''

        ending_naming = 'ая' if row_parent and parent_gender == 'женский' else 'ый'
        ending_resident = 'ая' if row_parent and parent_gender == 'женский' else 'ий'
        parent_short_name = ' '.join((row_parent[11], row_parent[0])) if row_parent else ''
        father = 'X' if row_parent and row_parent[14] == 'отец' else ''
        mother = 'X' if row_parent and row_parent[14] == 'мать' else ''
        applicant = 'X' if row_parent and row_parent[14] == 'законный представитель' else ''
        parent_citizenship = row_parent[12] if row_parent else ''

        row_svo = cur.execute(query_svo, (child_id,)).fetchone()
        svo_parent_birth_date = row_svo[3].strftime('%d.%m.%Y') if row_svo else ''
        svo_parent_last_name = row_svo[0] if row_svo else ''
        svo_parent_first_name = row_svo[1] if row_svo else ''
        svo_parent_patronymic = row_svo[2] if row_svo else ''
        svo_parent_full_name = ' '.join(
            (svo_parent_last_name, svo_parent_first_name, svo_parent_patronymic)) if row_parent else ''
        svo_parent_passport_data = ' '.join((row_svo[4], row_svo[5])) if row_svo else ''
        svo_parent_snils = row_svo[6] if row_svo else ''
        svo_parent_status = row_svo[8] if row_svo else ''

        row_child_address_reg = cur.execute(
            query_address % ("CHILD", "CHILD.PERSON_ID", "CHILD.CHILD_ID", "ADDRESS.IS_REGISTRATION"),
            (child_id,)).fetchone()
        child_reg_full_address = format_address(row_child_address_reg) if row_child_address_reg else ''
        child_registration_index = row_child_address_reg[0] if row_child_address_reg else ''
        child_registration_region = row_child_address_reg[1] if row_child_address_reg else ''
        child_registration_district = row_child_address_reg[3] if row_child_address_reg else ''
        child_registration_town = row_child_address_reg[4] if row_child_address_reg else ''
        child_registration_street = row_child_address_reg[8] if row_child_address_reg else ''
        child_registration_house = row_child_address_reg[10] if row_child_address_reg else ''
        child_registration_house_body = row_child_address_reg[11] if row_child_address_reg else ''
        child_registration_house_liter = row_child_address_reg[12] if row_child_address_reg else ''
        child_registration_house_build = row_child_address_reg[13] if row_child_address_reg else ''
        child_registration_house_building = ''.join(
            (child_registration_house_body, child_registration_house_liter, child_registration_house_build))
        child_registration_flat = row_child_address_reg[14] if row_child_address_reg else ''
        child_registration_town_district = row_child_address_reg[15] if row_child_address_reg[15] else ''

        row_child_address_fact = cur.execute(
            query_address % ("CHILD", "CHILD.PERSON_ID", "CHILD.CHILD_ID", "ADDRESS.IS_FACT"),
            (child_id,)).fetchone()
        child_fact_full_address = format_address(
            row_child_address_fact) if row_child_address_fact else child_reg_full_address
        child_fact_town = row_child_address_fact[4] if row_child_address_fact else ''
        child_fact_street = row_child_address_fact[8] if row_child_address_fact else ''
        child_fact_house = row_child_address_fact[10] if row_child_address_fact else ''
        child_fact_house_body = row_child_address_fact[11] if row_child_address_fact else ''
        child_fact_house_liter = row_child_address_fact[12] if row_child_address_fact else ''
        child_fact_house_build = row_child_address_fact[13] if row_child_address_fact else ''
        child_fact_house_building = ''.join(
            (child_fact_house_body, child_fact_house_liter, child_fact_house_build))
        child_fact_flat = row_child_address_fact[14] if row_child_address_reg else ''
        child_fact_town_district = row_child_address_fact[15] if row_child_address_fact[15] else ''

        row_parent_address_reg = cur.execute(
            query_address % ("PERSON", "PERSON.PERSON_ID", "PERSON.PERSON_ID", "ADDRESS.IS_REGISTRATION"),
            (person_id,)).fetchone()
        parent_reg_full_address = format_address(row_parent_address_reg) if row_parent_address_reg else ''
        applicant_registration_index = row_parent_address_reg[0] if row_parent_address_reg else ''
        applicant_registration_region = row_parent_address_reg[1] if row_parent_address_reg else ''
        applicant_registration_district = row_parent_address_reg[3] if row_parent_address_reg else ''
        applicant_registration_town = row_parent_address_reg[4] if row_parent_address_reg else ''
        applicant_registration_street = row_parent_address_reg[8] if row_parent_address_reg else ''
        applicant_registration_house = row_parent_address_reg[10] if row_parent_address_reg else ''
        applicant_registration_house_body = row_parent_address_reg[11] if row_parent_address_reg else ''
        applicant_registration_house_liter = row_parent_address_reg[12] if row_parent_address_reg else ''
        applicant_registration_house_build = row_parent_address_reg[13] if row_parent_address_reg else ''
        applicant_registration_house_building = ''.join(
            (applicant_registration_house_body, applicant_registration_house_liter, applicant_registration_house_build))
        applicant_registration_flat = row_parent_address_reg[14] if row_parent_address_reg else ''
        applicant_registration_town_district = row_parent_address_reg[15] if row_parent_address_reg[15] else ''

        row_parent_address_fact = cur.execute(
            query_address % ("PERSON", "PERSON.PERSON_ID", "PERSON.PERSON_ID", "ADDRESS.IS_FACT"),
            (person_id,)).fetchone()
        applicant_fact_town = row_parent_address_fact[4] if row_parent_address_fact else ''
        applicant_fact_street = row_parent_address_fact[8] if row_parent_address_fact else ''
        applicant_fact_house = row_parent_address_fact[10] if row_parent_address_fact else ''
        applicant_fact_house_body = row_parent_address_fact[11] if row_parent_address_fact else ''
        applicant_fact_house_liter = row_parent_address_fact[12] if row_parent_address_fact else ''
        applicant_fact_house_build = row_parent_address_fact[13] if row_parent_address_fact else ''
        applicant_fact_house_building = ''.join(
            (applicant_fact_house_body, applicant_fact_house_liter, applicant_fact_house_build))
        applicant_fact_flat = row_parent_address_fact[14] if row_parent_address_fact else ''
        applicant_fact_town_district = row_parent_address_fact[15] if row_parent_address_fact[15] else ''

        row_compensation = cur.execute(query_compensation, (person_id,)).fetchone()
        order_number_compensation = row_compensation[0] if row_compensation else ''
        order_date_compensation = row_compensation[1].strftime('%d.%m.%Y') if row_compensation else ''
        year_compensation = row_compensation[2].year if row_compensation else ''
        compensation_size = row_compensation[3] if row_compensation else ''

        row_compensation_add_docs = cur.execute(query_add_docs, (person_id,)).fetchall()
        doc_datas = []
        for i in range(1, 7):
            doc_datas.append((row_compensation_add_docs[0], row_compensation_add_docs[1])) if len(
                row_compensation_add_docs) > i else (" ", " ")

        document_1 = doc_datas[0][0] if len(doc_datas) > 0 else ''
        document_2 = doc_datas[1][0] if len(doc_datas) > 1 else ''
        document_3 = doc_datas[2][0] if len(doc_datas) > 2 else ''
        document_4 = doc_datas[3][0] if len(doc_datas) > 3 else ''
        document_5 = doc_datas[4][0] if len(doc_datas) > 4 else ''
        document_6 = doc_datas[5][0] if len(doc_datas) > 5 else ''

        document_details_1 = doc_datas[0][1] if len(doc_datas) > 0 else ''
        document_details_2 = doc_datas[1][1] if len(doc_datas) > 1 else ''
        document_details_3 = doc_datas[2][1] if len(doc_datas) > 2 else ''
        document_details_4 = doc_datas[3][1] if len(doc_datas) > 3 else ''
        document_details_5 = doc_datas[4][1] if len(doc_datas) > 4 else ''
        document_details_6 = doc_datas[5][1] if len(doc_datas) > 5 else ''

        # user_short_name =
        context = {
            # 'add_agr_start_date': add_agr_start_date,
            # 'add_agreement_date': add_agreement_date,
            'agreement_date': agreement_date,
            'agreement_end_date': agreement_end_date,
            'agreement_number': agreement_number,
            'agreement_start_date': agreement_start_date,
            'applicant': applicant,
            'applicant_fact_flat': applicant_fact_flat,
            'applicant_fact_house': applicant_fact_house,
            'applicant_fact_house_building': applicant_fact_house_building,
            'applicant_fact_street': applicant_fact_street,
            'applicant_fact_town': applicant_fact_town,
            'applicant_fact_town_district': applicant_fact_town_district,
            'applicant_registration_country': applicant_registration_country,
            'applicant_registration_district': applicant_registration_district,
            'applicant_registration_flat': applicant_registration_flat,
            'applicant_registration_house': applicant_registration_house,
            'applicant_registration_house_building': applicant_registration_house_building,
            'applicant_registration_index': applicant_registration_index,
            'applicant_registration_region': applicant_registration_region,
            'applicant_registration_street': applicant_registration_street,
            'applicant_registration_town': applicant_registration_town,
            'applicant_registration_town_district': applicant_registration_town_district,
            'birth_certificate_issued_by': birth_certificate_issued_by,
            'birth_certificate_issued_date': birth_certificate_issued_date,
            'birth_certificate_number': birth_certificate_number,
            'birth_certificate_record_number': birth_certificate_record_number,
            'birth_certificate_series': birth_certificate_series,
            'child_birth_date': child_birth_date,
            'child_fact_flat': child_fact_flat,
            'child_fact_full_address': child_fact_full_address,
            'child_fact_house': child_fact_house,
            'child_fact_house_building': child_fact_house_building,
            'child_fact_street': child_fact_street,
            'child_fact_town': child_fact_town,
            'child_fact_town_district': child_fact_town_district,
            'child_first_name': child_first_name,
            'child_full_name': child_full_name,
            'child_full_name_accusative': child_full_name_accusative,
            'child_full_name_genitive': child_full_name_genitive,
            'child_gender': child_gender,
            'child_last_name': child_last_name,
            'child_patronymic': child_patronymic,
            'child_place_of_birth': child_place_of_birth,
            'child_reg_full_address': child_reg_full_address,
            'child_registration_country': child_registration_country,
            'child_registration_district': child_registration_district,
            'child_registration_flat': child_registration_flat,
            'child_registration_house': child_registration_house,
            'child_registration_house_building': child_registration_house_building,
            'child_registration_index': child_registration_index,
            'child_registration_region': child_registration_region,
            'child_registration_street': child_registration_street,
            'child_registration_town': child_registration_town,
            'child_registration_town_district': child_registration_town_district,
            'child_type': child_type,
            'compensation_size': compensation_size,
            'current_year': current_year,
            'director_full_name_dative': director_full_name_dative,
            'director_full_name_genitive': director_full_name_genitive,
            'director_short_name': director_short_name,
            'document_1': document_1,
            'document_2': document_2,
            'document_3': document_3,
            'document_4': document_4,
            'document_5': document_5,
            'document_6': document_6,
            'document_details_1': document_details_1,
            'document_details_2': document_details_2,
            'document_details_3': document_details_3,
            'document_details_4': document_details_4,
            'document_details_5': document_details_5,
            'document_details_6': document_details_6,
            'ending_acting': ending_acting,
            'ending_female': ending_female,
            'ending_naming': ending_naming,
            'ending_naming_child': ending_naming_child,
            'ending_resident': ending_resident,
            'father': father,
            'focus_name': focus_name,
            'inn_number': inn_number,
            'kpp_number': kpp_number,
            'license_date': license_date,
            'license_number': license_number,
            'mode_name': mode_name,
            'mother': mother,
            'ogrn_number': ogrn_number,
            'okogu_number': okogu_number,
            'okpo_number': okpo_number,
            'order_date': order_date,
            'order_date_compensation': order_date_compensation,
            'order_name': order_name,
            'order_number': order_number,
            'order_number_compensation': order_number_compensation,
            'organization_full_name': organization_full_name,
            'organization_full_name_genitive': organization_full_name_genitive,
            'organization_full_reg_address': organization_full_reg_address,
            'organization_phone': organization_phone,
            'organization_short_name': organization_short_name,
            'parent_citizenship': parent_citizenship,
            'parent_email': parent_email,
            'parent_first_name': parent_first_name,
            'parent_full_name': parent_full_name,
            'parent_full_name_genitive': parent_full_name_genitive,
            'parent_last_name': parent_last_name,
            'parent_patronymic': parent_patronymic,
            'parent_reg_full_address': parent_reg_full_address,
            'parent_short_name': parent_short_name,
            'parental_fee_rate': parental_fee_rate,
            'parental_fee_rate_in_words': parental_fee_rate_in_words,
            'passport_date_of_issue': passport_date_of_issue,
            'passport_issued_by': passport_issued_by,
            'passport_number': passport_number,
            'passport_series': passport_series,
            'phone_number': phone_number,
            'position_name': position_name,
            'position_name_capital': position_name_capital,
            'position_name_dative': position_name_dative,
            'position_name_genitive': position_name_genitive,
            'program_name': program_name,
            'reg_date': reg_date,
            'reg_number': reg_number,
            'region_name': region_name,
            'region_name_genitive': region_name_genitive,
            'start_date': start_date,
            'svo_parent_birth_date': svo_parent_birth_date,
            'svo_parent_full_name': svo_parent_full_name,
            'svo_parent_passport_data': svo_parent_passport_data,
            'svo_parent_snils': svo_parent_snils,
            'svo_parent_status': svo_parent_status,
            'team_name': team_name,
            'user_short_name': user_short_name,
            'validity_name': validity_name,
            'year_compensation': year_compensation,
        }

        current_dir = os.path.dirname(__file__)
        for action, values in result.items():
            if values[0] == 1:
                template_path = os.path.join(current_dir, values[2])
                output_path = os.path.join(current_dir,
                                           f'../../output_docx/{child_last_name}_{child_first_name}_{agreement_number}'
                                           f'_{values[3]}.docx')
                doc_application = DocxTemplate(template_path)
                doc_application.render(context)
                doc_application.save(output_path)

                print(f"Выполняется {action}")
                if values[1] == 1:
                    os.startfile(output_path)
                    print(f"Открывается для просмотра {values[2]}")

        # current_dir = os.path.dirname(__file__)
        # template_path = os.path.join(current_dir, '../templates/template_application.docx')
        # output_path = os.path.join(current_dir,
        #                            f'../output_docx/Заявление_прием_№_{reg_number}_{child_full_name}.docx')
        # doc_application = DocxTemplate(template_path)
        # doc_application.render(context)
        # doc_application.save(output_path)
