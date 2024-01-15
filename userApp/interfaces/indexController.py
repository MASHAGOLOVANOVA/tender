from flask import render_template, request, redirect, jsonify
from userApp import *
from userApp.database import *
from userApp.interfaces.db_set import *
from userApp.pdfexport.pdfimport import doc
from userApp.pdfexport.data import import_dictionary
import os.path


@userApp.route('/', methods=['GET', 'POST'])
def index():
    # set_db()
    # doc_set()
    # add_ware()
    return render_template('sign_in.html', false=False)


@userApp.route('/customer/<int:id>', methods=['GET', 'POST'])
def customer(id):
    if request.method == 'POST':
        # s = Sender(role=role)
        #
        # m = Message(
        #     chat_id=chat_id,
        #     date=date_value,
        #     sender_id=sender_id,
        #     status=status_value,
        #     type_id=type_id,
        #     content=content_value
        # )
        pass
    stat = StatusDocument.query.get(doc.status_id)
    fields = Field.query.filter_by(document_id=id).all()
    fields = Field.query.order_by(Field.id)
    fields=fields[1:]
    common=fields[:8]
    customer=fields[8:22]
    c_common=customer[:5]
    c_bank=customer[5:12]
    c_contact=customer[12:]
    supplier=fields[22:33]
    s_common=supplier[:5]
    s_bank=supplier[5:9]
    s_contact=supplier[9:]
    ware = Ware.query.filter_by(document_id=id).all()

    colors = []
    colors.append('black')
    for f in fields:
        chat = Chat.query.filter_by(field_id=f.id).first()
        messages = Message.query.filter_by(chat_id=chat.id, type_id=2).all()
        flag = True
        for message in messages:
            if message.status!=True:
                flag=False
                break
        if flag:
            colors.append('#262626')
        else:
            colors.append('firebrick')



    return render_template('customer.html', doc=doc, status=stat.type,
                           common=common,
                           c_common=c_common, c_bank=c_bank, c_contact=c_contact,
                           s_common=s_common, s_bank=s_bank, s_contact=s_contact, ware=ware, colors=colors)


@userApp.route('/download', methods=['GET','POST'])
def download():
    dictionary = {
    '{numberOfContract}': import_dictionary['{numberOfContract}'],
    '{subjectOfContract}': import_dictionary['{subjectOfContract}'],
    '{placeOfConclusion}' : Field.query.get(4).value,
    '{seller}' : Field.query.get(23).value,
    '{buyer}' : Field.query.get(9).value,
    '{basisOfConclusion}' : Field.query.get(1).value,
    '{IKZ}': import_dictionary['{IKZ}'],
    '{sourceOfFinancing}' : Field.query.get(6).value,
    '{sum}' : Field.query.get(7).value,
    '{prepayment}' : Field.query.get(8).value,
    '{date}' : Field.query.get(2).value,
    '{adress}' : Field.query.get(4).value,
    '{sellerAdress}' : Field.query.get(25).value,
    '{sellerINN}' : Field.query.get(26).value,
    '{sellerKPP}' : Field.query.get(27).value,
    '{sellerRschet}' : Field.query.get(30).value,
    '{sellerBankName}' : Field.query.get(28).value,
    '{sellerKschet}' : Field.query.get(31).value,
    '{sellerBIK}' : Field.query.get(29).value,
    '{sellerPhone}' : Field.query.get(32).value,
    '{sellerEmail}' : Field.query.get(33).value,
    '{buyerAdress}' : Field.query.get(11).value,
    '{buyerPhone}' : Field.query.get(21).value,
    '{buyerRschet}' : Field.query.get(20).value,
    '{buyerBankName}' : Field.query.get(18).value,
    '{buyerBIK}' : Field.query.get(19).value,
    '{buyerINN}' : Field.query.get(12).value,
    '{buyerKPP}' : Field.query.get(13).value,
    '{OGRN}' : Field.query.get(14).value,
    '{OKPO}' : Field.query.get(15).value,
    '{OKTMO}' : Field.query.get(16).value,
    '{OKATO}' : Field.query.get(17).value,
    '{buyerEmail}' : Field.query.get(22).value,
    '{sellerSignatory}' : Field.query.get(24).value,
    '{wareName}': import_dictionary['{wareName}'],
    '{units}': import_dictionary['{units}'],
    '{quantity}' : import_dictionary['{quantity}'],
    '{buyerSignatory}' : Field.query.get(10).value}

    print(dictionary)


    docPath=os.path.join('C:\\Users\\masha\\Downloads\\MOReestrr-master\\MOReestrr-master\\tender\\userApp\\pdfexport\\template.docx')
    doc(dictionary, docPath)
    return 'zalooopa'


@userApp.route('/send/<int:id>', methods=['GET','POST'])
def sendMessage(id):
    dict = request.json
    sender_id = dict['sender_id']
    text = dict['value']
    type = dict['type']
    status = dict['status']
    sms = Message(chat_id=int(id),
                  date=datetime.now(),
                  sender_id=int(sender_id),
                  status=status,
                  type_id=type,
                  content=text,
                  )
    db.session.add(sms)
    db.session.commit()
    return dict


@userApp.route('/messages/<int:id>', methods=['GET','POST'])
def messages(id):
    messages = Message.query.filter_by(chat_id=id).all()
    l=list()
    for msg in messages:
        l.append(msg.serialize())
    return jsonify(l)


@userApp.route('/update/mes/<int:id>', methods=['GET','POST'])
def update_mes(id):
    message = Message.query.get(id)
    message.status = request.json.get('status')
    db.session.commit()
    if message.status:
        c=Chat.query.get(message.chat_id)
        f=Field.query.get(c.field_id+1)
        f.value = request.json.get('value')
        db.session.commit()
        return jsonify(f'{f.id}')





@userApp.route('/supplier/<int:id>', methods=['GET', 'POST'])
def supplier(id):
    doc = Document.query.get(id)
    stat = StatusDocument.query.get(doc.status_id)
    fields = Field.query.filter_by(document_id=id).order_by(Field.id).all()
    fields = fields[1:]
    common = fields[:8]
    customer = fields[8:22]
    c_common = customer[:5]
    c_bank = customer[5:12]
    c_contact = customer[12:]
    supplier = fields[22:33]
    s_common = supplier[:5]
    s_bank = supplier[5:9]
    s_contact = supplier[9:]
    ware = Ware.query.filter_by(document_id=id).all()

    return render_template('supplier.html', doc=doc, status=stat.type,
                           common=common,
                           c_common=c_common, c_bank=c_bank, c_contact=c_contact,
                           s_common=s_common, s_bank=s_bank, s_contact=s_contact, ware=ware)


@userApp.route('/add_mo', methods=['GET', 'POST'])
def mo():
    regions = Region.query.all()  # Загрузка
    if request.method=='POST':
        try:
            name = request.form['legal_name']
            short_name = request.form['short_name']
            legal_adress = request.form['legal_adress']
            clinic_region = request.form['region']
            is_private = get_private(request.form['private'])
            specialization = request.form['spec']
            leader = request.form['leader']
            phone_numbers = request.form['phone']
            mail = request.form['mail']
            nets = request.form['nets']
            inn = request.form['inn']
            partner = False
            if request.form.get('partner') == 'on':
                partner = True
            mo = Clinic(name=name, short_name=short_name, clinic_legal_address=legal_adress, clinic_region=clinic_region,
                        is_private=is_private, specialization=specialization, leader=leader, phone_numbers=phone_numbers,
                        mail=mail, nets=nets, inn=inn, partner=partner)
            db.session.add(mo)
            db.session.commit()
            return redirect('/')
        except:
            return 'Something went wrong'
    return render_template('add_mo.html', regions=regions)


@userApp.route('/mo/<int:id>/edit', methods=['GET', 'POST'])
def edit_mo(id):
    mo = Clinic.query.get(id)
    if request.method == 'POST':
        try:
            mo.name = request.form['legal_name']
            mo.short_name = request.form['short_name']
            mo.clinic_legal_adress = request.form['legal_adress']
            mo.clinic_region = request.form['region']
            mo.is_private = get_private(request.form['private'])
            mo.specialization = request.form['spec']
            mo.leader =request.form['leader']
            mo.phone_numbers = request.form['phone']
            mo.mail = request.form['mail']
            mo.nets = request.form['nets']
            mo.inn = request.form['inn']
            if request.form.get('partner') == 'on':
                mo.partner = True
            else:
                mo.partner = False
            db.session.commit()
            return redirect('/')
        except:
            return 'Something went wrong with db'
    regions = Region.query.all()
    return render_template('update_mo.html', mo=mo, regions=regions)


@userApp.route('/dm/<int:id>/del')
def del_dm(id):
    try:
        db.session.delete(DecisionMaker.query.get(id))
        db.session.commit()
        return 'nice'
    except:
        return 'Something went wrong'


@userApp.route('/mo/<int:id>/del')
def del_mo(id):
    try:
        db.session.delete(Clinic.query.get(id))
        db.session.commit()
        return 'nice'
    except:
        return 'Something went wrong'

