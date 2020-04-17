from django.shortcuts import render
from rest_framework.views import APIView
from .models import AuthorizedUser,Worker,SaleLog, Resource, StoneType, DieselStock, SaleBill
from .serializers import WorkerSerializer,SaleLogSerializer, StoneTypeSerializer, DieselStockSerializer, SaleBillSerializer
from rest_framework.response import Response
from django.core.serializers import serialize
from rest_framework import status
from django.http import HttpResponse
from .serializers import ResourceSerializer
# Create your views here.
import datetime


class Login(APIView):
    def post(self, request):
        authorized_users = AuthorizedUser.objects.all()
        message = "Unauthorized"
        s = status.HTTP_200_OK
        for user in authorized_users:
            if(user.username == request.data["username"]) and (user.password==request.data["password"]):
                s = status.HTTP_200_OK
                message = "Authorized"
        return Response({message}, status=s)

class WorkerView(APIView):
    def post(self, request):
        name = request.data["name"]
        title = request.data["title"]
        date = list(map(int, request.data["date_of_joining"].split('-')))
        date_of_joining = datetime.datetime(date[0], date[1], date[2])
        mobile = request.data["mobile"]
        aadhar_number = request.data["aadhar_number"]
        salary = request.data["salary"]
        photo = request.data["photo"]
        gender = request.data["gender"]
        new_worker = Worker.objects.create(name=name, 
        title=title,  
        mobile=mobile, 
        aadhar_number=aadhar_number, 
        salary=salary, 
        photo=photo, 
        gender = gender)
        new_worker.save()
       
        return Response({"Success"}, status=status.HTTP_200_OK)
        # return Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)

        
    def get(self, request):
        workers = Worker.objects.all()
        worker_data = []
        for i in range(len(workers)):
            worker_data.append({})
            worker_data[i]["id"] = i
            worker_data[i]["name"] = workers[i].name
            worker_data[i]["gender"] = workers[i].gender
            worker_data[i]["photo"] = workers[i].photo.url
            worker_data[i]["aadhar_number"] = workers[i].aadhar_number
            worker_data[i]["date_of_joining"] = workers[i].date_of_joining
            worker_data[i]["mobile"] = workers[i].mobile
            worker_data[i]["title"] = workers[i].title
            worker_data[i]["salary"] = workers[i].salary
        return Response(worker_data, status=status.HTTP_200_OK)
    
    def delete(self, request, aadhar):
        worker = Worker.objects.filter(aadhar_number = aadhar)
        if(len(worker) == 0):
            return Response({},status=status.HTTP_400_BAD_REQUEST)
        else:
            worker.delete()
            return Response({"deleted"}, status=status.HTTP_200_OK)
    

class SalesView(APIView):
    def get(self,request):
        sales = SaleLog.objects.all()
        
        sale_data = []
        for i in range(len(sales)):
            sale_data.append({})
            sale_data[i]["id"] = i
            st = sales[i].stone_type.stone_type
            price = sales[i].stone_type.price
            sale_data[i]["stone_type"] = {}
            sale_data[i]["stone_type"]["st"] = st
            sale_data[i]["stone_type"]["price"] = price
            sale_data[i]["v_num"] = {}
            sale_data[i]["v_num"]["type"] = sales[i].v_num.resource_type
            sale_data[i]["v_num"]["date"] = sales[i].v_num.purchase_date
            sale_data[i]["v_num"]["cost"] = sales[i].v_num.purchase_cost
            sale_data[i]["v_num"]["num"] = sales[i].v_num.rto_number
            sale_data[i]["quantity"] = sales[i].quantity
            sale_data[i]["delivery_worker"] = sales[i].delivery_worker.name
            sale_data[i]["diesel_stock_name"] = sales[i].diesel_stock_name.id
            sale_data[i]["desiel_spent"] = sales[i].desiel_spent
            sale_data[i]["sale_date"] = sales[i].sale_bill.date
        return Response(sale_data, status=status.HTTP_200_OK)
    def post(self, request):
            vehicle = request.data["vehicle"]
            vehicle = Resource.objects.get(rto_number = vehicle)
            stone_type = request.data["stonetype"]
            stone_type = StoneType.objects.get(stone_type=stone_type)
            delivery_worker = request.data["delivery_worker"]
            delivery_worker = Worker.objects.get(name=delivery_worker)
            diesel_stock_name = request.data["diesel_stock_name"]
            diesel_stock_name = DieselStock.objects.get(id = diesel_stock_name)
            sale_bill = request.data["sale_bill"]
            sale_bill = SaleBill.objects.get(bill_num = sale_bill)

            new_salelog = SaleLog.objects.create(
            v_num = vehicle,
            stone_type = stone_type,
            quantity = request.data["quantity"],
            delivery_worker = delivery_worker,
            diesel_stock_name = diesel_stock_name,
            desiel_spent = request.data["desiel_spent"],
            sale_bill = sale_bill
        )
            new_salelog.save()
            
            return Response({"Success"}, status=status.HTTP_200_OK)
        


class ResourceView(APIView):
    def get(self, request):
        resources = Resource.objects.all()
        res_list = []
        for i in range(len(resources)):
            res_list.append(resources[i].rto_number)
        return Response(res_list, status=status.HTTP_200_OK)

class StoneTypeView(APIView):
    def get(self, request):
        types = StoneType.objects.all()
        response_list = []
        for i in range(len(types)):
            response_list.append(types[i].stone_type)
        return Response(response_list, status=status.HTTP_200_OK)

class DieselStockView(APIView):
    def get(self, request):
        diesel_stock_names = []
        stocks = DieselStock.objects.all()
        for i in range(len(stocks)):
            diesel_stock_names.append(stocks[i].__str__()[3:])
        return Response(diesel_stock_names, status=status.HTTP_200_OK)
        
class SaleBillView(APIView):
    def get(self, request):
        bill_list = []
        bills = SaleBill.objects.all()
        for i in range(len(bills)):
            bill_list.append(bills[i].__str__())
        return Response(bill_list, status=status.HTTP_200_OK)
