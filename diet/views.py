# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import AddUser,Diet,BodyMassIndex,Calories
from django.http import HttpResponse
from django.conf import settings
from .forms import Login,Signup,bmi
import random
# Create your views here.

def index(request):
    return render(request,"index.html")

def base(request):
    if request.session.get('email'):
        data="Already logged in ..."
        return render(request,"logout.html")
    else:
        form=Login()
        form=Signup()
        return render(request,"base.html")
   

def login1(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            #print(form)
            email = form.cleaned_data['Email']
            try:
                u = AddUser.objects.get(Email=email)
            except AddUser.DoesNotExist as e:
                    error="no such user ... signup to login"
                    form=Signup()
                    return render(request,"base.html")
            else:
                password = form.cleaned_data['Password']
                p=u.Password
                if password == p:
                    request.session['email'] = email
                    request.session['password'] = p
                    return render(request,"logout.html")
                    #return HttpResponse("<h1 style='color:red'>Welcome user {} with password {}".format(email,password))
                else:
                    error="Password does not match"
                    form=Login()
                    return render(request,"index.html",{'error':error})
        else:
            error = "Form is not valid...Try again"
            return render(request,"base.html",{'error':error})
    else:
        error = "Incorrect method used"
        return render(request,"base.html",{'error':error})

class Signedup(View):
    def get(self,request):
        form = Signup()
        error = "Your method is incorrect..."
        return render(request,"index.html",{'error':error})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data['Email']
            try:
                AddUser.objects.get(Email=email)
            except AddUser.DoesNotExist as e:
                pass1 = form.cleaned_data['Password']
                pass2 = form.cleaned_data['Confirmpassword']
                if pass1 == pass2:
                    dict = {
                     'Name':form.cleaned_data['Name'],
                     'Username' : form.cleaned_data['Username'],
                     'Email' : form.cleaned_data['Email'],
                     'Password' : form.cleaned_data['Password'],
                      # 'Profile' : form.cleaned_data['Profile'],
                        }
                    new_user = AddUser.objects.create(**dict)
                    new_user.save()
                    return render(request,"logout.html")
            else:
                error = "Password does not match...Try again"
                form = Signup()
                return render(request,"base.html",{'error':error})
        else:
            error = "Your form is invalid...try again"
            form = Signup()
            return render(request,"base.html",{'error':error})

def logout(request):
    del request.session['email']
    del request.session['password']
    return render(request,"index.html")

def bmi(request):
    if request.method=="POST":
        height=request.POST['height']
        height=float(height)
        weight=request.POST['weight']
        weight=int(weight)
        pip=pow(height,height)
        BMI = weight / pip
        inss=BodyMassIndex(BMI=BMI)
        inss.save()
        if BMI <= 18.5:
            return render(request, 'bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And  You are Under weight'})
        elif 18.5 < BMI <= 25 :
            return render(request, 'bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And You are Normal Weight'})
        elif 25 < BMI <= 29.9 :
            return render(request, 'bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And  You are Over Weight'})
        else : BMI >=30 
        return render(request, 'bmi.html', {'xyz':'Your BMI is', 'bmi':f'{BMI:.4}', 'abc':'And You are Obese Weight'})
        return render(request, 'bmi.html', {'bmi':BMI})
        

        
    else:
        return render(request, 'bmi.html')

def calorie(request):
    if request.method == "POST":
        age=request.POST["age"]
        activity = request.POST["activity"]
        
        #print(get_type("activity"))
        weight = request.POST['weight']
        gender=request.POST['gender']
        height=request.POST['height']
        weight = int(weight)
        if gender == "Male":
           abc = (10 *int( weight)) + (6 * int(height)) -(5 * int(age)) - int(161)
        else:
           abc = (10 * int(weight)) + (6 * int(height)) -(5 * int(age)) + int(5)
        if activity == "Senedarty":
            defg = abc * 1.2
        elif activity == "Lightly Active":
            defg = abc * 1.375
        elif activity == "Moderately Active":
            defg = abc * 1.55
        else:
            defg = abc * 1.9
        inx = Calories(defg=defg)
        inx.save()
        return render(request, 'bmr.html', {'xyz':'Your Daily Required Calories Is = ','calories':round(defg)})
        '''return render(request, 'bmr.html', {'xyz':'Your Daily Required Calories Is = ', 'calories':f'{defg:.2}')'''
    return render(request, 'bmr.html')


def diet(request):
    if request.method == "POST":
        users= request.user.username
        age = request.POST["age"]
        height = request.POST["height"]
        gender= request.POST["gender"]
        activity= request.POST["activity"]

        weight = request.POST ["weight"]
        ins = Diet(users=users,age=age,height=height,gender=gender,activity=activity,weight=weight)
        ins.save()
        weight = int(weight)
        if gender == "Male":
           abc = (10 *int( weight)) + (6 * int(height)) -(5 * int(age)) - int(161)
        else:
           abc = (10 * int(weight)) + (6 * int(height)) -(5 * int(age)) + int(5)
        if activity == "Senedarty":
            defg = abc * 1.2
        elif activity == "Lightly Active":
            defg = abc * 1.375
        elif activity == "Moderately Active":
            defg = abc * 1.55
        else:
            defg = abc * 1.9
        

        
        import pandas as pd
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.model_selection import train_test_split
        #from sklearn.preprocessing import OneHotEncoder
        from sklearn.preprocessing import LabelEncoder
        from sklearn import metrics

        #from numpy import argmax
        import numpy as np
        #import sklearn.cross_validation as cross_validation
        print('k')
        diet_file_path = 'C:/Users/pallavi-pc/Desktop/AIproject/static/train1.csv'
        
        diet_data = pd.read_csv(diet_file_path) 
        #print(diet_data)
        y=diet_data.iloc[:,12]
        #print(y)
        x = diet_data.iloc[:,[-8,-9,-10,-2]]
        #print(x)
        #x=diet_data.iloc[:,[3,4,5,11]]
        print(type(diet_data))
        print(type(x))
        print(type(y))
        #ohc1=pd.get_dummies(val_x)
        #print(x)
        new_diet_data = pd.read_csv('C:/Users/pallavi-pc/Desktop/AIproject/static/test.csv')
        nx=new_diet_data.iloc[:,4]
        ny=new_diet_data.iloc[:,[0,1,2,3]]
        train_x,val_x,train_y,val_y=train_test_split(ny,nx,test_size=0.50,random_state = 0)
        '''ohc=pd.get_dummies(train_x)
        ohc2=pd.get_dummies(val_x)
        ohc3=pd.get_dummies(train_y)
        ohc4=pd.get_dummies(val_y)'''

        kd=diet_data.iloc[:,-10]
        nkd=np.array(kd)
        print(type(nkd))
        le.fit(nkd)
        tkd=le.transform(nkd)

        pd.DataFrame(tkd).to_csv("C:/Users/pallavi-pc/Desktop/AIproject/static/formatted.csv",index = False)
        print(type(tkd))
        print(tkd)
        reversetkd=le.inverse_transform(tkd)
       
        hd=diet_data.iloc[:,-8]
        nhd=np.array(hd)
        le.fit(nhd)
        #list(le.classes)
        thd=le.transform(nhd)
        pd.DataFrame(thd).to_csv("C:/Users/pallavi-pc/Desktop/AIproject/static/formatted2.csv",index = False)
        print(thd)
        reversethd=le.inverse_transform(thd)
        
        dia=diet_data.iloc[:,-9]
        ndia=np.array(dia)
        le.fit(ndia)
        #list(le.classes)
        tdia=le.transform(ndia)
        pd.DataFrame(tdia).to_csv("C:/Users/pallavi-pc/Desktop/AIproject/static/formatted3.csv",index = False)
        print(tdia)
        reversetdia=le.inverse_transform(tdia)
        
        #dec=enc.dot(OHC.active_features_).astype(int)
        #print(dec)
        #print(ohc1)
        #print(val_x)
        my_model=DecisionTreeRegressor(random_state=1)
        my_model.fit(train_x,train_y)

        #print("The predictions are")
        #pred=my_model.predict(val_x)

        pred=my_model.predict([[1,0,1,3600]])
        gt = np.array(train_y)
        #print(pred)
        #print(pred)

        #fpr,tpr,threshold = metrics.roc_curve(gt,pred,pos_label=2)
        #acc = metrics.auc(fpr, tpr)
        #print(acc)
        
        return render(request, 'plan.html', {'input':defg,'users':users})
    else:    
        return render(request, 'diet.html')

    
    return render(request, 'diet.html')