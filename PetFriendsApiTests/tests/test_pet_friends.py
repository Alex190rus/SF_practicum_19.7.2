from api import PetFriends
from settings import valid_email, valid_password, valid_name, valid_animal_type, valid_age, valid_pet_photo
from settings import new_name, new_animal_type, new_age, new_pet_photo, not_valid_emaill, not_valid_password
from settings import long_name, sumbols_type


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    if 'key' in result:
        print('Аутентификационный ключ успешно получен')
    else:
        raise Exception('Аутентификационный ключ неполучен')


def test_get_all_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(result['pets']) > 0:
        assert status == 200
        print('Количество ваших питомцев =', len(result['pets']))
    else:
        raise Exception("Питомцев не обнаружено")



def test_post_add_new_pet(name=valid_name, animal_type=valid_animal_type, age=valid_age,
                          pet_photo=valid_pet_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'name'in result
    assert 'age' in result
    assert 'animal_type' in result
    assert 'pet_photo' in result
    print(f'Создан питомец с именем {valid_name}, относится к семейству {valid_animal_type}, возраст {valid_age}'
          f'с фото')


def test_put_changing_data_pets(name=new_name, animal_type=new_animal_type, age=new_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(pet_id['pets']) > 0:
        status, result = pf.put_update_information_about_pet(auth_key, pet_id['pets'][0]['id'],
                                                 name, animal_type, age)
        assert status == 200
        assert 'name' in result
        print(f'Имя питомца {valid_name}, успешно изменено на {new_name}')
        print(f'Семейство питомца {valid_animal_type}, успешно изменено на {new_animal_type}')
        print(f'Возраст питомца изменился с {valid_age}, на {new_age}')
    else:
        raise Exception("Питомцев не обнаружено")


def test_delete_pet_from_database():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(pet_id['pets']) > 0:
        status, result = pf.delete_pet_from_database(auth_key, pet_id['pets'][0]['id'])
        assert status == 200
        print(f'Питомец {new_name}, успешно удалён.')
    else:
        raise Exception("Питомцев не обнаружено")


def test_post_add_new_pet_without_photo(name=valid_name, animal_type=valid_animal_type, age=valid_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert 'name' in result
    assert 'age' in result
    assert 'animal_type' in result
    print(f'Создан питомец с именем {valid_name}, относится к семейству {valid_animal_type}, возраст {valid_age}'
          f'без фото')


def test_post_add_photo_of_pet(pet_photo=new_pet_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(pet_id['pets']) > 0:
        status, result = pf.post_add_photo_of_pet(auth_key, pet_id['pets'][0]['id'], pet_photo)
        assert status == 200
        assert 'pet_photo' in result
        print(f'Питомцу {valid_name}, добавлено фото.')
    else:
        raise Exception("Питомцев не обнаружено")


def test_get_api_key_for_not_valid_user(email=not_valid_emaill, password=not_valid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    if 'key' in result:
        print('Аутентификационный ключ успешно получен')
    else:
        raise Exception('Аутентификационный ключ неполучен')


def test_get_all_pets_with_not_valid_key(filter=''):
    _, auth_key = pf.get_api_key(not_valid_emaill, not_valid_password)
    status, result = pf.get_list_of_pets(auth_key, 'my_pets')
    assert status != 200


def test_put_changing_data_pets_long_name(name=long_name, animal_type=new_animal_type, age=new_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(pet_id['pets']) > 0:
        status, result = pf.put_update_information_about_pet(auth_key, pet_id['pets'][0]['id'],
                                                 name, animal_type, age)
        assert status == 200
        assert 'name' in result
        print(f'Имя питомца {valid_name}, успешно изменено на {long_name}')
        print(f'Семейство питомца {valid_animal_type}, успешно изменено на {new_animal_type}')
        print(f'Возраст питомца изменился с {valid_age}, на {new_age}')
    else:
        raise Exception("Питомцев не обнаружено")


def test_put_changing_data_pets_animal_tupe_sumbols(name=long_name, animal_type=sumbols_type, age=new_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pet_id = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(pet_id['pets']) > 0:
        status, result = pf.put_update_information_about_pet(auth_key, pet_id['pets'][0]['id'],
                                                 name, animal_type, age)
        assert status == 200
        assert 'name' in result
        print(f'Имя питомца {valid_name}, успешно изменено на {long_name}')
        print(f'Семейство питомца {valid_animal_type}, успешно изменено на {sumbols_type}')
        print(f'Возраст питомца изменился с {valid_age}, на {new_age}')
    else:
        raise Exception("Питомцев не обнаружено")




