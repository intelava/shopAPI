from database import *

from datetime import datetime
from enum import Enum

"""
THIS FILE IS FOR A SPECIFIC OBJECT TYPE: ORDER
"""

Base = declarative_base()

class Order(Base):#Don't forget to apply structure changes also to the to_dict() method
    __tablename__ = "Orders"

    Id = Column(Integer(),primary_key=True)
    BrandId = Column(Integer())
    Price = Column(DECIMAL())
    StoreName = Column(String())
    CustomerName = Column(String())
    CreatedOn = Column(DateTime())
    Status = Column(Integer())


    def to_dict(self):
        dict = {
            "Id": self.Id,
            "BrandId": self.BrandId,
            "Price": self.Price,
            "StoreName": self.StoreName,
            "CustomerName": self.CustomerName,
            "CreatedOn": self.CreatedOn,
            "Status": self.Status
        }
        return dict

def orderFilterCriteria(filter):#Defines conditions for filtering

    name = filter['SearchText']
    start = filter['StartDate']
    end = filter['EndDate']
    status = filter['Status']

    sta = select(Order)

    if name is not None:
        sta = sta.filter(or_(Order.CustomerName == name, Order.StoreName == name))
    if start is not None:
        sta = sta.filter(Order.CreatedOn >= start)
    if end is not None:
        sta = sta.filter(Order.CreatedOn <= end)
    if status is not None:
        sta = sta.filter(Order.Status.in_(status))

    return sta


class OrderStatuss(Enum):#For reference and update possibilities
    Created = 10,
    InProgress = 20,
    Failed = 30,
    Completed = 40,
    Canceled = 50,
    Returned = 60

orderFilter = {
        "PageSize": None,
        "PageNumber": None,
        "SearchText": None,
        "StartDate": None,
        "EndDate": None,
        "Status": None,
        "SortBy": None
    }

def sortByCriteria(list, filter):

    list = sorted(list, key=lambda k: (k[filter['SortBy']] is None, k[filter['SortBy']]), reverse=False)#Pushes none types to the end

    return list


def insertOrder(obj,session):

    if obj['BrandId'] == 0:
        return
    session.add(Order(Id=obj['Id'], BrandId=obj["BrandId"], Price=obj["Price"], StoreName=obj["StoreName"],
                      CustomerName=obj["CustomerName"],
                      CreatedOn=datetime.strptime(obj["CreatedOn"], '%d/%m/%Y %H:%M:%S'), Status=obj["Status"]))
    session.commit()
