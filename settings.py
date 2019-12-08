# замените user, password, ds049945.mongolab.com, example на ваши данные доступа к БД.
MONGO_URI = "mongodb://namos:namosPass@localhost:27017/namos"

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    # Описываем ресурс `/users`
    'items': {
        # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
        # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
        # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
        #'url': 'lake/<regex("[a-f]+"):name>',
        'schema': {
            'name': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 15,
                'required': True,
                # уникальное поле (индекс не создаётся, просто значение должно быть уникальным)
                'unique': True,
            },
            'active': {
                'type': 'boolean',
                'default': True
            }
        }
    }
}