from flask import render_template, request, redirect, jsonify
from userApp import *
from userApp.database import *
from datetime import datetime

def set_db():
    s1 = Sender(role='заказчик')
    s2 = Sender(role='поставщик')
    db.session.add(s1)
    db.session.commit()
    db.session.add(s2)
    db.session.commit()

    t1 = Type(type='text')
    t2 = Type(type='file')
    t3 = Type(type='suggestion')
    db.session.add(t1)
    db.session.commit()
    db.session.add(t2)
    db.session.commit()
    db.session.add(t3)
    db.session.commit()

    sd_list = []
    sd_list.append(StatusDocument(type='Ввод сведений заказчиком'));
    sd_list.append(StatusDocument(type='Отправлен на подпись поставщику'));
    sd_list.append(StatusDocument(type='Подписано поставщиком'));
    sd_list.append(StatusDocument(type='Подписано заказчиком'));
    sd_list.append(StatusDocument(type='Направлен протокол разногласий'));
    sd_list.append(StatusDocument(type='Контракт не подписан'));
    sd_list.append(StatusDocument(type='Контракт подписан'));

    for i in range(len(sd_list)):
        db.session.add(sd_list[i])
        db.session.commit()




def doc_set():
    doc = Document(
        name='Договор № 129/23 На поставку расходного материала (Сетка-слинг)',
        status_id='1',
        restr_number='',
        zakup_number='',
    )

    db.session.add(doc)
    db.session.commit()

    c = Chat()
    db.session.add(c)
    db.session.commit()

    field_obj = Field(
        name="Основание заключения",
        value="п. 4 ч. 1 ст. 93 Закупка объемом до 600 тысяч рублей п. 5 ч. 1 ст. 93 Закупка объёмом до 600 тысяч рублей",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_obj = Field(
        name="Начало действия контракта",
        value="09.12.2023",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_obj = Field(
        name="Конец действия контракта",
        value="29.12.2023",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_obj = Field(
        name="Место заключения",
        value="Пермь, проспект Мира, 1",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_obj = Field(
        name="Идентификационный код закупки (ИКЗ)",
        value="12345678901234567890123456789012345678",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_obj = Field(
        name="Источник финансирования",
        value="Бюджетные средства",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_obj = Field(
        name="Сумма без НДС",
        value="220000",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_obj = Field(
        name="Аванс",
        value="",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_obj)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()


    field_address = Field(
        name="Заказчик",
        value="Государственное бюджетное учреждение здравоохранения Пермского края «Клиническая медико-санитарная часть №1»",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_address)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_address = Field(
        name="Подписант заказчика",
        value="Д.В. Михайленко Главный врач ГБУЗ «КМСЧ № 1»",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_address)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_address = Field(
        name="Фактический адрес",
        value="г. Москва, ул. Примерная, д. 123",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_address)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    # Пример заполнения полей для ИНН, КПП, ОГРН и фактического адреса
    field_inn = Field(
        name="ИНН",
        value="1234567890",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_inn)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_kpp = Field(
        name="КПП",
        value="123456789",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_kpp)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_ogrn = Field(
        name="ОГРН",
        value="1234567890123",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_ogrn)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_ogrn = Field(
        name="ОКПО",
        value="1234567890123",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_ogrn)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_ogrn = Field(
        name="ОКТМО",
        value="1234567890123",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_ogrn)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_ogrn = Field(
        name="ОКАТО",
        value="1234567890123",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_ogrn)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    # Пример заполнения полей для наименования банка, БИК и расчетного счета
    field_bank_name = Field(
        name="Наименование банка",
        value="Пример Банк",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_bank_name)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_bik = Field(
        name="БИК",
        value="123456789",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_bik)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_account = Field(
        name="Расчетный счет",
        value="12345678901234567890",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_account)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    # Пример заполнения полей для телефона и электронной почты
    field_phone = Field(
        name="Телефон",
        value="123-456-789",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_phone)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_email = Field(
        name="Email",
        value="example@example.com",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_email)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()


    #  for suolierrrrrrrrrrr
    field_address = Field(
        name="Поставщик",
        value="ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ КАМА-МЕДИКА",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_address)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_address = Field(
        name="Подписант поставщика",
        value="В.А. Агафонов Директор",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_address)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_address = Field(
        name="Фактический адрес",
        value="Российская Федерация, г. Пермь, ул. Монастырская, д. 12, оф. 308",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_address)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    # Пример заполнения полей для ИНН, КПП, ОГРН и фактического адреса
    field_inn = Field(
        name="ИНН",
        value="1234567890",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_inn)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_kpp = Field(
        name="КПП",
        value="123456789",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_kpp)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    # Пример заполнения полей для наименования банка, БИК и расчетного счета
    field_bank_name = Field(
        name="Наименование банка",
        value="Пример Банк",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_bank_name)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_bik = Field(
        name="БИК",
        value="123456789",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_bik)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_account = Field(
        name="Расчетный счет",
        value="12345678901234567890",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_account)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    field_account = Field(
        name="Корреспондентский счет",
        value="30101810900000000603",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_account)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()
    # Пример заполнения полей для телефона и электронной почты
    field_phone = Field(
        name="Телефон",
        value="123-456-789",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_phone)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()

    field_email = Field(
        name="Email",
        value="example@example.com",
        status_seller=False,
        status_buyer=True,
        document_id=Document.query.order_by(Document.id.desc()).first().id
    )
    db.session.add(field_email)
    db.session.commit()
    c = Chat(field_id=Field.query.order_by(Field.id.desc()).first().id)
    db.session.add(c)
    db.session.commit()



def add_ware():
    names = ['document_id', 'okpd2', 'name', 'price_nds', 'quantity', 'units', 'nds', 'sum', 'address', 'time' ]
    ware = Ware(
        document_id=Document.query.order_by(Document.id.desc()).first().id,
        okpd2="Example OKPD2",
        name="Example Name",
        price_nds="100.00",  # Пример цены с НДС
        quantity="10",  # Пример количества
        units="шт.",  # Пример единиц измерения
        nds="20%",  # Пример НДС
        sum_nds="1200.00",  # Пример суммы с НДС
        adress="г. Москва, ул. Примерная, д. 123",  # Пример адреса поставки
        time="29.12.2023",  # Пример срока поставки
    )
    db.session.add(ware)
    db.session.commit()
    for i in names:
        w_c = WareChat(ware_id=Ware.query.order_by(Ware.id.desc()).first().id, name=i)
        db.session.add(w_c)
        db.session.commit()
        c = Chat(ware_chat_id=WareChat.query.order_by(WareChat.id.desc()).first().id)
        db.session.add(c)
        db.session.commit()
