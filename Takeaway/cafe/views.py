from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            date__year=today.year, date__month=today.month, date__day=today.day)

        # loop through the orders and add the price value, check if order is not taken
        untaken_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_taken:
                untaken_orders.append(order)

        # pass total number of orders and total revenue into template
        context = {
            'orders': untaken_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'cafe/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {'order': order}

        return render(request, 'cafe/order-details.html', context)


    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_taken = True
        order.is_paid = True
        order.save()
        context ={
            'order' : order
        }

        return render(request, 'cafe/order-details.html', context)

    

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
        
    