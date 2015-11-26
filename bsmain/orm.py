__author__ = 'klein'

from bsmain.models import Mbean, Orders
import math

# Mbean operation
def get_mbean_list():
    return get_available_mbean().order_by('-m_b_c_date')


def get_available_mbean():
    return Mbean.objects.filter(m_b_deleted=False)


def get_mbean_from_search(q):
    return get_available_mbean().filter(m_b_name__contains=q)


def get_mbean_from_id(id):
    return get_available_mbean().get(id=id)


def get_mbean_order_limit(id):
    mbean = get_available_mbean().get(id=id)
    weight = mbean.m_b_weight
    minimum = mbean.m_b_minimum
    total = math.floor(weight / minimum)
    return total


def save_mbean(m_b_name,
               m_b_unitprice,
               m_b_weight,
               m_b_minimum,
               m_b_e_date,
               m_b_d_date,
               m_p_phone,
               m_b_remark,
               m_p_user):
    m = Mbean.objects.create(
        m_b_name=m_b_name,
        m_b_unitprice=m_b_unitprice,
        m_b_weight=m_b_weight,
        m_b_minimum=m_b_minimum,
        m_b_e_date=m_b_e_date,
        m_b_d_date=m_b_d_date,
        m_p_phone=m_p_phone,
        m_b_remark=m_b_remark,
        m_p_user=m_p_user)

    return m.pk

def get_bean_from_user(user):
    mbeans = get_available_mbean().filter(m_p_user=user)
    return mbeans


def delete_mbean(id, user):
    mbean = get_available_mbean().get(id=id)

    if mbean.m_p_user.id == user.id:
        orders = Orders.objects.filter(o_m_b=id)
        for i in orders:
            i.o_b_deleted = True
            i.save()

        mbean.m_b_deleted = True
        mbean.save()


# Orders operation

def save_order(o_m_b,
               o_b_set,
               o_b_remark,
               o_p_name,
               o_p_phone,
               o_p_address):
    m = Orders.objects.create(
        o_m_b=o_m_b,
        o_b_set=o_b_set,
        o_b_remark=o_b_remark,
        o_p_name=o_p_name,
        o_p_phone=o_p_phone,
        o_p_address=o_p_address)

    return m.pk


def get_order_from_user(user):
    orders = get_undeleted_order().filter(o_p_name_id=user)
    # .distinct('o_m_b_id')
    return orders

def get_order_from_mbean(mbean_id):
    return get_undeleted_order().filter(o_m_b=mbean_id)


def get_ordercounts_from_mbean(mbean_id):
    return get_undeleted_order().filter(o_m_b=mbean_id).count()


def delete_order(id, user):
    order = Orders.objects.get(id=id)

    if order.o_p_name.id == user.id:
        order.o_b_deleted = True
        order.save()


def get_undeleted_order():
    return Orders.objects.filter(o_b_deleted=False)