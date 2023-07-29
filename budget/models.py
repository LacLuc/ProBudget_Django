from django.db import models


class monthYear(models.Model):
    MonthYear = models.CharField(max_length=150)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.MonthYear


class category(models.Model):
    category = models.CharField(max_length=150)   
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class fontpayer(models.Model):
    fontpayer = models.CharField(max_length=150)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class expensetype(models.Model):
    expensetype = models.CharField(max_length=150)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class paytype(models.Model):
    paytype = models.CharField(max_length=150)   
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class aporty(models.Model):
    aporty = models.CharField(max_length=150)
    Ativo = models.CharField(max_length=10)
    Bank_Brok = models.CharField(max_length=10)
    MonthYear = models.ForeignKey(
        monthYear, on_delete=models.SET_NULL, null=True
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class credity(models.Model):
    credity = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    MonthYear = models.ForeignKey(
        monthYear, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(max_length=10)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class expense(models.Model):
    expense = models.CharField(max_length=150)
    category_ID = models.ForeignKey(
        category, on_delete=models.SET_NULL, null=True
    )
    expensetype_ID = models.ForeignKey(
        expensetype, on_delete=models.SET_NULL, null=True
    )
    paytype_ID = models.ForeignKey(
        paytype, on_delete=models.SET_NULL, null=True
    )
    paydate = models.DateField(auto_now=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    MonthYear = models.ForeignKey(
        monthYear, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(max_length=10)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class buylist(models.Model):
    qty = models.IntegerField()
    buylist = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valortotal = models.DecimalField(max_digits=10, decimal_places=2)
    MonthYear = models.ForeignKey(
        monthYear, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(max_length=10)
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)


class recipe(models.Model):
    recipe = models.CharField(max_length=150)
    fontpayer_ID = models.ForeignKey(
        fontpayer, on_delete=models.SET_NULL, null=True
    )
    recipedate = models.DateField(auto_now=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)    
    MonthYear = models.ForeignKey(
        monthYear, on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(max_length=10)    
    Create_Data = models.DateTimeField(auto_now_add=True)
    Update_Date = models.DateTimeField(auto_now=True)

    '''cover = models.ImageField(upload_to='budget/covers/%Y/%m/%d/')'''