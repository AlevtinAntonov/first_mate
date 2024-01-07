import os
from datetime import timedelta, datetime
from docxtpl import DocxTemplate
from number_to_string import get_string_by_number

from app_model.db.db_connect import db
from app_view_model.functions.format_address import format_address
from app_view_model.print_forms.functions.db_queries import query_organization, query_parent, query_address, query_child
from app_view_model.print_forms.functions.print_functions import decline_organization, decline_position, \
    declension_full_name


def print_agreement(child_id, referral_id, person_id):
    with db as cur:
        row_org = cur.execute(query_organization, (referral_id,)).fetchone()
        organization_full_name = row_org[0] if row_org else ''
        license_date = row_org[23].strftime('%d.%m.%Y') if row_org else ''
        license_number = row_org[22] if row_org else ''
        position_name = row_org[11] if row_org else ''
        position_name_capital = position_name.capitalize() if position_name else ''
        position_name_genitive = decline_position(position_name, 'родительный')
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
        kpp_number = row_org[10] if row_org else ''
        director_short_name = ' '.join((row_org[20], row_org[12])) if row_org else ''

        row_parent = cur.execute(query_parent, (person_id,)).fetchone()
        parent_full_name = ' '.join((row_parent[0], row_parent[1], row_parent[2])) if row_parent else ''
        parent_full_name_genitive = declension_full_name(parent_full_name, 'родительный',
                                                         row_parent[8]) if parent_full_name else ''
        passport_series = row_parent[4] if row_parent else ''
        passport_number = row_parent[5] if row_parent else ''
        passport_date_of_issue = row_parent[7].strftime('%d.%m.%Y') if row_parent else ''
        passport_issued_by = row_parent[6] if row_parent else ''
        phone_number = row_parent[9] if row_parent else ''
        ending_female = 'а' if row_parent and row_parent[8] == 'женский' else ''

        ending_naming = 'ая' if row_parent and row_parent[8] == 'женский' else 'ый'
        parent_short_name = ' '.join((row_parent[11], row_parent[0])) if row_parent else ''

        row_parent_address_reg = cur.execute(
            query_address % ("PERSON", "PERSON.PERSON_ID", "PERSON.PERSON_ID", "ADDRESS.IS_REGISTRATION"),
            (person_id,)).fetchone()
        parent_reg_full_address = format_address(row_parent_address_reg) if row_parent_address_reg else ''

        row_child_address_reg = cur.execute(
            query_address % ("CHILD", "CHILD.PERSON_ID", "CHILD.CHILD_ID", "ADDRESS.IS_REGISTRATION"),
            (child_id,)).fetchone()
        child_reg_full_address = format_address(row_child_address_reg) if row_child_address_reg else ''

        row_child = cur.execute(query_child, (referral_id,)).fetchone()
        child_last_name = row_child[0] if row_child else ''
        child_first_name = row_child[1] if row_child else ''
        child_full_name = ' '.join((row_child[0], row_child[1], row_child[2])) if row_child else ''
        child_full_name_genitive = declension_full_name(child_full_name,
                                                        'родительный', row_child[9]) if child_full_name else ''
        child_birth_date = row_child[3].strftime('%d.%m.%Y') if row_child else ''

        focus_name = row_child[10] if row_child else ''
        agreement_number = row_child[14] if row_child else ''
        agreement_date = row_child[15].strftime('%d.%m.%Y') if row_child else ''
        ending_naming_child = 'ой' if row_child and row_child[9] == 'женский' else 'ого'
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
        agreement_end_date = calculate_end_date.replace(year=datetime.now().year + int(validity_years)).strftime('%d.%m.%Y')
        team_name = row_child[21] if row_child else ''

        context = {
            'organization_full_name': organization_full_name,
            'organization_full_name_genitive': organization_full_name_genitive,
            'organization_short_name': organization_short_name,
            'director_full_name_genitive': director_full_name_genitive,
            'license_date': license_date,
            'license_number': license_number,
            'position_name': position_name,
            'position_name_capital': position_name_capital,
            'position_name_genitive': position_name_genitive,
            'ending_acting': ending_acting,
            'organization_full_reg_address': organization_full_reg_address,
            'organization_phone': organization_phone,
            'okpo_number': okpo_number,
            'okogu_number': okogu_number,
            'ogrn_number': ogrn_number,
            'inn_number': inn_number,
            'kpp_number': kpp_number,
            'director_short_name': director_short_name,
            'parent_full_name': parent_full_name,
            'parent_full_name_genitive': parent_full_name_genitive,
            'passport_series': passport_series,
            'passport_number': passport_number,
            'passport_date_of_issue': passport_date_of_issue,
            'passport_issued_by': passport_issued_by,
            'phone_number': phone_number,
            'ending_female': ending_female,
            'ending_naming': ending_naming,
            'parent_short_name': parent_short_name,
            'parent_reg_full_address': parent_reg_full_address,
            'child_reg_full_address': child_reg_full_address,
            'child_last_name': child_last_name,
            'child_first_name': child_first_name,
            'child_full_name': child_full_name,
            'child_full_name_genitive': child_full_name_genitive,
            'child_birth_date': child_birth_date,
            'focus_name': focus_name,
            'agreement_number': agreement_number,
            'agreement_date': agreement_date,
            'ending_naming_child': ending_naming_child,
            'program_name': program_name,
            'validity_name': validity_name,
            'mode_name': mode_name,
            'agreement_start_date': agreement_start_date,
            'agreement_end_date': agreement_end_date,
            'team_name': team_name,
            'order_number': order_number,
            'order_date': order_date,
            'order_name': order_name,
            'parental_fee_rate': parental_fee_rate,
            'parental_fee_rate_in_words': parental_fee_rate_in_words,

        }

        current_dir = os.path.dirname(__file__)
        template_path = os.path.join(current_dir, '../templates/template_agreement.docx')
        output_path = os.path.join(current_dir,
                                   f'../output_docx/Договор_№_{agreement_number}_{child_full_name}.docx')

        doc_application = DocxTemplate(template_path)
        doc_application.render(context)
        doc_application.save(output_path)
