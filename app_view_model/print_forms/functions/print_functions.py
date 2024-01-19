import os

from petrovich.main import Petrovich
from petrovich.enums import Case, Gender

current_dir = './'
custom_path = os.path.join(current_dir, './db/rules.json')
petro = Petrovich(rules_path=custom_path)


def declension_full_name(full_name, genitive, male=None):
    match male:
        case 'мужской':
            gender = Gender.MALE
        case 'женский':
            gender = Gender.FEMALE
        case _:
            gender = None
    match genitive:
        case 'родительный':
            genitive = Case.GENITIVE
        case 'дательный':
            genitive = Case.DATIVE
        case 'винительный':
            genitive = Case.ACCUSATIVE
    segments = full_name.split()
    if len(segments) == 4:
        last_name, first_name, patronymic, patronymic_2 = segments
        cased_last_name = petro.lastname(last_name, genitive, gender)
        cased_first_name = petro.firstname(first_name, genitive, gender)
        cased_patronymic = petro.middlename(patronymic, genitive, gender)
        cased_patronymic_2 = petro.middlename(patronymic_2, genitive, gender)
        return ' '.join((cased_last_name, cased_first_name, cased_patronymic, cased_patronymic_2))
    elif len(segments) == 3:
        last_name, first_name, patronymic = segments
        cased_last_name = petro.lastname(last_name, genitive, gender)
        cased_first_name = petro.firstname(first_name, genitive, gender)
        cased_patronymic = petro.middlename(patronymic, genitive, gender)
        return ' '.join((cased_last_name, cased_first_name, cased_patronymic))
    elif len(segments) == 2:
        last_name, first_name = segments
        cased_last_name = petro.lastname(last_name, genitive, gender)
        cased_first_name = petro.firstname(first_name, genitive, gender)
        return ' '.join((cased_last_name, cased_first_name))
    else:
        raise ValueError


def decline_organization(original_string, genitive, keyword='учреждение'):
    parts = original_string.split(keyword)
    first_part = ' '.join((parts[0], keyword))
    words = first_part.split()

    words_list = []
    for word in words:
        if genitive == 'родительный':
            if word.endswith('ое'):
                word = word[:-2] + 'ого'
            elif word.endswith('ие'):
                word = word[:-2] + 'ия'
        elif genitive == 'дательный':
            if word.endswith('ое'):
                word = word[:-2] + 'ому'
            elif word.endswith('ие'):
                word = word[:-2] + 'ию'

        words_list.append(word)
        parts[0] = ' '.join(words_list)
    return ''.join((parts[0], parts[1]))


def decline_region(region, case):
    if case == 'родительный':
        if region.endswith('ий'):
            region = region[:-2] + 'ого'
        elif region.endswith('ый'):
            region = region[:-2] + 'ого'
    elif case == 'дательный':
        if region.endswith('ий'):
            region = region[:-2] + 'ому'
        elif region.endswith('ый'):
            region = region[:-2] + 'ому'
    return region


def decline_position(position, case):
    decline_dict = {
        'заведующий': {
            'родительный': 'заведующего',
            'дательный': 'заведующему',
            'винительный': 'заведующего'
        },
        'директор': {
            'родительный': 'директора',
            'дательный': 'директору',
            'винительный': 'директора'
        }
    }

    if position.lower() in decline_dict:
        if case in decline_dict[position]:
            return decline_dict[position][case]
        else:
            return "Данный падеж не поддерживается"
    else:
        return "Данная должность не поддерживается"


if __name__ == '__main__':
    pass
