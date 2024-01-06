import os
from docxtpl import DocxTemplate

from app_model.db.db_connect import db
from app_view_model.functions.format_address import format_address
from app_view_model.print_forms.functions.db_queries import query_child, query_organization, query_address, query_parent
from app_view_model.print_forms.functions.print_functions import declension_full_name, decline_organization


def print_application(child_id, referral_id, person_id):
    with db as cur:
        row_child = cur.execute(query_child, (referral_id,)).fetchone()
        child_full_name = ' '.join((row_child[0], row_child[1], row_child[2])) if row_child else ''
        child_full_name_accusative = declension_full_name(child_full_name,
                                                          'винительный', row_child[9]) if child_full_name else ''
        child_full_name_genitive = declension_full_name(child_full_name,
                                                        'родительный', row_child[9]) if child_full_name else ''
        child_birth_date = row_child[3].strftime('%d.%m.%Y')
        birth_certificate_series = row_child[4] or ''
        birth_certificate_number = row_child[5] or ''
        birth_certificate_issued_by = row_child[6] or ''
        birth_certificate_issued_date = row_child[7].strftime('%d.%m.%Y')
        child_place_of_birth = row_child[8] or ''
        focus_name = row_child[10]
        reg_number = row_child[11]
        reg_date = row_child[12].strftime('%d.%m.%Y')
        start_date = row_child[13].strftime('%d.%m.%Y')
        child_type = 'сына' if row_child[9] == 'мужской' else 'дочь'

        row_org = cur.execute(query_organization, (referral_id,)).fetchone()
        organization_full_name = row_org[0] if row_org else ''
        organization_full_name_genitive = decline_organization(organization_full_name,
                                                               'родительный') if organization_full_name else ''
        organization_short_name = row_org[1] if row_org else ''
        director_full_name = ' '.join((row_org[12], row_org[13], row_org[14])) if row_org else ''
        director_full_name_dative = declension_full_name(director_full_name, 'дательный',
                                                         row_org[21]) if director_full_name else ''

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

        row_child_address_reg = cur.execute(
            query_address % ("CHILD", "CHILD.PERSON_ID", "CHILD.CHILD_ID", "ADDRESS.IS_REGISTRATION"),
            (child_id,)).fetchone()
        child_reg_full_address = format_address(row_child_address_reg) if row_child_address_reg else ''
        row_child_address_fact = cur.execute(
            query_address % ("CHILD", "CHILD.PERSON_ID", "CHILD.CHILD_ID", "ADDRESS.IS_FACT"),
            (child_id,)).fetchone()
        child_fact_full_address = format_address(
            row_child_address_fact) if row_child_address_fact else child_reg_full_address

        row_parent_address_reg = cur.execute(
            query_address % ("PERSON", "PERSON.PERSON_ID", "PERSON.PERSON_ID", "ADDRESS.IS_REGISTRATION"),
            (person_id,)).fetchone()
        address_reg_full = format_address(row_parent_address_reg) if row_parent_address_reg else ''

        context = {
            'child_full_name_accusative': child_full_name_accusative,
            'child_full_name_genitive': child_full_name_genitive,
            'child_birth_date': child_birth_date,
            'birth_certificate_series': birth_certificate_series,
            'birth_certificate_number': birth_certificate_number,
            'birth_certificate_issued_by': birth_certificate_issued_by,
            'birth_certificate_issued_date': birth_certificate_issued_date,
            'child_place_of_birth': child_place_of_birth,
            'focus_name': focus_name,
            'reg_number': reg_number,
            'reg_date': reg_date,
            'start_date': start_date,
            'child_type': child_type,
            'organization_full_name': organization_full_name,
            'organization_full_name_genitive': organization_full_name_genitive,
            'organization_short_name': organization_short_name,
            'director_full_name_dative': director_full_name_dative,
            'child_reg_full_address': child_reg_full_address,
            'child_fact_full_address': child_fact_full_address,
            'address_reg_full': address_reg_full,
            'parent_full_name_genitive': parent_full_name_genitive,
            'passport_series': passport_series,
            'passport_number': passport_number,
            'passport_date_of_issue': passport_date_of_issue,
            'passport_issued_by': passport_issued_by,
            'phone_number': phone_number,
            'ending_female': ending_female,
        }

        current_dir = os.path.dirname(__file__)
        template_path = os.path.join(current_dir, '../templates/template_application.docx')
        output_path = os.path.join(current_dir,
                                   f'../output_docx/Заявление_прием_№_{reg_number}_{row_child[0]}_{row_child[1]}.docx')

        doc_application = DocxTemplate(template_path)
        doc_application.render(context)
        doc_application.save(output_path)


if __name__ == '__main__':
    pass
