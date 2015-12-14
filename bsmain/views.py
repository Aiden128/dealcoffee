# -*-coding:utf-8 -*-
# coding=UTF-8

# Create your views here.
# bsmain/views.py


import firebase
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import mail
import orm
from bsmain.forms import MbeanForm, OrderForm, UserCreateForm
from bsmain.models import Mbean


# User Implement
def user(request):
    mbeans = orm.get_bean_from_user(request.user)
    orders = orm.get_order_from_user(request.user)

    return render_to_response('users/manual.html',
                              RequestContext(request, locals()))


def home(request):
    return render_to_response('index.html',
                              RequestContext(request, locals()))


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            u = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreateForm()

    return render_to_response('registration/register.html',
                              RequestContext(request, locals()))


@login_required
def show_detailbean(request, id):
    # get mbean info
    mbean = orm.get_mbean_from_id(id)

    # get mbean limit
    total = orm.get_mbean_order_limit(id)

    # get mbean limit
    customer = orm.get_ordercounts_from_mbean(id)

    orders = orm.get_order_from_mbean(id)

    # f = OrderForm()
    # if request.POST:
    #
    #     f = OrderForm(request.POST)
    #     if f.is_valid():
    #         o_b_set = f.cleaned_data['o_b_set']
    #
    #         if customer + o_b_set > total:
    #             order_error = "＊超過可訂購數量"
    #             return render(request, "suborder.html", RequestContext(request, locals()))
    #         else:
    #             o_b_remark = f.cleaned_data['o_b_remark']
    #             o_p_phone = f.cleaned_data['o_p_phone']
    #             o_p_address = f.cleaned_data['o_p_address']
    #             o_m_b = mbean
    #             o_p_name = request.user
    #
    #             orm.save_order(o_m_b=o_m_b,
    #                            o_b_set=o_b_set,
    #                            o_b_remark=o_b_remark,
    #                            o_p_name=o_p_name,
    #                            o_p_phone=o_p_phone,
    #                            o_p_address=o_p_address)
    #
    #             # get mbean limit
    #             customer = orm.get_order_from_mbean(id)
    #
    #     else:
    #         f = OrderForm()

    return render_to_response('users/beandetail.html', RequestContext(request, locals()))


# Bean Implement
@login_required
def save_mbean(request):
    if request.POST:

        f = MbeanForm(request.POST)
        if f.is_valid():
            m_b_name = f.cleaned_data['m_b_name']
            m_b_unitprice = f.cleaned_data['m_b_unitprice']
            m_b_weight = f.cleaned_data['m_b_weight']
            m_b_minimum = f.cleaned_data['m_b_minimum']
            m_b_e_date = f.cleaned_data['m_b_e_date']
            m_b_d_date = f.cleaned_data['m_b_d_date']
            m_b_remark = f.cleaned_data['m_b_remark']
            m_p_user = request.user
            m_p_phone = f.cleaned_data['m_p_phone']

            id = orm.save_mbean(
                m_b_name=m_b_name,
                m_b_unitprice=m_b_unitprice,
                m_b_weight=m_b_weight,
                m_b_minimum=m_b_minimum,
                m_b_e_date=m_b_e_date,
                m_b_d_date=m_b_d_date,
                m_p_phone=m_p_phone,
                m_b_remark=m_b_remark,
                m_p_user=m_p_user)

            send_mail(mail.mbean_mail_title(m_b_name), mail.mbean_mail_content(request.user.username, m_b_name, id), '',
                      [request.user.email], html_message=mail.mbean_mail_content(request.user.username, m_b_name, id))
            return HttpResponseRedirect('/')

    else:
        f = MbeanForm()

    return render_to_response('order.html', RequestContext(request, locals()))


def get_bean_list(request):
    mbeans = orm.get_mbean_list()
    return render_to_response('index.html',
                              RequestContext(request, locals()))


@login_required
def delete_mbean(request, id):
    orm.delete_mbean(id, request.user)
    return HttpResponseRedirect('/user/')


def get_bean_from_user(user):
    mbeans = Mbean.objects.filter(m_p_user=user)
    return mbeans


def search(request):
    mbeans = None
    if 'q' in request.GET:
        q = request.GET['q']
        mbeans = orm.get_mbean_from_search(q)
    else:
        mbeans = orm.get_mbean_list()
    # return render(request,

    return render_to_response('index.html', locals())


# Order Implement
def save_order(request, id):
    # get mbean info
    mbean = orm.get_mbean_from_id(id)

    # get mbean limit
    total = orm.get_mbean_order_limit(id)

    # get mbean limit
    customer = orm.get_ordercounts_from_mbean(id)

    f = OrderForm()
    if request.POST:

        f = OrderForm(request.POST)
        if f.is_valid():
            o_b_set = f.cleaned_data['o_b_set']

            if customer + o_b_set > total:
                order_error = "＊超過可訂購數量"
                return render(request, "suborder.html", RequestContext(request, locals()))
            else:
                o_b_remark = f.cleaned_data['o_b_remark']
                o_p_phone = f.cleaned_data['o_p_phone']
                o_p_address = f.cleaned_data['o_p_address']
                o_m_b = mbean
                o_p_name = request.user

                orm.save_order(o_m_b=o_m_b,
                               o_b_set=o_b_set,
                               o_b_remark=o_b_remark,
                               o_p_name=o_p_name,
                               o_p_phone=o_p_phone,
                               o_p_address=o_p_address)

                # get mbean limit
                customer = orm.get_ordercounts_from_mbean(id)
                f = OrderForm()

        else:
            f = OrderForm()

    return render_to_response('suborder.html', RequestContext(request, locals()))


def delete_order(request, id):
    orm.delete_order(id, request.user)
    return HttpResponseRedirect('/user/')


def test(request):
    messages.error(request, "Error")
    return render_to_response('test.html', RequestContext(request, locals()))


def testFirebase(request):
    firebaseApp = firebase.FirebaseApplication('https://dealcoffee.firebaseio.com', None)
    result = firebaseApp.get('/test', None)
    print result
    return render_to_response('test.html', RequestContext(request, locals()))
